#include <stdio.h>
#include <string.h>

#define HEAP_SIZE (128*8)

#define USED 1
#define FREE 0

#define BEST_FIT 1
#define FIRST_FIT 0

// private function prototypes
void duInitMalloc(int fitType);
void* duMalloc(int size, int heapNum);
void duFree(void* ptr, int heapIndex);
void printMemoryBlockInfo(int currentYoungHeap);
void printFreeList(int currentYoungHeap);
void printManagedList();


// create the structure to act as a header
typedef struct memoryBlockHeader {
    int type;   // FREE or USED (0 or 1)
    int size;   // size of the reserved block
    int managedIndex; // the unchanging index in the managed array
    int survivalAmt;    // number of times the block has been moved between young heaps
    struct memoryBlockHeader* next;   // the next block in the integrated free list
} memoryBlockHeader;

unsigned char heap[3][HEAP_SIZE];
int currentYoungHeap;
memoryBlockHeader* freeListHeads[3];

// global variable to determine the fit type
int fit;

// global variable to hold the managed list, array of pointers to heap locations
void* managedList[HEAP_SIZE/8];

// global variable to hold the managed list size
int managedListSize = 0;



void duManagedInitMalloc(int searchType) {

    // set current heap to heap[0]
    currentYoungHeap = 0;

    // call original init
    duInitMalloc(searchType);
}



void** duManagedMalloc(int size) {

    void* ptr = duMalloc(size, currentYoungHeap);

    // check if the call to duMalloc failed
    if (ptr == NULL) {
        return NULL;
    }

    // set managedIndex of newBlock
    memoryBlockHeader* newBlock = (memoryBlockHeader*)(ptr - sizeof(memoryBlockHeader));
    newBlock->managedIndex = managedListSize;

    // set newBlock's survivalAmt to 0
    newBlock->survivalAmt = 0;

    // add entry to managedList for this heap block
    managedList[managedListSize] = ptr;

    managedListSize++;

    return (void**)(&managedList[managedListSize-1]);
}



void duManagedFree(void** mptr) {

    // determine whether the pointer to be freed is in young or old memory
    int heapIndex;
    if (*mptr >= heap[2]) {
        heapIndex = 2;
    } else {
        heapIndex = currentYoungHeap;
    }

    // call original duFree
    duFree(*mptr, heapIndex);

    // null out the address at the slot of the managed list being freed
    memoryBlockHeader* ptrHeader = (memoryBlockHeader*)(*mptr-sizeof(memoryBlockHeader));
    managedList[ptrHeader->managedIndex] = NULL;
}



void duInitMalloc(int fitType) {

    // set the global variable 'fit' to the input 'fitType'
    fit = fitType;

    // for each heap...
    for (int j = 0; j < 3; j++) {
        // initialize all memory in the heap to 0
        for (int i = 0; i < HEAP_SIZE; i++) {
            heap[j][i] = 0;
        }

        // stamp the header into the starting 16 bytes of the heap
        memoryBlockHeader* currentBlock = (memoryBlockHeader*)heap[j];

        // set the fields for 'currentBlock'
        currentBlock->size = HEAP_SIZE - sizeof(memoryBlockHeader);
        currentBlock->next = NULL;
        currentBlock->type = FREE;

        // set the freeListHead to point to 'currentBlock'
        freeListHeads[j] = currentBlock;
    }
}



