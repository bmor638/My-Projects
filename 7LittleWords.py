# Beckett Morris
# 10/07/2021
# Program purpose: To recreate the game '7 Little Words' with Environmental Science vocabulary!

# I think I spent about 2 hours on this lab.
# The most challenging part was checking if the guess matched a word and removing the used chunks.
# To overcome this challenge, I thought about the pseudocode for the task and translated that into Python piece by piece. I also ran the program often to check my progress.
# Seeing my final product come together was the most fun! My mom loves puzzle-type games, so I had her play it, too!
# Instead of changing the used chunks to three spaces, I want to try to rework my code so that I can remove the used chunks from the 'chunks' list entirely.

from random import shuffle

# Heading
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("*                         Let's play...                         *")
print("*         7 LITTLE WORDS: Environmental Science Edition         *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

# Create lists of definitions, words, spaces (for tidy output), word lengths, wordsSolved, and chunks of letters
definitions = ["You can't trust them because they make up everything", "Vanished", "The monomer of nucleic acids", "Man-made", "Variety of life", "Robbers steal jewels, scientists steal...", "Randomness in a system"]
words = ["ATOMS", "EXTINCT", "NUCLEOTIDES", "ANTHROPOGENIC", "BIODIVERSITY", "JOULES", "ENTROPY"]
spaces = ["  ", "                                              ", "                          ", "                                              ", "                                       ", "             ", "                                "]
letCount = [len(words[0]), len(words[1]), len(words[2]), len(words[3]), len(words[4]), len(words[5]), len(words[6])]
answerSlot = [str(letCount[0]) + " letters", str(letCount[1]) + " letters", str(letCount[2]) + " letters", str(letCount[3]) + " letters", str(letCount[4]) + " letters", str(letCount[5]) + " letters", str(letCount[6]) + " letters"]
wordsSolved = ["no", "no", "no", "no", "no", "no", "no"]
chunks = [["ATO", "MS ", "EXT", "INC", "T  "], ["NUC", "LEO", "TID", "ES ", "ANT"], ["HRO", "POG", "ENI", "C  ", "BIO"], ["DIV", "ERS", "ITY", "JOU", "LES"], ["ENT", "ROP", "Y  "]]    

# Shuffle chunks
shuffle(chunks)

# Funtion purpose: print definitions, word lengths, and letter chunks
def output(): 
   # Print definitions and word lengths
   for i in range(len(words)):
      print(definitions[i] + spaces[i] + answerSlot[i])
   print("")
   # Print chunks
   print ("\n".join("            ".join(el for el in row) for row in chunks))
   print("")   

# Function purpose: take in a user-entered guess,
# check if the guess matches a word,
# remove used chunks, and
# print a message once all words are solved.
def guessAndPost():
   while (wordsSolved.count("no") != 0):
      # User input
      guess = input ("Enter your guess: ")
      guess = guess.upper()
       # Check if guess matches a word
      for i in range(len(words)):
         if (guess == words[i]):
            wordsSolved[i] = "yes"
            answerSlot[i] = guess
            guess = guess + "   " # Add 3 spaces to guess in order to account for words that are not divisible by 3
            threes = [guess[i:i+3] for i in range(0, len(guess), 3)] # Split guess into groups of 3 characters
            # Hide used chunks
            for three in threes:
               for i in range(len(chunks)):
                  for j in range(len(chunks[i])):
                     if(chunks[i][j] == three):
                        chunks[i][j] = "   "
            output()
   # Print completion message
   print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
   print("*         YOU HAVE SOLVED THIS PUZZLE!!!!!!!!!!!!!!!!!!         *")
   print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
 
# Function calls   
output()
guessAndPost()