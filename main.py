# ============================================================================
# Joe Pringle (661114638), CSCI-4210 OpSys, main.py

#      *** RUNNING INSTRUCTIONS ***
#
#           python3 main.py
#
#      ****************************

# ============================================================================
import process as pr
import process_priority as prp
from copy import deepcopy
from completed_plist import CompletedPlist
from sjf import sjf
from sjf_preemption import sjf_preemption
from roundrobin import roundrobin
from roundrobin_priority import roundrobin_priority
from fcfs_aging import fcfs_aging
# ============================================================================


def simulation(n=12):
    """
    n is an optional argument specifying the number of processes in the
    simulation. n defaults to 12.

    Create a list of processes, then run these processes through the
    following scheduling algorithms, in order:

    1. SJF (no preemption)
    2. SJF (with preemption)
    3. Round-Robin (preemption, time slice defaults to 200ms)
    4. Preemptive-Priority via Round-Robin 
            (default time slice 100ms)
    5. Preemptive-Priority with aging via Round-Robin 
            (default time slice 100ms)

    After each algorithm runs, it returns a CompletedPlist. Each
    process records information about itself as it runs, and the 
    statistics() method on a CompletedPlist computes min/avg/max
    values for turnaround time, initial wait time, and total
    wait time.

    Although the time for a context switch (TCS) is set as a global variable, 
    I don't reccommend changing it. The instructions said that 7ms of the 
    switch was for removing a "before" process, and 10ms of the switch 
    was for selecting the next process. There was no provided information 
    on how to scale these values for different values of TCS. 

    To change the 10/90 arrival time distribution, look at the top of 
    process_priority.py. At the top, there is a global variable called 
    PERCENT_ARRIVING_TIME_ZERO, defaulted to 10.

    """
    plist = prp.create_plist()
    simulations = [sjf, sjf_preemption, roundrobin,
                   roundrobin_priority, fcfs_aging]

    for sim in simulations:
        # for clarity, print the name of the simulation
        print("RUNNING {}".format(sim.__name__), end='\n\n')

        # python passes all lists by reference, so copy plist to not
        cpy = deepcopy(plist)

        # run the simulation
        plist_completed = sim(cpy)

        # print statistics after scheduling completes
        print(end='\n')
        plist_completed.statistics()
        print(end='\n')


if __name__ == "__main__":
    simulation()
