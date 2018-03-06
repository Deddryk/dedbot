#!/usr/bin/python3

import sys
import argparse
import logging

import discord

<<<<<<< HEAD
@client.event
async def on_message(message):
    global auto_catch
    if message.author.id == '365975655608745985':
        if message.embeds != []:
            if 'title' in message.embeds[0].keys() and message.embeds[0]['title'].startswith("A wild po"):
                embed = message.embeds[0]
                if 'image' in embed.keys() and auto_catch:
                    pokemon = re.search('[0-9]{3}(.+?)(-.+)?\.png', embed['image']['url']).group(1)
                    await client.send_message(message.channel, 'p!catch ' + pokemon)
                    print("Trying to catch " + pokemon)
            if 'title' in message.embeds[0].keys() and message.embeds[0]['title'].find("Congrat" + str(client.user.id)):
                    pokemon = re.search('[0-9]{3}(.+?)(-.+)?\.png', embed['image']['url']).group(1)
                    print("You caught " + pokemon)
    if message.author == client.user:
        if message.content.startswith('!spam'):
                if message.channel in spam.keys():
                    spam[message.channel] = not spam[message.channel]
                else:
                    spam[message.channel] = True
                await do_spam(message.channel);
        elif message.content.startswith('!catch'):
            auto_catch = not auto_catch
        elif re.search('deleted message', message.content):
             await client.add_reaction(message, '\U0001F61E')



@client.event
async def on_message_delete(message):
    await client.send_message(message.channel, '{0} deleted message: {1}'.format(message.author, message.content))
=======
from dedbot import client

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
>>>>>>> develop

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=open, help="Text file to read spam from")
args = parser.parse_args()
if args.file:
    client.main(args.file)
else:
    client.main()

