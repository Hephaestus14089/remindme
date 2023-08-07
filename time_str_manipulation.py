from datetime import datetime

class TimeStr:
    def __init__(self):
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
        self.time_dict = {}

    def validate_time_str_attr(self, attr):
        time_dict = self.time_dict

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

    def validate_time_dict(self):
        time_dict = self.time_dict
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

    def validate_time_str(time_str):
        # format of remind_time :-
        # hrs[:]mins (24hr clock)
        # hrs[:]mins[AM/PM] (12hr clock)
        # hrs[:]mins [AM/PM] (12hr clock)
        # hrs[h]mins[m] (current time + entered)
        # hrs[h] mins[m] (current time + entered)
        # mins (current time + entered)
        # days[d] (along with h and m: + current time)

        obj = TimeStr()
        time_dict = obj.time_dict

        if time_str == "" or time_str == "0":
            raise ValueError("invalid time format")

        time_str_lst = time_str.split()

        if len(time_str_lst) > 3:
            raise ValueError("invalid time format")

        print("time_str_lst: ", time_str_lst) # debug output

        # loop through time_str_lst and create time_dict
        for attr in time_str_lst:
            obj.validate_time_str_attr(attr)

        # validate  time_dict
        obj.validate_time_dict()

        return time_dict


class TimeDict:
    time_gap_minutes = 3 # minimum gap needed for the remind_time of the next Task object (in mins)

    def get_curr_time():
        return list(map(lambda x: int(x), str(datetime.now().time()).split(':')[:2]))

    def get_curr_date():
        return list(map(lambda x: int(x), str(datetime.now().date()).split('-')))

    def create_clock(time_dict):
        now = TimeDict.get_curr_time()
        time_dict['clock'] = { 'h': now[0], 'm': now[1] + TimeDict.time_gap_minutes }

        if 'h' in time_dict:
            time_dict['clock']['h'] += time_dict['h']
            time_dict['d'] = (time_dict['d'] if 'd' in time_dict else 0) + (time_dict['clock']['h'] // 24)
            time_dict['clock']['h'] %= 24
        if 'm' in time_dict:
            time_dict['clock']['m'] += time_dict['m']
            time_dict['clock']['h'] += time_dict['clock']['m'] // 59
            time_dict['clock']['m'] %= 59

    # converts clock from 12hr to 24hr format
    def convert_clock(time_dict):
        if time_dict['twelve_hr'] == 'AM':
            if time_dict['clock']['h'] == 12:
                time_dict['clock']['h'] = 0
        else:
            if time_dict['clock']['h'] != 12:
                time_dict['clock']['h'] += 12

    def format_date(date):
        # date = [year, month, day]
        y, m, d = date
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (y % 4 == 0): # leap year (gregorian calander)
            if not (y % 100 == 0 and not y % 400 == 0):
                days_in_month[1] += 1
        # incomplete function

    def check_time_validity(time_dict):
        now = TimeDict.get_curr_time()

        # confirm that the time is in the future
        def check_time():
            h, m = list(map(lambda x: int(x), time_dict['time'].split(':')))
            if h < now[0]:
                return False
            elif h == now[0]:
                if m < now[1] + TimeDict.time_gap_minutes:
                    return False
            return True

        if time_dict['date'] == '-'.join(list(map(lambda x: str(x), TimeDict.get_curr_date()))):
            return check_time()

        return True

    def convert_time_dict(time_dict):
        # the final time_dict must contain
        # only the following attributes :-
        # 'date': y-m-d
        # 'time': h:m
        # the final time_dict will replace remind_time

        if 'twelve_hr' in time_dict:
            TimeDict.convert_clock(time_dict) # convert clock to 24hr format

        if 'clock' not in time_dict:
            TimeDict.create_clock(time_dict)

        # create 'time' attribute
        time_dict['time'] = str(time_dict['clock']['h']) + ':' + str(time_dict['clock']['m'])

        # create 'date' attribute
        date = TimeDict.get_curr_date()
        date[2] += time_dict['d'] if 'd' in time_dict else 0
        # format_date(date)
        time_dict['date'] = '-'.join(list(map(lambda x: str(x), date)))

        # remove unnecessary data
        time_dict = {
            'time': time_dict['time'],
            'date': time_dict['date']
        }

        # print(time_dict)

        # final time validity check
        if not TimeDict.check_time_validity(time_dict):
            raise ValueError("time invalid")

        return time_dict
