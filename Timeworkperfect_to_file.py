import datetime as dt
import tkinter


def start(info_list):
    task=input("Enter name of the task")
    info_list.append(task)
    start_time_ho=dt.datetime.now()
    start_time_hour=start_time_ho.hour
    start_time_min=dt.datetime.now()
    start_time_minute=start_time_min.minute
    time_now=f"{start_time_hour}:{start_time_minute}"
    info_list.append(time_now)


def stop(info_list):
    stop_time_ho=dt.datetime.now()
    stop_time_hour=stop_time_ho.hour
    stop_time_min=dt.datetime.now()
    stop_time_minute=stop_time_min.minute
    stop_time_now=f"{stop_time_hour}:{stop_time_minute}"
    info_list.append(stop_time_now)
    date_today=dt.date.today()
    date_print=str(date_today)
    info_list.append(date_print)


running=True
final_list=[]

while running:
    cmd=input(">")
    if cmd=="start":
        nlist=[]
        start(nlist)
        cmc=input(">")
        if cmc=="stop":
            stop(nlist)
            final_list.append(nlist)
            print(f'''
            Task->{nlist[0]}
            Start Time->{nlist[1]}
            Stop Time->{nlist[2]}
            Date->{nlist[3]}''')
        else:
            print("not valid")
            break
    elif cmd=="quit":
        running=False
    else:
        print("Not a valid command")


text_file=open("C:/Users/Stephen/Desktop/Logs.txt", "a")
sstring=str(final_list)
ssstring=sstring+"\n"
text_file.write(ssstring)










