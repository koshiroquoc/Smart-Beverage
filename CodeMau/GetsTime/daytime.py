from datetime import datetime

# get current datetime
dt = datetime.now()
date_sta="09:50"
date_str="09:51"
# get current datetime
dt = datetime.now()
print(dt.strftime('%x'))
# get weekday name
print('day Name:', dt.strftime('%A'))
print('Datetime is:', dt.now())
print('Weekday is:', dt.isoweekday())
#current_time = dt.strftime("%D:%M:%S")
print("Gio hien tai =", int(dt.strftime("%S")))
gui_canhbao=0
gui_baocao=0
while True:
    dt = datetime.now()
    if dt.strftime("%H:%M")== date_sta:
        if gui_canhbao==0:
            print("gui canh bao")
            gui_canhbao=1
    elif gui_canhbao==1:
        gui_canhbao=0
    if dt.strftime("%H:%M")== date_str and dt.strftime('%A')=='Tuesday':
        if gui_baocao==0:
            print("gui bao cao")
            gui_baocao=1
    elif gui_baocao==1:
        gui_baocao=0


