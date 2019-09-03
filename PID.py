# -*- coding: UTF-8 -*-

#Created by Martin Kodada, 19. 08. 2019

#Used frameworks + var for request

import requests
from bs4 import BeautifulSoup
import re


#Set the bus station from pid.cz/zastavkova-tabla/
URL = 'https://pid.cz/zastavkova-tabla/?stop=Sidli%C5%A1t%C4%9B+Male%C5%A1ice&stanoviste=&tab=1'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}



def Loop_Ticket_number():
    
    #GETs content from PID, Parses it and creates next_hour.txt where all buses are nicely parsed (it is always next 30 buses for the station)
    
    page = requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    buses_arrival = soup.findAll("tr", {"class": "more-info-init"})
    
# Input example for parsing
#
#
#199
#
#
#				Sídliště Malešice			
#
#A
#			
#
#
#
#19:04
#
#?
#
#
#
#
    bus_arrives =[]
    index = 0
    for bus_arrival in buses_arrival: 
            
        text = re.sub(r'[^\S\ ]',"",bus_arrival.text)
        bus_list = []
        if "+" in text:
            position_plus = text.find("+")
            bus_number = text[0:3]
            bus_direction =  text[3:position_plus-6]
            bus_station = text[position_plus-6]
            bus_arrive = text[position_plus-5:position_plus]
            bus_late = text[position_plus:len(text)-1]
            bus_info = [bus_arrive,bus_number,bus_direction,bus_station,bus_late]
            bus_arrives.append(bus_info)
            index = index + 1
            
#test on 31/08/2019 showed that when the bus is cancelled, the delay is replaced with word "NEJEDE"
#This function replaces the possible bus info with string -1 (to not bother with it in PID Body
        elif "NEJEDE" in text:
             bus_info = ["-1"]   
             bus_arrives.append(bus_info)

        else:
            bus_number = text[0:3]
            bus_direction =  text[3:len(text)-7]
            bus_station = text[len(text)-7]
            bus_arrive = text[len(text)-6:len(text)-1]
            bus_late = 0
            bus_info = [bus_arrive,bus_number,bus_direction,bus_station,bus_late]
            bus_arrives.append(bus_info)
            index = index + 1
    return bus_arrives
# returns list of lists [21:42, 225,Vypich,A,0]

if __name__ == '__main__':
    Loop_Ticket_number()


