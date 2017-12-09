import datetime
cur_hour_7 = False
while not cur_hour_7:
    now = datetime.datetime.now()
    print (now.minute, now.second)
    print('*'*10)
    if now.minute == 28:
        gmail.send(msg)
        cur_hour_7 = True
