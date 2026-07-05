# Preemptive round-robin scheduler with priorities, arrival handling, and I/O blocking using Python priority queues
# Simulates CPU execution, preemption, blocking, termination, and computes average turnaround time

from queue import PriorityQueue
import sys



class Process():

    def __init__(self, name, priority, arrival_time, total_time, block_interval):
        self.name = name
        self.priority = priority
        self.arrival_time = arrival_time
        self.total_time = total_time
        self.block_interval = block_interval

        self.time_last_run = 0
        self.time_remaining = total_time
        self.time_until_blocked = block_interval
    
    # in case of ties in priority, order the processes by time last run
    def __lt__(self, other):
        return self.time_last_run < other.time_last_run
    
    # for debugging
    def __str__(self):
        return "%s\t%d\t%d\t%d\t%d" % (self.name, self.priority, self.arrival_time, self.total_time, self.block_interval)




def main():

    # initialize queues and variables
    arrival_queue = PriorityQueue()
    blocked_queue = PriorityQueue()
    ready_queue = PriorityQueue()
    sim_time = 0
    num_processes = 0
    turnaround_total = 0

    # get parameters from command line
    input_file = sys.argv[1]
    time_slice = int(sys.argv[2])
    block_duration = int(sys.argv[3])

    # read input file
    with open(input_file, 'r') as f:

        for line in f:

            # ignore commented lines
            if not line.startswith("#"):
                line = line.split()

                num_processes += 1

                # place all processes on the arrival queue according to priority
                #   negate the priority to use PriorityQueue as a max-heap
                arrival_queue.put((-int(line[1]), Process(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]))))

    # make first output line
    print("timeSlice: %d\tblockDuration: %d" % (time_slice, block_duration))


    # main loop
    while not arrival_queue.empty() or not blocked_queue.empty() or not ready_queue.empty():

        # check for new arrivals
        ready = []
        for arr in arrival_queue.queue:
            # check if the process has arrived
            if arr[1].arrival_time <= sim_time:
                # if so, add it to the ready list (to be cleared from the arrival_queue later) and the ready queue
                ready.append(arr)
                ready_queue.put(arr)
                
        # now clear the ready processes from the arrival queue
        for process in ready:
            arrival_queue.queue.remove(process)


        # check for unblocked processes
        unblocked = []
        for blocked in blocked_queue.queue:
            # check if the process is available to run again
            if sim_time - blocked[1].time_last_run >= block_duration:
                # if so, add it to the unblocked list (to be cleared from the blocked_queue later) and the ready queue
                unblocked.append(blocked)
                ready_queue.put(blocked)

        # now clear the unblocked processes from the blocked queue
        for process in unblocked:
            blocked_queue.queue.remove(process)


        # run the next process in the ready queue
        if not ready_queue.empty():

            # get the highest priority process
            next_process = ready_queue.get()
            
            # determine when the interval ends...

            # if the next process will finish before the time slice...
            if next_process[1].time_remaining <= time_slice:
                status_code = "T"
                interval = next_process[1].time_remaining

                # the process is finished, so no real need to update any of its instance variables
                #   just add the process's turnaround time to the total
                turnaround_total += sim_time + interval - next_process[1].arrival_time


            # if the next process will block before the time slice...
            elif next_process[1].time_until_blocked <= time_slice:
                status_code = "B"
                interval = next_process[1].time_until_blocked

                # reset the time until blocked, time last run, and time remaining
                next_process[1].time_until_blocked = next_process[1].block_interval
                next_process[1].time_last_run = sim_time + interval
                next_process[1].time_remaining -= interval

                # put the process on the blocked queue
                blocked_queue.put(next_process)


            # otherwise...
            else:
                status_code = "P"
                interval = time_slice

                # update the time until blocked, time last run, and time remaining
                next_process[1].time_until_blocked -= interval
                next_process[1].time_last_run = sim_time + interval
                next_process[1].time_remaining -= interval

                # put the process back on the ready queue
                ready_queue.put(next_process)

            # print output line
            print("%d\t%s\t%d\t%s" % (sim_time, next_process[1].name, interval, status_code))

            # update sim time
            sim_time += interval

        # if no processes are ready...
        else:

            # determine the idle interval time
            #   which will be the smallest time interval until a new process arrives or a process unblocks
            interval = min([arr[1].arrival_time - sim_time for arr in arrival_queue.queue] + [blocked[1].time_last_run + block_duration - sim_time for blocked in blocked_queue.queue])

            # print idle line
            print("%d\t(IDLE)\t%d\tI" % (sim_time, interval))

            # update sim time
            sim_time += interval


    # calculate and print average turnaround time
    print("Average turnaround time: %.1f" % (turnaround_total / num_processes))




if __name__ == "__main__":
    main()
