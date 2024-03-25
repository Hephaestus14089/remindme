#!/usr/bin/env python3
from task import Task


def test_task():
    t1 = Task("2:30")
    t1.print()

    t1.update_title("title_test")
    t1.update_remind_time("3:30")
    t1.update_details_description("test description")
    t1.update_details_time(("4:00PM", "6:00PM"))
    t1.print()

    t1.update_title("")
    t1.update_details_start_time("5:00")
    t1.update_details_end_time("")
    t1.print()

    t1.update_remind_time("")
    t1.update_details_time(("", ""))
    t1.print()


def test_time_str_validation():
    rt_lst = ["5:15", "6:00 PM", "2d 4h 3m", "45", "2d", "2d 4:00 PM", "1h 30m 3D", "5:03 AM 2d", "2d 4m"]
    # rt_lst.append("5:5AM", "1h5m")
    rt_bogus_lst = ["5:a7", "4:4 P M", "60:7", "0:30 PM", "1 a b 4", "", "0", "6a", "2m 8", "00:20 PM"]

    print("Testing good list...")
    for time_str in rt_lst:
        print("case input string:", time_str)
        tsk = Task(time_str)
        try:
            time_dict = tsk.validate_time()
            print('Y  ', time_dict)
        except ValueError as err:
            print('X  ', err)

    print("\nTesting bad list...")
    for time_str in rt_bogus_lst:
        print("case input string:", time_str)
        tsk = Task(time_str)
        try:
            time_dict = tsk.validate_time()
            print('Y  ', time_dict)
        except ValueError as err:
            print('X  ', err)


if __name__ == '__main__':
    # test_task()
    test_time_str_validation()
