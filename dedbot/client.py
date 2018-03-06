#Author: Deddryk

import discord
import asyncio
import re
import getpass
import argparse

SPAM_TEXT = '''The big brown dog jumped over the small cat'''
client = discord.Client()
spam = {}
spam_from_file = False
spam_file = None
auto_catch = True
reactions = True

async def do_spam(channel):
    g = next_spam_line()
    while(True):
        text = next(g)
        if (spam[channel]):
            await client.send_message(channel, text)
            await asyncio.sleep(1.5)
        else:
            return

def next_spam_line():
    if spam_from_file:
        g = next_spam_line_file()
        while(True):
            yield next(next_spam_line_file())
    else:
        while True:
            yield SPAM_TEXT

def next_spam_line_file():
    global spam_file
    while True:
        while(spam_file):
            text = spam_file.readline()
            if text != "\n" and text != '':
                yield text
            if text == '':
                spam_file.seek(0)


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
    global reactions
    if message.author.id == '365975655608745985':
        if message.embeds != []:
            def is_congrats_message(message):
                if message.content.re.search('Congra') and message.content.re.search(str(client.user.id)):
                    caught = True
                else:
                    caught = False
            if 'title' in message.embeds[0].keys() and message.embeds[0]['title'].startswith("A wild po"):
                embed = message.embeds[0]
                if 'image' in embed.keys() and auto_catch:
                    pokemon = re.search('[0-9]{3}(.+?)(-.+)?\.png', embed['image']['url']).group(1)
                    await client.send_message(message.channel, 'p!catch ' + pokemon)
                    print("Trying to catch " + pokemon)
            if 'title' in message.embeds[0].keys() and caught:
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
        elif message.content.startswith('!react'):
             reactions = not reactions
        elif message.content.startswith('!everyone'):
            m = ""
            for i in get_server_members(message.server):
                m += i
            await client.send_message(message.channel, m) 


#To be omitted
        elif reactions and message.channel.id == '255851788870090754':
            await client.add_reaction(message, "\U0001F1ED")
            await client.add_reaction(message, "\U0001F1F4")
            await client.add_reaction(message, "\U0001F1F5")
            await client.add_reaction(message, "\U0001F1EA")
            await client.add_reaction(message, "\u23E9")
            await client.add_reaction(message, "\U0001F1F0")
            await client.add_reaction(message, "\U0001F0CF")
            await client.add_reaction(message, "\U0001F1FB")
            await client.add_reaction(message, "\U0001F1EE")
            await client.add_reaction(message, "\U0001F1F3")
#


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        print('Your secret is safe with me')
    else:
        await client.send_message(message.channel, '{0} deleted message: {1}'.format(message.author, message.content))
        #insert gotcha into the sent message via reactions


def main(_spam_file=None):
    global spam_from_file
    global spam_file
    if _spam_file == None:
        spam_from_file = False
    else:
        spam_from_file = True
        spam_file = _spam_file
    user_email = input("Email: ")
    user_pw = getpass.getpass()
    client.run(user_email, user_pw)

#gotcha in reactions
#            await client.add_reaction(message, "\U0001F1EC")
#            await client.add_reaction(message, "\U0001F1F4")
#            await client.add_reaction(message, "\U0001F1F9")
#            await client.add_reaction(message, "\U0001F1E8")
#            await client.add_reaction(message, "\U0001F1ED")
#            await client.add_reaction(message, "\U0001F1E6")
