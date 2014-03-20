def simulation(n = 12):
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

    """
    print(n)
    pass


if __name__ == "__main__":
    simulation()
