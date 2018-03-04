#!/usr/bin/python3

import sys
import argparse

from dedbot import client

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=open, help="Text file to read spam from")
args = parser.parse_args()
if args.file:
    client.main(args.file)
else:
    client.main()

