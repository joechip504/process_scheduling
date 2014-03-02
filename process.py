from random import randint as ri

# Change this to test different distributions of arrival times
#=============================================================================
PERCENT_ARRIVING_TIME_0 = 10 
#=============================================================================

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
        self.priority = ri(1, 4)

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
        """print message indicating process has arrived in ready_q"""

        print("[time {}ms] Process {} entered ready queue (requires {}ms"
              " CPU time; priority {})".format(
                  time, self.pid, self.time, self.priority))

    def is_complete(self):
        """return true if process has no time remaining"""
        return (self.time == 0)

    def completes(self, time):
        """print message indicating process has completed"""

        print("[time {}ms] Process {} CPU burst done (turnaround time"
              " {}ms, initial wait time {}ms, total wait time"
              " {}ms".format(time, self.pid, time - self.arrived, 0, 0))


def create_plist(n=12):
    """
    Returns a list of n Process objects, numbered 1-n. Burst times for 
    each process are 500-4000 ms, randomly generated. If no argument is
    given, default n to 12.
    """
    # for now, don't worry about arrival time
    return [Process(i, ri(500, 4000), ri(0, 3)) for i in range(1, n + 1)]

def get_process_times(n, PERCENT_ARRIVING_TIME_0):
  """
  return the lengths of n random processes, as a list. 10% start at time 0, 
  and the rest are exponentially distributed. Times over 5000ms are ignored.
  """
  pass
