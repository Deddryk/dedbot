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
        if self.message_matters(message) and PokeCatcher.is_wild_pokemon(message) and (self.catch_all or PokeCatcher.get_wild_pokemon(message) in self.catch_list or PokeCatcher.get_wild_pokemon(message) not in self.caught_file):
            if self.channels[message.channel]:
                await self.client.send_message(message.channel, 'p!catch ' + PokeCatcher.get_wild_pokemon(message))
                if PokeCatcher.get_wild_pokemon(message) in self.catch_list:
                    with open('files/spotted_filter.txt', 'a' ) as spotted:
                        spotted.write('Spotted: ' + PokeCatcher.get_wild_pokemon(message) + '\n')
                with open('files/spotted_all.txt', 'a' ) as spotted:
                    spotted.write('Spotted: ' + PokeCatcher.get_wild_pokemon(message) + '\n')

    def toggle_autocatch(self, channel):
        if channel in self.channels.keys():
            self.channels[channel] = not self.channels[channel]
        else:
            self.channels[channel] = True
            
         
        
    def is_caught(message):
        if message_matters(message) and client.user.name in message and 'aug' in message:
            hard_shit = message.split()
            caught_pokemon = hard_shit.split('1')
               with open(self.caught_file, 'a' ) as caught:
                   caught.write(caught_pokemon + '\n')
            
