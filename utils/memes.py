import time
import random
import requests
import json


def meme():
	memeget = requests.get('https://meme-api.herokuapp.com/gimme')
	memeSent = memeget.json()['url']
	memeMsg = '' + memeSent
	return memeMsg