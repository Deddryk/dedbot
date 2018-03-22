import asyncio
import re
import logging

import discord

POKECORD_ID = '365975655608745985'
POKEMON_REGEX = '[0-9]{3}([A-Za-z_é]+)(-.+)?\.png(/\.*)?'
AUTOCATCH_LOG_MSG = "Auto catch is now {} in channel {}."
logger = logging.getLogger(__name__)

def is_wild_pokemon(message):
    if not message.embeds:
        return False
    embed = message.embeds[0]
    if 'title' in embed.keys() and embed['title'].startswith("A wild po"):
        return True

def get_wild_pokemon(message):
    url = message.embeds[0]['image']['url']
    return pokemon_from_url(url)

def pokemon_from_url(url):
    pokemon = ''
    try:
        pokemon = re.search(POKEMON_REGEX, url).group(1)
        pokemon = re.sub('_', ' ', pokemon)
    except:
        logger.error('Failed to get pokemon from {}'.format(url))
    return pokemon


def is_pokecord(message):
    return message.author.id == POKECORD_ID

class PokeCatcher():

    def __init__(self, client, catch_list=[]):
        self.channels = {}
        self.client = client
        self.catch_list = catch_list
        self.catch_all = not self.catch_list
        logger.info("Initializing PokeCatcher")

    def message_matters(self, message):
        return is_pokecord(message) and message.channel in self.channels

    async def catch(self, channel, pokemon):
        logger.info("Trying to catch pokemon {}.".format(pokemon))
        self.most_recent_try = pokemon.lower()
        await self.client.send_message(channel, 'p!catch ' + pokemon)

    async def on_message(self, message):
        if self.message_matters(message) and is_wild_pokemon(message) and (self.catch_all or PokeCatcher.get_wild_pokemon(message) in self.catch_list):
            if self.channels[message.channel]:
                await self.catch(message.channel, get_wild_pokemon(message))
        if is_pokecord(message) and self.client.user.mentioned_in(message):
            if message.content.startswith('Cong'):
                logger.debug(message.content)
                pokemon = re.search("You caught a (.+)!", message.content)
                logger.debug(repr(pokemon))
                pokemon = pokemon.group(1)
                logger.info("Caught a {}".format(pokemon))
                if pokemon.lower() != self.most_recent_try:
                    logger.error("Did not catch {}".format(self.most_recent_try))

    def toggle_autocatch(self, channel):
        if channel in self.channels.keys():
            self.channels[channel] = not self.channels[channel]
        else:
            self.channels[channel] = True
        enabled = self.channels[channel]
        server_str = channel.server.name
        channel_str = server_str + '.' + channel.name
        logger.info(AUTOCATCH_LOG_MSG.format("enabled" if enabled else "disabled", channel_str))

