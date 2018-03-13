import asyncio
import re

import discord

POKECORD_ID = '365975655608745985'
POKEMON_REGEX = '[0-9]{3}([A-Z][a-z]+)(-.+)?\.png(/\.*)?'

class PokeCatcher():

    def __init__(self, client):
        self.channels = {}
        self.client = client

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
        if self.message_matters(message) and PokeCatcher.is_wild_pokemon(message):
            if self.channels[message.channel]:
                await self.client.send_message(message.channel, 'p!catch ' + PokeCatcher.get_wild_pokemon(message))

    def toggle_autocatch(self, channel):
        if channel in self.channels.keys():
            self.channels[channel] = not self.channels[channel]
        else:
            self.channels[channel] = True
            
        
