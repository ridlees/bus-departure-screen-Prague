# -*- coding: UTF-8 -*-

#Created by Martin Kodada, 23. 08. 2019

import time
import datetime
from PID import Loop_Ticket_number

#TODO ADD kontrolu víc jak jednoho příjezdu (asi next three vždy, to by mohlo fungovat fajn)

#gets a new list of arrivals from website
def Arrivals():
    arrivals = Loop_Ticket_number()
    return arrivals

#main loop
def Loop(arrivals):
    now_time = datetime.datetime.now().time()
    now = int(str(now_time.hour) + str(now_time.minute))

    #tests if the first bus is still the next arrival
    
    if now <= int(arrivals[0][0].replace(":","")):
        print("Still first")
        print(arrivals[0][0])
        #send to OLED
    else:
        #if not, shortens the list. If there is only last bus info, gets a new list of arrivals 
        print("Not first anymore")
        print(arrivals[0][0])
        if len(arrivals) == 1:
            arrivals = Arrivals()
        else:
            arrivals = arrivals[1:len(arrivals)]
            print(arrivals)
        #send to OLED
        #Update picture
    time.sleep(10)
    Loop(arrivals)

if __name__ == '__main__':        
    arrivals = Arrivals()
    Loop(arrivals)
