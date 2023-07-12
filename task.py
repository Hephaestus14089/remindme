class Task:
    def __init__(self, remind_time, title="no title"):
        self.title = title
        self.remind_time = remind_time
        self.details = {}

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

    def print(self):
        print(f"title: {self.title}")
        print(f"remind_time: {self.remind_time}")

        if self.details:
            print(self.details)

    def validate_time(self):
        # format of remind_time :-
        # hrs[:]mins (24hr clock)
        # hrs[:]mins[AM/PM] (12hr clock)
        # hrs[:]mins [AM/PM] (12hr clock)
        # hrs[h]mins[m] (current time + entered)
        # hrs[h] mins[m] (current time + entered)
        # mins (current time + entered)
        # days[d] (along with h and m: + current time)

        time_str = self.remind_time


        if time_str == "" or time_str == "0":
            raise ValueError("invalid time format")

        time_str_lst = time_str.split()

        if len(time_str_lst) > 3:
            raise ValueError("invalid time format")

        # time_dict can have the following attributes:-
        #
        # clock: 'h:m' format (if twelve_hr attr is not present, assume 24 hr)
        # twelve_hr: AM/PM (must have clock attr)
        # days: n days
        #
        # or
        #
        # days: n days
        # hrs: n hrs
        # mins: n mins
        #
        time_dict = {}

        # loop through time_str_lst and create time_dict
        for element in time_str_lst:
            pass

        # validate time_dict

        return time_dict
