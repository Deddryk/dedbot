#Author: Deddryk

import discord
import asyncio
import re
import getpass
import argparse

from dedbot.spammer import Spammer

SPAM_TEXT = '''The big brown dog jumped over the small cat'''
client = discord.Client()
spam = {}
spam_from_file = False
spam_file = None
auto_catch = False
spammer = None

async def do_spam(channel):
    while(True):
        if (spam[channel]):
            await client.send_message(channel, next(spammer))
            await asyncio.sleep(1.5)
        else:
            return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def get_server_members(server):
    return [member.mention for member in server.members]

@client.event
async def on_message(message):
    global auto_catch
    if message.author.id == '365975655608745985':
        if message.embeds != []:
            if 'title' in message.embeds[0].keys() and message.embeds[0]['title'].startswith("A wild po"):
                embed = message.embeds[0]
                pokemon = re.search('[0-9]{3}(.+?)(-.+)?\.png', embed['image']['url']).group(1)
                if 'image' in embed.keys() and auto_catch and server.id == '418975946394173442':
                    await client.send_message(message.channel, 'p!catch ' + pokemon)
                    print("Trying to catch " + pokemon)
    if message.author == client.user:
        if message.content.startswith('!spam'):
                if message.channel in spam.keys():
                    spam[message.channel] = not spam[message.channel]
                else:
                    spam[message.channel] = True
                await do_spam(message.channel);
        elif message.content.startswith('!catch'):
            auto_catch = not auto_catch
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
    spammer = Spammer(_spam_file)
    user_email = input("email: ")
    user_pw = getpass.getpass()
    client.run(user_email, user_pw)


