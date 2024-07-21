# -*- coding: UTF-8 -*-

#Created by Martin Kodada, 19. 08. 2019

#Used frameworks + var for request

import asyncio
from pyppeteer.launcher import launch
from bs4 import BeautifulSoup

URL = 'https://pid.cz/zastavkova-tabla/?stop=Sidli%C5%A1t%C4%9B+Male%C5%A1ice&stanoviste=&tab=1'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}


async def pyppetet(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.waitFor(7000)
    ## Get HTML
    html = await page.content()
    await browser.close()
    return html

    
#Set the bus station from pid.cz/zastavkova-tabla/


def Loop_Ticket_number():
    html_response = asyncio.get_event_loop().run_until_complete(pyppetet(URL))
    soup = BeautifulSoup(html_response, "html.parser")
    line = soup.find_all("div", class_="box-subject-subtitle box-cnt-column is-begin")
    end = soup.find_all("div", class_="box-cnt-column is-end")
    arrival = soup.find_all("span", class_="view-time")
    delay = soup.find_all("span", class_="view-delay")
    print(line[0].text.strip(), end[0].text.strip(), arrival[0].text.strip(), delay[0].text.strip())

if __name__ == '__main__':
    Loop_Ticket_number()


