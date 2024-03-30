#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
from urllib import request
import colorama
import signal
import os
import json
import re

def clear_screen():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear_screen()

colorama.init()

def Header():
    print(colorama.Fore.RED+"""
\033[1;31m
$$$$$$\ $$$$$$$\   $$$$$$\                               
\_$$  _|$$  __$$\ $$  __$$\                              
  $$ |  $$ |  $$ |$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  
  $$ |  $$$$$$$  |\$$$$$$\  $$  _____|\____$$\ $$  __$$\ 
  $$ |  $$  ____/  \____$$\ $$ /      $$$$$$$ |$$ |  $$ |
  $$ |  $$ |      $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |
$$$$$$\ $$ |      \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |
\______|\__|       \______/  \_______|\_______|\__|  \__|
                                        \033[1;39mDeveloper by DxeiZ\033[1;31m
""".center(shutil.get_terminal_size().columns))

Header()

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.2f%s' % (num, ['', ' Bin', ' Milyon', ' Milyar', ' Trilyon', 'Katrilyon'][magnitude])

def exit_code(sig, frame):
  print("\n"+colorama.Fore.LIGHTRED_EX + "Uygulama Kapatılıyor...")
  exit()

signal.signal(signal.SIGINT, exit_code)

while True:
    print(colorama.Style.RESET_ALL)
    ip = input(colorama.Fore.GREEN + "[+] " + colorama.Fore.LIGHTRED_EX + "IP Adresini Girin "+colorama.Style.RESET_ALL+"> ")

    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    p = re.compile(regex)

    if (re.search(p, ip)):
        url = 'https://ipapi.co/' + ip + '/json/'
        req = request.Request(url)
        response = request.urlopen(req)
        result = json.loads(response.read().decode("utf-8"))

        if len(result) == 5:
            print(colorama.Fore.RED+f"\n\033[1;3mHATA: {str(result['reason'])}\033[0m\n"+
                colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· IP · {colorama.Fore.LIGHTGREEN_EX+str(result['ip'])}\n"+
                colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Tür · {colorama.Fore.LIGHTGREEN_EX+str(result['version'])}")

        else:
            populatioNum = human_format(result['country_population'])
            countyDts = f"{str(result['country_name'])}, {str(result['region'])}, {str(result['city'])} ({str(result['country'])})"
            network = f"{str(result['ip'])} ({str(result['network'])})"
            print(colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m⤚IP⤍  {colorama.Fore.LIGHTGREEN_EX+network}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m⤚Ülke⤍  {colorama.Fore.LIGHTGREEN_EX+countyDts}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m    ⤿ Nüfus · {colorama.Fore.LIGHTGREEN_EX+populatioNum}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m    ⤿ Telefon · {colorama.Fore.LIGHTGREEN_EX+str(result['country_calling_code'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m    ⤿ Tld · {colorama.Fore.LIGHTGREEN_EX+str(result['country_tld'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m    ⤿ Asn · {colorama.Fore.LIGHTGREEN_EX+str(result['asn'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m    ⤿ Org · {colorama.Fore.LIGHTGREEN_EX+str(result['org'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m⤚Zaman Dilimi⤍  {colorama.Fore.LIGHTGREEN_EX+str(result['timezone'])} ({colorama.Fore.LIGHTGREEN_EX+str(result['utc_offset'])})\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m⤚Para Birimi⤍  {colorama.Fore.LIGHTGREEN_EX+str(result['currency_name'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m⤚Posta⤍  {colorama.Fore.LIGHTGREEN_EX+str(result['postal'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m⤚Konum⤍  {colorama.Fore.LIGHTGREEN_EX+'https://google.com/maps/place/'+str(result['latitude'])},{str(result['longitude'])} ({str(result['latitude'])},{str(result['longitude'])})")

    else:
        print(colorama.Fore.GREEN + "[-] " + colorama.Fore.RED + "IP Adresi Yanlış!")
