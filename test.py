#!/usr/bin/env python3
from task import *

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
    rt_lst = ["5:15", "5:5AM", "6:00 PM", "2d 4h 3m", "1h5m", "45", "2d", "2d 4:00 PM", "1h 30m 3D"]
    rt_bogus_lst = ["5:a7", "4:4 P M", "60:7", "1 a b 4", "", "0"]

    print("Testing good list...")
    for time_str in rt_lst:
        print("time_str: " + time_str)
        tsk = Task(time_str)
        try:
            tsk.validate_time()
        except ValueError as err:
            print("err: ", err)

    print("Testing bad list...")
    for time_str in rt_bogus_lst:
        print("time_str: " + time_str)
        tsk = Task(time_str)
        try:
            tsk.validate_time()
        except ValueError as err:
            print("err: ", err)


if __name__ == '__main__':
    # test_task()
    test_time_str_validation()
