# bus-departure-screen-Prague
Build based on Python that scraps PID for bus arrivals and uses raspberry pi zero + OLED display to show them.

1st step is to scrap and paste the bus arrivals. The scrapped input is part of the script.

The three digits are bus number, following word sequence is the end station for this bus (which shows the direction in which it goes), the one letter stands for the correct place of arrival (based on direction, A is one direction, B is the oposite, other letter are used if station is slipped into more stations (example, Sídliště Malešice is 4 stations or Strossmayerovo náměstí has A,B,D,E,F), the following time stemp is expected arrival/departure and the ? ends this input. If the bus is known to be late, the input can have + 1/ + 10 at its end.

Parsing is currently based on the exact position, which is not ideal solution (regex is way better). The current script saves parsed bus info into text file (will change). 

2nd step is to build an algorytm, that will run PID.py function, gets 30 responses, starts to list them on the OLED and then loop itself. 
