# ============================================================================
# Joe Pringle (661114638), CSCI-4210 OpSys, process_priority.py
# ============================================================================
from random import randint as ri
from random import expovariate
import math

# Change this to test different distributions of arrival times
#=============================================================================
PERCENT_ARRIVING_TIME_ZERO = 10
#=============================================================================


class Process:

    def __init__(self, pid, burst_time, arrival_time):
        """
        self.pid:  Process ID
        self.time: time **REMAINING**
        self.arrived: time entering ready queue
        self.priority: process priority. lower number = higher priority
        self.popped: time FIRST popped out of q
        self.time_q: total time spent waiting in q
        self.turnaround: turnaround time, computed as process completes
        self.iwait: initial wait time
        """
        self.pid = pid
        self.time = burst_time
        self.arrived = arrival_time
        self.popped = None
        self.time_q = 0
        self.priority = ri(0, 4)
        self.turnaround = 0
        self.i_wait = 0

    def __str__(self):
        """Simple representation, for debugging only"""
        return "PID: {} PRIORITY: {} TIME REMAINING: {}".format(
            self.pid, self.priority, self.time)

    def __lt__(self, other):
        """
        Comparison operator included to ensure proper behavior in the
        heap/ready_q. Lower number indicated higher priority.
        """
        return (self.priority < other.priority)

    def arrives(self, time):
        """Print message indicating process has arrived in ready_q"""

        print("[time {}ms] Process {} entered ready queue (requires {}ms"
              " CPU time; priority {})".format(
                  time, self.pid, self.time, self.priority))

    def ages(self, time):
        """
        Print message indicating process has increased priority due
        to aging. A process with priority 0 cannot be aged.
        """
        self.priority -= 1

        if (self.priority < 0):
            self.priority = 0

        else:
            print("[time {}ms] Increased priority of process {} to {} due to"
                  " aging".format(time, self.pid, self.priority))

    def is_complete(self):
        """return true if process has no time remaining"""
        return (self.time == 0)

    def completes(self, time):
        """print message indicating process has completed"""
        # this will change somewhat when initial/total wait times are
        # not the same. Going to keep track of total time in q

        print("[time {}ms] Process {} CPU burst done (turnaround time"
              " {}ms, initial wait time {}ms, total wait time"
              " {}ms)".format(time, self.pid, time - self.arrived,
                              self.popped - self.arrived, self.time_q))

        self.turnaround = time - self.arrived
        self.i_wait = self.popped - self.arrived

#=============================================================================


def switches(old, new, time):
    """
    print message indicating a context switch, swapping out process
    old for process new
    """
    if (old is None):
        print("[time {}ms] Context switch (Adding process {} (priority {}),"
              " no process currently in CPU)".format(
                  time, new.pid, new.priority))
    else:
        print("[time {}ms] Context switch (swapping out process {}"
              " (priority {}) for process {} (priority {}))".format(
                  time, old.pid, old.priority, new.pid, new.priority))


def create_plist(n=12):
    """
    Returns a list of n Process objects, numbered 1-n. Burst times for
    each process are 500-4000 ms, randomly generated. If no argument is
    given, default n to 12. Arrival times are based on an exponential
    distribution averaging 800ms.
    """
    times = get_process_times(n, PERCENT_ARRIVING_TIME_ZERO)
    return [Process(i, ri(500, 4000), j) for i, j in zip(
        range(1, n + 1), times)]


def get_process_times(n, PERCENT_ARRIVING_TIME_ZERO):
    """
    Return the lengths of n random processes, as a list. A percentage start
    at time 0, and the rest are exponentially distributed.
    Times over 5000ms are ignored.
    """
    times = [0 for i in range(math.floor(
        n * PERCENT_ARRIVING_TIME_ZERO / 100))]

    while (len(times) < n):
        tmp = math.floor(expovariate(1 / 800))
        if (tmp < 5000):
            times.append(tmp)

    return times