void* duMalloc(int size, int heapNum) {
    
    // if the size is not a multiple of 8, round up to the nearest multiple of 8
    size = ((size+7)/8)*8;
    
    // add space for a free block header after the space the client will be given
    size += sizeof(memoryBlockHeader);

    // find a block in the free list that is large enough to hold the requested size
    memoryBlockHeader* currentFreeBlock = freeListHeads[heapNum];
    memoryBlockHeader* previousFreeBlock = NULL;
    memoryBlockHeader* clientsBlock = NULL;

    // find a block for the client using FIRST_FIT fit setting
    if (fit == FIRST_FIT) {

        while (currentFreeBlock != NULL) {

            // check if a 'currentFreeBlock' is large enough to hold the requested size
            if (currentFreeBlock->size >= size) {
                clientsBlock = currentFreeBlock;
                currentFreeBlock = NULL;
            
            // otherwise move to the next free block in the free list
            } else {
                previousFreeBlock = currentFreeBlock;
                currentFreeBlock = previousFreeBlock->next;
            }
        }
    
    // otherwise find a block for the client using BEST_FIT fit setting
    } else {

        int bestFit = HEAP_SIZE;

        while (currentFreeBlock != NULL) {

            // check if a 'currentFreeBlock' is large enough to hold the requested size
            if (currentFreeBlock->size >= size) {

                // check if a 'currentFreeBlock' is a better fit than the current best fit
                //  (i.e. the block is smaller than the current best fit)  
                if (currentFreeBlock->size < bestFit) {
                    bestFit = currentFreeBlock->size;
                    clientsBlock = currentFreeBlock;
                }
            }

            // continue iterating through the free list
            currentFreeBlock = currentFreeBlock->next;
        }
    }

    // check if we reached the end of the free list without finding a large enough block
    if (clientsBlock == NULL) {
        return NULL;
    }
    
    // if the block is larger than the requested size, split the block
    if (clientsBlock->size > size) {

        // create a new block header for the remaining free space
        memoryBlockHeader* newFreeBlock = (memoryBlockHeader*)((unsigned char*)clientsBlock + size);

        // set the fields for 'newFreeBlock'
        newFreeBlock->size = clientsBlock->size - size;
        newFreeBlock->next = clientsBlock->next;
        newFreeBlock->type = FREE;

        // set the fields for 'clientsBlock'
        clientsBlock->size = size - sizeof(memoryBlockHeader);
        clientsBlock->next = NULL;
        clientsBlock->type = USED;

        // add the new free block to the free list
        if (previousFreeBlock == NULL) {
            freeListHeads[heapNum] = newFreeBlock;
        } else {
            previousFreeBlock->next = newFreeBlock;
        }

    } else {

        // remove the block from the free list
        if (previousFreeBlock == NULL) {
            freeListHeads[heapNum] = currentFreeBlock->next;
        } else {
            previousFreeBlock->next = currentFreeBlock->next;
        }
    }

    // return a pointer to the location where the client's memory begins, after the block header
    return (void*)((unsigned char*)clientsBlock + sizeof(memoryBlockHeader));
}



void duFree(void* ptr, int heapIndex) {

    // find the start of the block header
    memoryBlockHeader* ptrHeader = (memoryBlockHeader*)(ptr - sizeof(memoryBlockHeader));

    // mark 'ptrHeader' as free
    ptrHeader->type = FREE;

    // now splice 'ptrHeader' into the correct position in the free list...

    // check if free list is empty
    if (freeListHeads[heapIndex] == NULL) {
        freeListHeads[heapIndex] = ptrHeader;
        ptrHeader->next = NULL;

    // check if 'ptrHeader' goes at the head of the free list
    } else if (ptrHeader < freeListHeads[heapIndex]) {
        ptrHeader->next = freeListHeads[heapIndex];
        freeListHeads[heapIndex] = ptrHeader;

    // otherwise splice 'ptrHeader' into the free list
    } else {

        // find the correct position in the free list to insert 'ptrHeader'
        memoryBlockHeader* currentFreeBlock = freeListHeads[heapIndex];
        memoryBlockHeader* previousFreeBlock = NULL;

        while (currentFreeBlock != NULL && currentFreeBlock < ptrHeader) {
            previousFreeBlock = currentFreeBlock;
            currentFreeBlock = currentFreeBlock->next;
        }

        // insert 'ptrHeader' at the correct position
        ptrHeader->next = currentFreeBlock;
        previousFreeBlock->next = ptrHeader;
    }
}



void minorCollection() {

    int otherHeap = 1 - currentYoungHeap;
    
    unsigned char* newYoungPosition = heap[otherHeap];

    // loop through managed list
    for (int i = 0; i < managedListSize; i++) {

        // if not NULL and pointing to a block in the young generation, add the block next open position in other heap
        if ((managedList[i] != NULL) && (managedList[i] < heap[2])) {

            memoryBlockHeader* toMove = (memoryBlockHeader*) (managedList[i] - sizeof(memoryBlockHeader));

            // increase the block's survival amount
            toMove->survivalAmt++;

            // check if the survivalAmt is 3
            if (toMove->survivalAmt == 3) {

                // move to the old generation
                unsigned char* newOldPosition = duMalloc(toMove->size, 2);
                memcpy(newOldPosition - sizeof(memoryBlockHeader), toMove, toMove->size + sizeof(memoryBlockHeader));

                // update managed list pointer   
                managedList[i] = newOldPosition;

            } else {

                // block is still in young generation, so move to otherHeap
                memcpy(newYoungPosition, toMove, toMove->size + sizeof(memoryBlockHeader));

                // update managed list pointer
                managedList[i] = newYoungPosition + sizeof(memoryBlockHeader);

                // update newYoungPosition
                newYoungPosition += sizeof(memoryBlockHeader) + toMove->size;
            }
        }
    }

    // create a free block at the end of the new heap
    memoryBlockHeader* newFreeBlock = (memoryBlockHeader*) newYoungPosition;
    newFreeBlock->type = FREE;
    newFreeBlock->next = NULL;
    newFreeBlock->size = HEAP_SIZE - sizeof(memoryBlockHeader) - (newYoungPosition - heap[otherHeap]);
    freeListHeads[otherHeap] = newFreeBlock;

    // make the new heap be the current heap
    currentYoungHeap = otherHeap;
}



