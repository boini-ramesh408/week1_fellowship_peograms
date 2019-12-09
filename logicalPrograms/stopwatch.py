import time
def stopWatch():

    instruction1=int(input('enter 1 to start..'))
    if instruction1==1:
        start=time.time()
        print(start)
    instruction2 = int(input('enter 2 to start..'))
    if instruction2==2:
        stop=time.time()
        print(stop)
        elapsed_time=stop-start
        print("Diference between start time and stop time is..",int(elapsed_time))
stopWatch()