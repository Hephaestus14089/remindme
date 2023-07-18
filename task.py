from datetime import datetime

class Task:
    def __init__(self, remind_time, title="no title"):
        self.title = title
        self.remind_time = remind_time
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
        # d: n days
        #
        # or
        #
        # d: n days
        # h: n hrs
        # m: n mins
        #
        time_dict = {}

        def validate_time_str_attr(attr):

            def check_if_twelve_hr():
                if attr.upper() in ['AM', 'PM']:
                    if 'twelve_hr' in time_dict:
                        raise ValueError("invalid time format: repeating AM/PM specification")

                    time_dict['twelve_hr'] = attr.upper()
                    return True

                return False

            def check_if_clock():
                if ':' in attr:
                    if 'clock' in time_dict:
                        raise ValueError("invalid time format: repeating 'h:m' time specification")

                    clock_lst = attr.split(':')

                    if len(clock_lst) != 2:
                        raise ValueError("invalid time format: bad 'h:m' time specification")

                    try:
                        clock_lst[0] = int(clock_lst[0])
                        clock_lst[1] = int(clock_lst[1])
                    except:
                        raise ValueError("invalid time format: bad 'h:m' time specification")

                    if clock_lst[0] < 0 or clock_lst[1] < 0:
                        raise ValueError("invalid time format: bad 'h:m' time specification")
                    elif clock_lst[0] > 23 or clock_lst[1] > 59:
                        raise ValueError("invalid time format: bad 'h:m' time specification")

                    time_dict['clock'] = { 'h': clock_lst[0], 'm': clock_lst[1] }
                    return True

                return False

            def check_if_dhm():
                d_h_m = attr[len(attr) - 1:].lower()

                if d_h_m in ['d', 'h', 'm']:
                    n = attr[:len(attr) - 1]

                    try:
                        n = int(n)
                    except:
                        raise ValueError("invalid time format: bad D, H or M specification")

                    if d_h_m in time_dict:
                        raise ValueError("invalid time format: repeating argument")

                    time_dict[d_h_m] = n
                    return True

                return False

            def check_if_single_integer():
                # a single integer will be treated as minutes
                if 'm' in time_dict:
                    raise ValueError("invalid time format: possible repeatative argument")

                try:
                    time_dict['m'] = int(attr)
                    return True
                except:
                    raise ValueError("invalid time format")

                return False

            # the order for checking the attributes in the time string
            check_if_twelve_hr() or check_if_clock() or check_if_dhm() or check_if_single_integer()

        def validate_time_dict():
            bad_cases  = []

            if 'clock' in time_dict:
                bad_cases.append('h' in time_dict or 'm' in time_dict)
                bad_cases.append('twelve_hr' in time_dict and (time_dict['clock']['h'] > 12 or time_dict['clock']['h'] < 1))
            else:
                bad_cases.append('twelve_hr' in time_dict)

            good = True
            for bad_case in bad_cases:
                good = good and not bad_case
                if not good:
                    raise ValueError("invalid time format: bad combination of arguments")

        print("time_str_lst: ", time_str_lst) # debug output

        # loop through time_str_lst and create time_dict
        for attr in time_str_lst:
            validate_time_str_attr(attr)

        # validate  time_dict
        validate_time_dict()

        return time_dict

    def convert_time_dict(self, time_dict):
        # the final time_dict must contain
        # only the following attributes :-
        # 'date': y-m-d
        # 'time': h:m
        # the final time_dict will replace remind_time

        now = list(map(lambda x: int(x), str(datetime.now().time()).split(':')[:2]))
        today = list(map(lambda x: int(x), str(datetime.now().date()).split('-')))

        def create_clock():
            pass

        # converts clock from 12hr to 24hr format
        def convert_clock():
            if time_dict['twelve_hr'] == 'AM':
                if time_dict['clock']['h'] == 12:
                    time_dict['clock']['h'] = 0
            else:
                if time_dict['clock']['h'] != 12:
                    time_dict['clock']['h'] += 12

        def check_datetime_validity():
            # confirm that the date/time is in the future
            def check_date():
                y, m, d = list(map(lambda x: int(x), time_dict['date'].split('-')))
                if (today[0] > y):
                    return False
                elif (today[0] == y): # this year
                    if (today[1] > m):
                        return False
                    elif (today[1] == m): # this month
                        if (today[2] > d):
                            return False
                return True

            def check_time():
                h, m = list(map(lambda x: int(x), time_dict['time'].split(':')))
                if h < now[0]:
                    return False
                elif h == now[0]:
                    if m <= now[1] + 2:
                        return False
                return True

            if not check_date():
                return False
            if time_dict['date'] == '-'.join(list(map(lambda x: str(x), today))):
                return check_time()
            return True

        if 'twelve_hr' in time_dict:
            convert_clock() # convert clock to 24hr format

        # create 'time' attribute
        time_dict['time'] = str(time_dict['clock']['h']) + ':' + str(time_dict['clock']['m'])

        # create 'date' attribute
        date = today
        date[2] += time_dict['d'] if 'd' in time_dict else 0
        time_dict['date'] = '-'.join(list(map(lambda x: str(x), date)))

        # remove unnecessary data
        time_dict = {
            'time': time_dict['time'],
            'date': time_dict['date']
        }

        # final date/time validity check
        if not check_datetime_validity():
            raise ValueError("date/time invalid")

        return time_dict


if __name__ == "__main__":
    t = Task("01:5")
    time_dict = t.validate_time()
    print(t.convert_time_dict(time_dict))
