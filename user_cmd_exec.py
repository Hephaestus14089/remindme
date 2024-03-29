from task import Task
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
        if self.task_q.remove(index) is None:
            self.display_error("the entered index in inaccessible!")

    def update_remind_time(self, index, new_remind_time_str):
        removed_task = self.task_q.remove(index)
        if removed_task is not None:
            self.insert_task(Task(new_remind_time_str, removed_task.title))
        else:
            self.display_error("the entered index in inaccessible!")

    def update_title(self, index, new_val):
        task = self.task_q.peek_at(index)
        if task is not None:
            task.update_title(new_val)
        else:
            self.display_error("the entered index in inaccessible!")

    # update task details
    def update_details(self, index, attr, new_val):
        if attr in [
            'description',
            'start_time',
            'end_time',
            'timing',
            'timings'
        ]:
            task = self.task_q.peek_at(index)
            if task is None:
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

    def display_task_queue(
        self,
        index_needed=True,
        details_needed=False,
        limit=0
    ):
        tasks_tuple = self.task_q.export_schedule_tuple()

        if limit != 0:
            tasks_tuple = tuple([tasks_tuple[i] for i in range(limit)])

        self.dispatcher.dispatch_schedule(
            tasks_tuple,
            index_needed,
            details_needed
        )

    def display_task_at(
            self,
            index,
            details_needed=False
    ):
        task = self.task_q.peek_at(index)

        if task is None:
            self.dispatcher.dispatch_message(
                task.export_task_str(details_needed)
            )
        else:
            self.display_error("the entered index in inaccessible!")


class Interpreter():
    # interprets the messages sent by the user
    # invokes the executor to execute the desired operation
    def __init__(self, executor):
        self.executor = executor

    def interpret_single_line(self, msg):
        msg = msg.split()
        msg_len = len(msg)
        msg[0] = msg[0].lower()

        if msg[0] == 'create':
            # create {remind_time} {title}
            # create {remind time}
            if msg_len < 2:
                self.executor.display_error("Bad command")
                return
            task = Task(msg[1])  # wrap in try catch
            title = ' '.join(msg[2:])
            task.update_title(title)
            self.executor.insert_task(task)

        elif msg[0] == 'delete' or msg[0] == 'remove':
            if msg_len < 2:
                self.executor.display_error("Bad command")
                return
            # wrap in try catch
            self.executor.remove_task(int(msg[1]))

        elif msg[0] == 'list':
            index_needed = True
            details_needed = False
            limit = 0
            for item in msg[1:]:
                if item == 'index':
                    index_needed = True
                elif item == 'noindex':
                    index_needed = False
                elif item == 'details':
                    details_needed = True
                elif item == 'nodetails':
                    details_needed = False
                else:
                    # wrap in try catch
                    limit = int(item)
            self.executor.display_task_queue(
                index_needed,
                details_needed,
                limit
            )

        elif msg[0] == 'update' or msg[0] == 'modify':
            if msg_len < 4:
                self.executor.display_error("bad command format")
            index = int(msg[1])  # wrap in try catch
            new_val = ' '.join(msg[3:])
            if msg[2] == 'title':
                self.executor.update_title(
                    index,
                    new_val
                )
            elif msg[2] == 'remindtime' or msg[2] == 'remind':
                self.executor.update_remind_time(
                    index,
                    new_val
                )
            else:
                self.executor.update_details(
                    index,
                    msg[2],
                    new_val
                )

        elif msg[0] == 'peek':
            details_needed = False
            index = 0
            for item in msg[1:]:
                item = item.lower()
                if item == 'details':
                    details_needed = True
                elif item == 'nodetails':
                    details_needed = False
                else:
                    # wrap in try catch
                    index = int(item)
            self.executor.display_task_at(
                index,
                details_needed
            )

        elif msg[0] == 'show':
            details_needed = False
            index_needed = True
            limit = 0
            for item in msg[1:]:
                item = item.lower()
                if item == 'details':
                    details_needed = True
                elif item == 'nodetails':
                    details_needed = False
                elif item == 'index':
                    index_needed = True
                elif item == 'noindex':
                    index_needed = False
                else:
                    # wrap in try catch
                    limit = int(item)
            try:
                index = int(msg[1])
                self.executor.display_task_at(
                    index,
                    details_needed
                )
            except ValueError:
                self.executor.display_task_queue(
                    index_needed,
                    details_needed,
                    limit
                )

        else:
            self.executor.display_error("unknown command")

    def interpret_multi_line(self, msg):
        # create
        # remind_time
        # title
        #
        # description
        # start_time
        # end_time
        msg_len = len(msg)
        divider_index = 2  # empty string before description

        for i in range(msg_len):
            msg[i] = msg[i].strip()

        msg[0] = msg[0].lower()

        if msg[0] == 'create':
            # wrap in try catch
            task = Task(msg[1])

            if msg_len > 2:
                if msg[2] == '':
                    divider_index = 2
                else:
                    task.update_title(msg[2])
                    divider_index = 3
            if msg_len > divider_index + 1:
                task.update_details_description(msg[divider_index + 1])
            if msg_len > divider_index + 2:
                task.update_details_start_time(msg[divider_index + 2])
            if msg_len > divider_index + 3:
                task.update_details_end_time(msg[divider_index + 3])

            self.executor.insert_task(task)
            self.executor.display_task_queue(details_needed=True)  # debug command

    def interpret(self, msg):
        msg = msg.splitlines()
        if len(msg) == 1:
            self.interpret_single_line(msg[0])
        else:
            self.interpret_multi_line(msg)
