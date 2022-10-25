import datetime
import time
from playsound import playsound


alarmHour = int (input("Enter hour:"))
alarmMin = int(input("Enter minutes:"))
alarmAm= input("am  /  pm: ")

if alarmAm=="pm":
    alarmHour+=12

while True:
        
             
           
            if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minutes:
                print("playing .......")  
                playsound("song.mp3")
                break
