import asyncio
import re

import discord

POKECORD_ID = '365975655608745985'
POKEMON_REGEX = '[0-9]{3}([A-Z][a-z]+)(-.+)?\.png(/\.*)?'

class PokeCatcher():

    def __init__(self, client, catch_list=[]):
        self.channels = {}
        self.client = client
        self.catch_list = catch_list
        self.catch_all = not self.catch_list

    def message_matters(self, message):
        return message.author.id == POKECORD_ID and message.channel in self.channels

    def is_wild_pokemon(message):
        if not message.embeds:
            return False
        embed = message.embeds[0]
        if 'title' in embed.keys() and embed['title'].startswith("A wild po"):
            return True
        
    def get_wild_pokemon(message):
        url = message.embeds[0]['image']['url']
        return re.search(POKEMON_REGEX, url).group(1)

    async def on_message(self, message):
        self.is_caught(message)
        if self.message_matters(message) and PokeCatcher.is_wild_pokemon(message) and (self.catch_all or PokeCatcher.get_wild_pokemon(message) in self.catch_list or PokeCatcher.get_wild_pokemon(message) not in 'files/what_has_been_caught.txt'):
            if self.channels[message.channel]:
                await self.client.send_message(message.channel, 'p!catch ' + PokeCatcher.get_wild_pokemon(message))
                if PokeCatcher.get_wild_pokemon(message) in self.catch_list:
                    with open('files/spotted_filteimport asyncio
2
import re
3
​
4
import discord
5
​
6
POKECORD_ID = '365975655608745985'
7
POKEMON_REGEX = '[0-9]{3}([A-Z][a-z]+)(-.+)?\.png(/\.*)?'
8
​
9
class PokeCatcher():
10
​
11
    def __init__(self, client, catch_list=[]):
12
        self.channels = {}
13
        self.client = client
14
        self.catch_list = catch_list
15
        self.catch_all = not self.catch_list
16
​
17
    def message_matters(self, message):
18
        return message.author.id == POKECORD_ID and message.channel in self.channels
19
​
20
    def is_wild_pokemon(message):
21
        if not message.embeds:
22
            return False
23
        embed = message.embeds[0]
24
        if 'title' in embed.keys() and embed['title'].startswith("A wild po"):
25
            return True
26
        
27
    def get_wild_pokemon(message):
28
        url = message.embeds[0]['image']['url']
29
        return re.search(POKEMON_REGEX, url).group(1)
30
​
31
    async def on_message(self, message):
32
        if self.message_matters(message) and PokeCatcher.is_wild_pokemon(message) and (self.catch_all or PokeCatcher.get_wild_pokemon(message) in self.catch_list or PokeCatcher.get_wild_pokemon(message) not in 'files/what_has_been_caught.txt'):
33
            if self.channels[message.channel]:
34
                await self.client.send_message(message.channel, 'p!catch ' + PokeCatcher.get_wild_pokemon(message))
35
                if PokeCatcher.get_wild_pokemon(message) in self.catch_list:
36
                    with open('files/spotted_filter.txt', 'a' ) as spotted:
37
                        spotted.write('Spotted: ' + PokeCatcher.get_wild_pokemon(message) + '\n')
38
                with open('files/spotted_all.txt', 'a' ) as spotted:
39
                    spotted.write('Spotted: ' + PokeCatcher.get_wild_pokemon(message) + '\n')
40
​
41
    def toggle_autocatch(self, channel):
42
        if channel in self.channels.keys():
43
            self.channels[channel] = not self.channels[channel]
44
        else:
45
            self.channels[channel] = True
46
​
47
​
48
        
49
    def is_caught(message):
50
        if message.startswith('Congr') and client.user.mentioned_in(message):
51
             caught_pokemon = message.split()[-1].split('!')
52
             with open('files/what_has_been_caught.txt', 'a' ) as caught:
53
                 caught.write(str(caught_pokemon[0]) + '\n')
54
                 print('Pokemon Added To Caught List:     ' + str(caught_pokemon[0]))
55
r.txt', 'a' ) as spotted:
                        spotted.write('Spotted: ' + PokeCatcher.get_wild_pokemon(message) + '\n')
                with open('files/spotted_all.txt', 'a' ) as spotted:
                    spotted.write('Spotted: ' + PokeCatcher.get_wild_pokemon(message) + '\n')

    def toggle_autocatch(self, channel):
        if channel in self.channels.keys():
            self.channels[channel] = not self.channels[channel]
        else:
            self.channels[channel] = True


        
    def is_caught(self, message):
        if message.content.startswith('Congr') and self.client.user.mentioned_in(message):
             caught_pokemon = message.content.split()[-1].split('!')
             with open('files/what_has_been_caught.txt', 'a' ) as caught:
                 caught.write(str(caught_pokemon[0]) + '\n')
                 print('Pokemon Added To Caught List:     ' + str(caught_pokemon[0]))

