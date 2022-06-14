import time


class StopWatch:

    def calculateTime(self):
        print("process has started")
        try:
           start_time = time.time()
           input("press Enter key to start the time ")
           end_time = time.time()
           input("press Enter key to stop the time ")
        except:
           elapsedtime=end_time - start_time

obj = StopWatch()
elapseTime = obj.calculateTime()