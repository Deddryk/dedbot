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
auto_catch = False

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

def main():
    user_email = input("email: ")
    user_pw = getpass.getpass()
    client.run(user_email, user_pw)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=open, help="Text file to read spam from")
    args = parser.parse_args()
    if args.file:
        spam_file = args.file
        spam_from_file = True
    main()
