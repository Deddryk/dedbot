#Author: Deddryk

import discord
import asyncio
import re
import getpass
import argparse

from dedbot.spammer import Spammer
from dedbot.pokemon import PokeCatcher

SPAM_TEXT = '''The big brown dog jumped over the small cat'''
client = discord.Client()
spam = {}
spam_from_file = False
spam_file = None
textfile = 'files/what_to_catch.txt'
spammer = None
message_listeners = []
reactions = True

async def do_spam(channel):
    while(True):
        if (spam[channel]):
            await client.send_message(channel, next(spammer))
            await asyncio.sleep(6)
        else:
            return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    with open(textfile) as pokemon_catch:
        catch_list = pokemon_catch.readlines()

def get_server_members(server):
    return [member.mention for member in server.members]

def add_message_listener(function):
    message_listeners.append(function)

def del_message_listener(function):
    message_listeners.remove(function)

@client.event
async def on_message(message):
    if message.author == client.user or message.author.id == '237019959287480320':
    for func in message_listeners:
        await func(message)
    if message.author == client.user:
        if message.content.startswith('!spam'):
            if message.channel in spam.keys():
                spam[message.channel] = not spam[message.channel]
            else:
                spam[message.channel] = True
            await do_spam(message.channel)
        elif message.content.startswith('!catch'):
            pokecatcher.toggle_autocatch(message.channel)
        elif message.content.startswith('!everyone'):
            m = ""
            for i in get_server_members(message.server):
                m += i
            await client.send_message(message.channel, m)

#@client.event
#async def on_message_delete(message):
#    await client.send_message(message.channel, '{0} deleted message: {1}'.format(message.author, message.content))

def main(_spam_file=None):
    global spam_from_file
    global spam_file
    global spammer
    global pokecatcher
    global client
    spammer = Spammer(_spam_file)
    pokecatcher = PokeCatcher(client)
    add_message_listener(pokecatcher.on_message)
    user_email = input("email: ")
    user_pw = getpass.getpass()
    client.run(user_email, user_pw)

