# -*- coding: UTF-8 -*-

#Created by Martin Kodada, 19. 08. 2019

#Used frameworks + var for request

import requests
from bs4 import BeautifulSoup
import time
import re
import os

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
    with open("next_hour.txt", 'w') as f:
        for bus_arrival in buses_arrival:
            
        
            
            text = re.sub(r'[^\S\ ]',"",bus_arrival.text) #funguje
            pattern= r"(\d{3})"
            
            

            #text = re.match(pattern,bus_arrival.text)
            
               
            if "+" in text:
                position_plus = text.find("+") 
                text = text[0:3] + " " + text[3:position_plus-6] + " " + text[position_plus-6] + " " + text[position_plus-5:position_plus]+ " " + text[position_plus:len(text)-1]
            #format = cislo busu+ End Station + Station + arrival + Late minutes
            else:
                text = text[0:3] + " " + text[3:len(text)-7] + " " + text[len(text)-7] + " " + text[len(text)-6:len(text)-1]
            #format = bus_number + End Station + Station + "" + arrival

            
            f.write(text + "\n")


if __name__ == '__main__':
    Loop_Ticket_number()


