class CompletedPlist:
    """
    As processes complete, add them to a CompletedPlist. Once a scheduling
    algorithm completes, use methods on this class to calculate minimum, 
    avg, and maximum values for turnaround time, initial wait time, total
    wait time. 
    """
    def __init__(self):
        self.plist = []

    def push(self, p):
        """
        Add a (completed) process to self.plist
        """
        self.plist.append(p)

    def turnaround_time(self):
        min_ = min([p.turnaround for p in self.plist])
        avg_ = sum([p.turnaround for p in self.plist]) / len(self.plist)
        max_ = max([p.turnaround for p in self.plist])

        print("Turnaround time: min {0:.3f}ms; avg {1:.3f}ms; max {2:.3f}"
                " ms".format(min_, avg_, max_))

    def i_wait_time(self):
        min_ = min([p.i_wait for p in self.plist])
        avg_ = sum([p.i_wait for p in self.plist]) / len(self.plist)
        max_ = max([p.i_wait for p in self.plist])

        print("Initial wait time: min {0:.3f}ms; avg {1:.3f}ms; max {2:.3f}"
                " ms".format(min_, avg_, max_))

    def t_wait_time(self):
        min_ = min([p.time_q for p in self.plist])
        avg_ = sum([p.time_q for p in self.plist]) / len(self.plist)
        max_ = max([p.time_q for p in self.plist])

        print("Total wait time: min {0:.3f}ms; avg {1:.3f}ms; max {2:.3f}"
                " ms".format(min_, avg_, max_))

    def statistics(self):
        """
        Calls above methods to print requested message about turnaround time,
        initial wait time, and total wait time.
        """
        self.turnaround_time()
        self.i_wait_time()
        self.t_wait_time()


    



    

    
