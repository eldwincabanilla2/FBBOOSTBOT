import requests
from fbchat import Client
from fbchat.models import *
import ua_generator
import re
from concurrent.futures import ThreadPoolExecutor
import os
import threading
import json
import sys
import time

try:
                with open('configuration.json') as f:
                    configuration = json.load(f)
except FileNotFoundError:
            print("\033[1m\033[91mSORRY, AN ERROR ENCOUNTERED WHILE FINDING 'CONFIGURATION.JSON'.\033[0m")
            sys.exit()
except json.decoder.JSONDecodeError:
            print("\033[1m\033[91mSORRY, AN ERROR ENCOUNTERED WHILE READING THE JSON FILE.\033[0m")
