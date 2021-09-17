import datetime as dt
list_time=[]
list_date=[]
list_task=[]

start_time = 0
stop_time = 0
task = ''
date_now = dt.datetime.time


def start(time_nowa):
    time_of_start = dt.datetime.now()
    print("start time", time_of_start)
    time_nowa = time_nowa + (time_of_start.hour*60+time_of_start.minute)
    list_time.append(time_nowa)


def stop(time_nowb):
    time_of_stop = dt.datetime.now()
    print("stop time", time_of_stop)
    time_nowb = time_nowb + (time_of_stop.hour*60+time_of_stop.minute)
    list_time.append(time_nowb)


while True:
    commad = input(">")
    if commad == "start":
        task=input("Enter name of task")
        start(start_time)
    elif commad =="stop":
        stop(stop_time)
        st = list_time[0]
        rt = list_time[1]
        print(st, rt)
        time_used = rt - st
        time_remaining = 240 - time_used
        print(f'''
        Task->{task}
        Time used->{time_used}
        ''')
        print(f"Work time remaining->{time_remaining}")

    elif commad =="quit":
        break
    else:
        print("not an real command")





