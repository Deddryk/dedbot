#!/usr/bin/python3

import sys
import argparse
import logging

import discord

from dedbot import client

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=open, help="Text file to read spam from")
args = parser.parse_args()
if args.file:
    client.main(args.file)
else:
    client.main()

