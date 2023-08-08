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

    def display_error(self, err_msg="unknown error"):
        self.dispatcher.dispatch_message("Error Occurred!\n" + err_msg)

    def insert_task(self, task):
        self.task_q.insert(task)

    def remove_task(self, index):
        if self.task_q.remove(index) == None:
            self.display_error("the entered index in inaccessible!")

    def update_remind_time(self, index, new_remind_time_str):
        removed_task = self.remove_task(index)
        if removed_task != None:
            self.create_task(Task(new_remind_time_str, removed_task.title))
        else:
            self.display_error("the entered index in inaccessible!")

    def update_title(self, index, new_val):
        task = self.task_q.peek_at(index)
        if task != None:
            task.update_title(new_val)
        else:
            self.display_error("the entered index in inaccessible!")

    # update task details
    def update_details(self, index, attr, new_val):
        if attr in ['description', 'start_time', 'end_time', 'timing', 'timings']:
            task = self.task_q.peek_at(index)
            if task != None:
                if attr == 'timing' or attr == 'timings':
                    # new_val must be a Tuple : (start_time, end_time)
                    task.update_details_timings(new_val)
                elif attr == 'description':
                    task.update_details_description(new_val)
                elif attr == 'start_time':
                    task.update_details_start_time(new_val)
                else:
                    task.update_details_end_time(new_val)
            else:
                self.display_error("the entered index in inaccessible!")
        else:
            self.display_error("invalid attribute specified!")

    def display_task_queue(self, index_needed=True, details_needed=False, limit=0):
        tasks_tuple = self.task_q.export_schedule_tuple()
        if limit != 0:
            tasks_tuple = tuple([tasks_tuple[i] for i in range(limit)])
        self.dispatcher.dispatch_schedule(tasks_tuple, index_needed, details_needed)

    def display_task_at(self, index, details_needed=False):
        task = self.task_q.peek_at(index)
        if task != None:
            self.dispatcher.dispatch_message(task.export_task_str(details_needed))
        else:
            self.display_error("the entered index in inaccessible!")

if __name__ == "__main__":
    tq = TaskQueue()
    ex = Executor(tq)

    ex.create_task("9:59 PM", "T 1")
    ex.create_task("9:57 PM", "T 2")
    ex.create_task("9:51 PM", "T 3")
    ex.create_task("9:54 PM", "T 4")

    ex.display_task_queue()
    ex.remove_task(1)
    ex.display_task_at(1)
    ex.display_task_queue()
    ex.display_task_at(10)


class Interpreter():
    # interprets the messages sent by the user
    # invokes the executor to execute the desired operation
    def __init__(self, executor):
        self.executor = executor

    def interpret_single_line(self, msg):
        msg = msg.split()
        msg[0] = msg[0].lower()

    def interpret_multi_line(self, msg):
        # create
        # remind_time
        # title
        #
        # description
        # start_time
        # end_time
        msg_len = len(msg)
        msg[0] = msg[0].lower()

        if msg[0] == 'create':
            task = Task(msg[1])
            if msg_len > 2:
                task.update_title(msg[2])
            if msg_len > 4:
                task.update_details_description(msg[4])
            if msg_len > 5:
                task.update_details_start_time(msg[5])
            if msg_len > 6:
                task.update_details_end_time(msg[6])
            self.executor.insert_task(task)
            self.executor.display_task_queue(details_needed=True) # debug command

    def interpret(self, msg):
        msg = msg.splitlines()

        if msg_len == 1:
            self.interpret_single_line(msg)
        else:
            self.interpret_multi_line(msg)
