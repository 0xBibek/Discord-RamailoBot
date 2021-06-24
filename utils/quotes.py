import time
import random
import secrets
import requests
import json
import string


def quoteGen():
	quote = requests.get('https://api.quotable.io/random')
	quoteContent = quote.json()['content']
	quoteAuthor = quote.json()['author']
	quoteMsg = '' + quoteContent + ' - ' + quoteAuthor
	return quoteMsg