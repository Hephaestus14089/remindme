from datetime import datetime
from time_str_manipulation import TimeStr, TimeDict

class Task:
    # anatomy of a Task object :-
    # remind_time = { time, date }
    # title = ""
    #`details = {
    #   description: ""
    #   start_time: ""
    #   end_time: ""
    # }`
    def __init__(self, remind_time_str, title="no title"):
        self.remind_time = TimeDict.convert_time_dict(TimeStr.validate_time_str(remind_time_str))
        self.title = title
        self.details = {}

    def print(self):
        print(f"title: {self.title}")
        print(f"remind_time: {self.remind_time}")

        if self.details:
            print(self.details)

    def update_details_description(self, newVal):
        self.details['description'] = newVal

    def update_details_start_time(self, newVal):
        if newVal == "":
            try:
                del self.details['start_time']
            except:
                return
        else:
            self.details['start_time'] = newVal

    def update_details_end_time(self, newVal):
        if newVal == "":
            try:
                del self.details['end_time']
            except:
                return
        else:
            self.details['end_time'] = newVal

    def update_details_time(self, timeTuple):
        st, et = timeTuple
        self.update_details_start_time(st)
        self.update_details_end_time(et)

    def update_title(self, newVal):
        self.title = newVal if newVal != "" else "no title"

    def compare_remind_time(self, task_other):
        # compares remind_time of two Task objects
        # returns integer value :-
        # positive if remind_time is further than the other object
        # negative if remind_time is nearer than the other object
        # 0 if equal
        remind_time_this = self.remind_time
        remind_time_that = task_other.remind_time

        def compare_date():
            date_this = list(map(lambda x: int(x), remind_time_this['date'].split('-')))
            date_that = list(map(lambda x: int(x), remind_time_that['date'].split('-')))
            y_diff, m_diff, d_diff = [date_this[i] - date_that[i] for i in range(3)]
            if y_diff != 0:
                return y_diff
            if m_diff != 0:
                return m_diff
            return d_diff

        def compare_time():
            time_this = list(map(lambda x: int(x), remind_time_this['time'].split(':')))
            time_that = list(map(lambda x: int(x), remind_time_that['time'].split(':')))
            h_diff, m_diff = [time_this[i] - time_that[i] for i in range(2)]
            return h_diff if h_diff != 0 else m_diff

        date_diff = compare_date()
        return date_diff if date_diff != 0 else compare_time()

    def get_details_str(self):
        details_str = ""
        if 'description' in self.details:
            details_str += self.details['description']
        if 'start_time' in self.details or 'end_time' in self.details:
            reminder_str += "\n\nEvent timings :-"
            if 'start_time' in self.details:
                reminder_str += "\nstart: " + task_obj.details['start_time']
            if 'end_time' in self.details:
                reminder_str += "\nend: " + task_obj.details['end_time']
        return details_str

    def export_task_str(self, details_needed):
        task_str = f"Remind time: {self.remind_time}\n"
        task_str += f"Title: {self.title}\n"
        if details_needed:
            task_str += "\n" + self.get_details_str()
        return task_str

if __name__ == "__main__":
    # t = Task("1d 9:40 pm")
    t1 = Task("1h 2m")
    t2 = Task("1h 5m")
    print(t1.compare_remind_time(t2))
