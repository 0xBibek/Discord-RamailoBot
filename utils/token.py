#####
#### Author: Bibek 
#### Github: 0xBibek
#####
import time
import random
import secrets
import requests
import json
import string


def tokenGen():
	ranToken = secrets.token_hex(32)
	tokenn = 'Random Token::\n' + ranToken
	return tokenn