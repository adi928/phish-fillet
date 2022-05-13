#!/usr/bin/python3

import os
from sys import exit



try:
    import requests
    import argparse
    from urllib.parse import urlparse
    import re
    from progress.bar import IncrementalBar
    from bs4 import BeautifulSoup
    from ip2geotools.databases.noncommercial import DbIpCity

except ModuleNotFoundError as e:
    print("\n[-] Error: {}".format(e))
    print("[-] You are missing a required dependency.")
    answer = input("\n[?] Do you wish to install the missing dependency? (y/n): ")
    answer = answer.lower().strip()
    if answer in ["yes", "y"]:
        print("[!] Using pip3 to install module")
        os.system("pip3 install -r ../requirements.txt")
    else:
        print("[!] Please use pip3 to install module")

except KeyboardInterrupt:
        print("[!] Goodbye!")
        exit()

from filletFun.filletClass import  *
from filletFun.filletFun import  *


