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

    def update_details_description(self, new_val):
        if new_val == "":
            try:
                del self.details['description']
            except:
                return
        else:
            self.details['description'] = new_val

    def update_details_start_time(self, new_val):
        if new_val == "":
            try:
                del self.details['start_time']
            except:
                return
        else:
            self.details['start_time'] = new_val

    def update_details_end_time(self, new_val):
        if new_val == "":
            try:
                del self.details['end_time']
            except:
                return
        else:
            self.details['end_time'] = new_val

    def update_details_timings(self, timeTuple):
        st, et = timeTuple
        self.update_details_start_time(st)
        self.update_details_end_time(et)

    def update_title(self, new_val):
        self.title = new_val if new_val != "" else "no title"

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

    def export_details_str(self):
        details_str = ""
        if 'description' in self.details:
            details_str += self.details['description']
        if 'start_time' in self.details or 'end_time' in self.details:
            details_str += "\n\nEvent timings :-"
            if 'start_time' in self.details:
                details_str += "\nstart: " + self.details['start_time']
            if 'end_time' in self.details:
                details_str += "\nend: " + self.details['end_time']
        return details_str

    def export_task_str(self, details_needed):
        task_str = f"Remind time: {self.remind_time['time']}, {self.remind_time['date']}\n"
        task_str += f"Title: {self.title}\n"
        if details_needed:
            details_str = self.export_details_str()
            if details_str != "":
                task_str += "\n" + details_str
        return task_str

if __name__ == "__main__":
    t1 = Task("1h 2m")
    t1.update_details_description("Description of a Task object, for testing.")
    t1.update_details_time(("5:00pm", "9:00pm"))
    t1.update_title("Test Task")
    print(t1.export_task_str(True))
