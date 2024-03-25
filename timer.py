from datetime import datetime
import time
from task import Task
from task_queue import TaskQueue
from dispatcher import Dispatcher

# note: we do not really need a Timer instance when queue is empty

class Timer:
    def __init__(self, task_queue):
        self.dispatcher = Dispatcher()
        self.task_q = task_queue

    def get_curr_datetime():
        return { # convert str to int and then again to str
            'time': ':'.join(list(map(lambda x: str(x), list(map(lambda x: int(x), str(datetime.now().time()).split(':')[:2]))))),
            'date': '-'.join(list(map(lambda x: str(x), list(map(lambda x: int(x), str(datetime.now().date()).split('-'))))))
        }
        # note:
        # the final int to str conversion might not be needed
        # if the Task objects remind_time dictionary has int values

    def start(self):
        print("Timer started.")

        while True:
            # the timer stops as soon as the above while loop is exited
            # and can be restarted again using start()
            # if self.task_q.isEmpty():
            #     break

            if not self.task_q.isEmpty():
                curr = Timer.get_curr_datetime() # dictionary containing current datetime
                remind_time = self.task_q.peek().remind_time

                if curr['date'] == remind_time['date'] and curr['time'] == remind_time['time']:
                    self.dispatcher.dispatch_reminder(self.task_q.dequeue())

            time.sleep(10) # the number of seconds to sleep could be user specifiable


        print("Timer stopped.")

if __name__ == "__main__":
    timer = Timer()
    q = TaskQueue()

    q.insert(Task("20:28", "T 1"))
    # q.insert(Task("16:43", "T 2"))
    # q.insert(Task("16:50", "T 3"))
    # q.insert(Task("16:40", "T 4"))

    timer.start(q)
