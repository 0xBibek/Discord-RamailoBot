#####
#### Author: Bibek 
#### Github: 0xBibek
#####
import discord
import os
import time
import sys
import string
import pause
import json
from config import BOT_TOKEN
import utils.td as timee
import utils.quotes as quoteG
import utils.memes as memeG

client = discord.Client()
TOKEN = BOT_TOKEN

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == "?td":
    td = timee.td()
    await message.channel.send(td)

  if message.content == "?quote":
    quote = quoteG.quoteGen()
    await message.channel.send(quote)

  if message.content == "?meme":
    meme = memeG.meme()
    await message.channel.send(meme)


  if message.content == "?help":
    embed = discord.Embed(title=" [ Help ] ", description="Commands list")
    embed.add_field(name="?meme", value="Random Meme")
    embed.add_field(name="?quote", value="Random quotes")
    await message.channel.send(content=None, embed=embed)


client.run(TOKEN)