# bus-departure-screen-Prague
Build based on Python that scraps PID for bus arrivals and uses raspberry pi zero + OLED display to show them.

1st step is to scrap and paste the bus arrivals. The scrapped input is part of the script.

The three digits are bus number, following word sequence is the end station for this bus (which shows the direction in which it goes), the one letter stands for the correct place of arrival (based on direction, A is one direction, B is the oposite, other letter are used if station is slipped into more stations (for example, Sídliště Malešice has 4 stations or Strossmayerovo náměstí has A,B,D,E,F), the following time stemp is expected arrival/departure and the ? (signaling the unknown delay from ideal time) ends this input. If the bus is known to be late, the input can have + 1/ + 10 at its end.

Parsing is currently based on the exact position, which is not ideal solution (regex is way better). The current script saves parsed bus info into 2D array that is later processed in the PID-body.py

PID Body.py runs the script "Loop_Ticket_number()" from PID.py and gets 2D array with 30 arrivals. Then it checks if the time of arrival is same or less than the machine time (thus getting us the closes arrival). If the function detects that the check is false, it shortens the list for 1 arrival.

The current steps that should be taken are to add "display" of the 3 closes arrivals and creating an image for the OLED display. 
