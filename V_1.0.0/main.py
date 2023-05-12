import pyautogui as pgui
import random as rd
import subprocess
import time

#CREATE URL TO INCLUDE BING BROWSER.
def urlbuilder():
    values = rd.randint(0,4545454)
    url = "https://www.bing.com/search?q="+str(values)
    return url


def ReEntry():
        with pgui.hold('ctrl'):
            pgui.press('e')
        input = urlbuilder()
        for x in input:
            pgui.press(x)
        pgui.press('enter')


def RequestGenerator(default_entry = 30):
    subprocess.Popen('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    #SLEEP FOR 3 SECONDS BEFORE PROCESSING REQUESTS
    time.sleep(3)
    input = urlbuilder()
    for x in input:
        pgui.press(x)
    pgui.press('enter')
    if default_entry > 1:
        for x in range(default_entry-1):
            ReEntry()
    
req_count = input("Enter number of Requests to generate default is 30 : ")
if req_count.isdigit()==False:
    RequestGenerator()
else:
    RequestGenerator(int(req_count))
    