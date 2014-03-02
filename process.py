from random import randint as ri

class Process:

    def __init__(self, pid, burst_time, arrival_time):
        """ 
        self.pid:  Process ID
        self.time: time **REMAINING**
        self.arrived: time entering ready queue
        self.priority: process priority. lower number = higher priority
        """
        self.pid = pid
        self.time = burst_time
        self.arrived = arrival_time
        self.priority = ri(1,4)

    def __str__(self):
        """Simple representation, for debugging only"""
        return "PID: {} ARRIVED: {} TIME REMAINING: {}".format(
                self.pid, self.arrived, self.time)

    def __lt__(self, other):
        """
        Comparison operator included to ensure proper behavior in the
        heap.
        """
        return (self.time < other.time)

    def arrives(self, time):
        print("[time {}ms] Process {} entered ready queue (requires {}ms"
                " CPU time; priority {})".format(
                    time, self.pid, self.time, self.priority))



def create_plist(n=12):
    """
    Returns a list of n Process objects, numbered 1-n. Burst times for 
    each process are 500-4000 ms, randomly generated. If no argument is
    given, default n to 12.
    """
    #for now, don't worry about arrival time
    return [ Process(i, ri(500, 4000), 0) for i in range(1,n+1) ]

