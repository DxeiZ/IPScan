#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
from urllib import request
import colorama
import json
import re

print(chr(27) + "[2J")

colorama.init()


def Header():
    print(colorama.Fore.RED + "\033[1;3mシ-ド ＩＰＳｃａｎ　シ-ド\033[0m".center(shutil.get_terminal_size().columns))
    print("\033[1;3mEratOS\033[0m".center(shutil.get_terminal_size().columns))


Header()

print(colorama.Style.RESET_ALL)
print(colorama.Fore.GREEN + "[+] " + colorama.Fore.LIGHTRED_EX + "IP Adresini Daxil Edin ↓")
ip = input("> ")

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
p = re.compile(regex)

if (re.search(p, ip)):
    url = 'https://ipapi.co/' + ip + '/json/'
    req = request.Request(url)
    response = request.urlopen(req)
    result = json.loads(response.read().decode("utf-8"))

    if len(result) == 5:
        print(f"\nIP · {result['ip']}\n"
              f"Type · {result['version']}\n"
              + colorama.Fore.RED + f"\n\033[1;3mError: {result['reason']}\033[0m")

    else:
        print(f"\nIP · {result['ip']}\n"
              f"Network · {result['network']}\n"
              f"Type · {result['version']}\n"
              f"Country · {result['country_name']}\n"
              f"Country Code · {result['country']}\n"
              f"Country Phone · {result['country_calling_code']}\n"
              f"Country Tld · {result['country_tld']}\n"
              f"Region · {result['region']}\n"
              f"City · {result['city']}\n"
              f"Asn · {result['asn']}\n"
              f"Org · {result['org']}\n"
              f"Timezone · {result['timezone']} ({result['utc_offset']})\n"
              f"Currency ·  {result['currency_name']}\n"
              f"Country Population · {result['country_population']}\n"
              f"Languages · {result['languages']}\n"
              f"Postal · {result['postal']}\n"
              f"Location · https://google.com/maps/place/{result['latitude']},{result['longitude']} ({result['latitude']},{result['longitude']})")

else:
    print(colorama.Fore.GREEN + "[-] " + colorama.Fore.RED + "IP Adresini Yanlisdir!")
