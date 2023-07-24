from datetime import datetime
from time_str_manipulation import TimeStr, TimeDict

class Task:
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

    def update_remind_time(self, newVal):
        # this is just for testing
        # according to the current plan,
        # updating remind_time would require expensive
        # queue operations too, like a re-insertion
        # might be, creating and inserting a new Task object
        # and deleting the current one
        #
        # checking the value should not require checking here
        # as it would be checked and converted to a 'time' type
        # before it is passed to this function
        if newVal != "":
            self.remind_time = newVal


if __name__ == "__main__":
    # t = Task("1d 9:40 pm")
    t = Task("1h 2m")
    t.print()
