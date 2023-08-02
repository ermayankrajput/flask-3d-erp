import time

def whatTime():
    obj = time.gmtime(0)
    epoch = time.asctime(obj)
    print("The epoch is:",epoch)
    curr_time = round(time.time()*1000)
    print("Milliseconds since epoch:",curr_time)