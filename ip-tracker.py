import requests

import os

from time import sleep

from colorama import Fore

#@JuniorProgrammerboy

os.system('clear')


print(Fore.CYAN+PROGRAMMER)

print(Fore.YELLOW+"Author:Yousuf Shafi'i Muhammad",Fore.LIGHTYELLOW_EX+"                                          Version:1.7")                                                                           

print(Fore.BLUE+"Contact me on Telegram:https://t.me/Juniorprogrammerboy")

print(Fore.BLUE+"Telegram Channel:https://t.me/Learn700programminglanguages\n")                                                                            

print(Fore.RED+"legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

def Find():

    while True:

        IP=input(Fore.WHITE+"Enter Your Target IP: ")

        nayak = requests.get("http://ip-api.com/json/"+IP).json()

        print("\n")

        print(Fore.CYAN+"GET INFORMATION")

        print(Fore.BLUE+"[+]Target IP: "+nayak['query'])

        print("[+]Status: "+nayak['status'])

        print("[+]Country: "+nayak['country'])

        print("[+]Country Code: "+nayak['countryCode'])

        print("[+]Region: "+nayak['region'])

        print("[+]State: "+nayak['regionName'])

        print("[+]City: "+nayak['city'])

        print("[+]Lat And Lon",nayak['lat'],nayak['lon'])

        print("[+]TimeZone: "+nayak['timezone'])

        print("[+]ISP: "+nayak['isp'])

        print("[+]Industries: "+nayak['as'])

        sleep(3)

        Me()         

def Me():

        S = input(str(Fore.RED+"\nLet's Do Next IP Information Gathering[Y/n]: "))

        if S == 'y' or S == 'Y':

            print(Fore.GREEN+PROGRAMMER)

            Find()

        elif S == 'N' or S == 'n':

            os.system('clear')

            print(Fore.LIGHTGREEN_EX+"Exiting")

            sleep(1)

            print(Fore.RED+banner)

            print(Fore.CYAN+"Thank's For Using TEAM JUNIOR PROGRAMMERS Tool")

            print(Fore.YELLOW+"Author: Junior Programmer Boy")

            exit()                

        else:

            print(Fore.RED+"\nEnter Right Option   [Invalid Option!!!]")

            Me()

Find()