void majorCollection() {

    // start at the first free block
    memoryBlockHeader* firstFree = freeListHeads[2];

    int compactionFinished = 0;
    while (!compactionFinished) {

        memoryBlockHeader* nextBlock = (memoryBlockHeader*)((unsigned char*)(firstFree) + firstFree->size + sizeof(memoryBlockHeader));

        // compaction is finished if we have reached the end of the heap
        if (nextBlock >= (heap[2] + HEAP_SIZE)) {

            compactionFinished = 1;

        // if the nextBlock is free...
        } else if (nextBlock->type == FREE) {

            // coalesce nextBlock with firstFree
            firstFree->size += nextBlock->size + sizeof(memoryBlockHeader);
            firstFree->next = nextBlock->next;

        // if the nextBlock is used...
        } else if (nextBlock->type == USED) {

            // save firstFree's members
            memoryBlockHeader* tempNext = firstFree->next;
            int tempSize = firstFree->size;

            // reset firstFree to have the members of nextBlock
            firstFree->size = nextBlock->size;
            firstFree->type = USED;
            firstFree->managedIndex = nextBlock->managedIndex;
            firstFree->survivalAmt = nextBlock->survivalAmt;

            // update the managedList
            managedList[firstFree->managedIndex] = firstFree + sizeof(memoryBlockHeader);

            // move the client memory of nextBlock to the location of the client memory of firstFree
            memcpy(firstFree + sizeof(memoryBlockHeader), nextBlock + sizeof(memoryBlockHeader), nextBlock->size);

            // make a new free list header at the end of the relocated nextBlock
            firstFree = (memoryBlockHeader*)((unsigned char*)(firstFree) + firstFree->size + sizeof(memoryBlockHeader));
            firstFree->next = tempNext;
            firstFree->size = tempSize;
            firstFree->type = FREE;

            // reset the old generation's free list head
            freeListHeads[2] = firstFree;
        }
    }
}



void duMemoryDump() {

    printf("MEMORY DUMP\n");
    printf("Current heap (0/1 young): %d\n", currentYoungHeap);
    printf("Young heap (only the current one)\n");

    // print young memory block
    printMemoryBlockInfo(currentYoungHeap);

    // print young free list
    printFreeList(currentYoungHeap);

    printf("Old Heap\n");

    // print old memory block
    printMemoryBlockInfo(2);

    // print old free list
    printFreeList(2);

    // print managed list
    printManagedList();
}



// helper method to print the entire memory block (addresses and graphical string)
void printMemoryBlockInfo(int heapNum) {

    char cstringRepresentation[HEAP_SIZE/8];
    int cstringIndex = 0;
    char freeLetter = 'a';
    char usedLetter = 'A';

    // print the entire memory block
    printf("Memory Block\n");

    memoryBlockHeader* currentBlock = (memoryBlockHeader*)heap[heapNum];

    while (currentBlock != NULL && currentBlock < (heap[heapNum] + HEAP_SIZE)) {
        
        if (currentBlock->type == FREE) {

            printf("Free at %p, size %d\n", currentBlock, currentBlock->size);

            // add appropriate free letters to 'cstringRepresentation'
            for (int j = 0; j < (currentBlock->size + sizeof(memoryBlockHeader))/8; j++) {
                cstringRepresentation[cstringIndex] = freeLetter;
                cstringIndex++;
            }
            freeLetter++;   

        } else if (currentBlock->type == USED) {

            printf("Used at %p, size %d, surv: %d\n", currentBlock, currentBlock->size, currentBlock->survivalAmt);

            // add appropriate used letters to 'cstringRepresentation'
            for (int j = 0; j < (currentBlock->size + sizeof(memoryBlockHeader))/8; j++) {
                cstringRepresentation[cstringIndex] = usedLetter;
                cstringIndex++;
            }
            usedLetter++;
        }

        // move to the next block
        currentBlock = (memoryBlockHeader*)((unsigned char*)currentBlock + currentBlock->size + sizeof(memoryBlockHeader));

    }

    // add null terminator to 'cstringRepresentation'
    cstringRepresentation[cstringIndex] = 0;

    // print the cstring representation
    printf("%s\n", cstringRepresentation);
}



// helper method to print the free list's memory addresses and sizes
void printFreeList(int heapNum) {

    printf("Free List\n");

    memoryBlockHeader* currentFreeBlock = freeListHeads[heapNum];
    while (currentFreeBlock != NULL) {
        printf("Block at %p, size %d\n", currentFreeBlock, currentFreeBlock->size);
        currentFreeBlock = currentFreeBlock->next;
    }
}



void printManagedList() {

    printf("ManagedList\n");

    for (int i = 0; i < managedListSize; i++) {
        printf("ManagedList[%d] = %p\n", i, managedList[i]);
    }
}