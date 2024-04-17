import time
currentTime = time.strftime('%H:%M:%S:%p')
print(currentTime)
hour = int(time.strftime('%H'))
amformat = time.strftime('%p')

if(hour <= 12 and amformat =="AM"):
    print("Good Morning")
elif(hour >= 12 and hour <= 16 and amformat =="PM"):
    print("Good Afternoon")
elif(hour >=16 and amformat =="PM"):
    print("Good Evening")
else:
    print("incorrect time")
        
