from task import Task
from task_queue import TaskQueue
from dispatcher import Dispatcher

class Executor:
    # Executor contains functions that execute commands
    # Exeutor object needs a TaskQueue object to initialise
    # as that will be the TaskQueue upon which it performs the operations
    def __init__(self, task_queue):
        self.task_q = task_queue
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


class Interpreter():
    # interprets the messages sent by the user
    # invokes the executor
    # to execute the desired operation
    # and passes provides it with the required data
    #
    # Acceptible user instruction-message formats :-
    # 1. Based on CREATE instruction
    #   "create {title} {remind time}"
    #   "create {remind time} {title}"
    #   "{title} {remind time}"
    #   "{remind time} {title}"
    #
    # 2. Based on DELETE/REMOVE instruction
    #   "delete/remove {TaskQueue index}"
    #   "delete/remove {title}" : all task objects with matching titles (exact string match) will be removed from the TaskQueue
    #
    # 3. Based on LIST/SHOW instruction
    #   "list/show" : display task objects in TaskQueue with index
    #   "list index" : display task objects in TaskQueue with index
    #   "list noindex" : display task objects in TaskQueue without index
    #   "list {n}" : display the first n task object in TaskQueue
    #
    # 4. Based on PEEK/SHOW instruction
    #   "peek" : display first Task object in TaskQueue
    #   "peek/show {TaskQueue index}"
    #
    # 5. BASED on UPDATE/MODIFY instruction
    #   "update/modify title {TaskQueue index} {new value}"
    #   "update/modify remindtime {TaskQueue index} {new value}"
    #   "update/modify description {TaskQueue index} {new value}"
    #   "update/modify timing/timings {TaskQueue index} {new value}"
    #   "update/modify starttime {TaskQueue index} {new value} {new value}" : start_time and end_time respectively
    #   "update/modify endtime {TaskQueue index} {new value}"
    #
    # Interpreter will accept the above mentioned formats and
    # call the Executor to execute operations accordingly

    def __init__(self, executor):
        self.executor = executor
