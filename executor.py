from task import Task
from task_queue import TaskQueue
from dispatcher import Dispatcher

class Executor:
    # Executor contains functions that execute commands
    # Exeutor object needs a TaskQueue object to initialise
    # as that will be the TaskQueue upon which it performs the operations
    def __init__(self, tq):
        self.task_queue = tq
        self.dispatcher = Dispatcher()

    def create_task(self):
        # create Task object
        # insert Task object in TaskQueue
        pass

    def remove_task(self, index):
        # remove Task object at given index in TaskQueue
        pass

    # update task remind_time
    def update_remind_time(self, index, new_val):
        pass

    # update task details
    def update_details(self, index, attr, new_val):
        # update the specified attribute of the Task details dictionary
        # if attr == 'timing' invoke Task_obj.update_details_time
        pass

    def display_task_queue(self, index_needed):
        # display all Tasks in the TaskQueue
        pass
