dedbot
======

A discord bot that does fun stuff

Features
--------

* Pokemon catch

    Automatically catches pokemon in channels with the [Pokecord][pokecord] bot.  

    Toggle with `!catch`.
* Spam

    Spams messages in a given discord channel.  The main purpose of this is to make wild pokemon spawn 
    in channels with [Pokecord][pokecord] present but can obviously be used for other purposes.  Spam
    will only appear in the channel it is launched in but can be used across multiple channels.

    By default the spam text is a single string repeated infinitely, but if the bot is launched with 
    `-f <filename>` it reads lines from that text file and loops over it.

    Toggle with `!spam`
* !everyone
    
    Mentions everyone in a channel, even in channels where @everone is disabled

[pokecord]: https://discordbots.org/bot/365975655608745985

