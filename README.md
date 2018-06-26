# palbot
a simple discord bot

This fork is modified to fix deprecated APIs and to smooth out some issues with running it as a docker image.

This is effectively a discord version of [iamsix/genmaybot](https://github.com/iamsix/genmaybot)

In its current version it's still basically a standard IRC bot that works on discord - it needs some modification to work with discord-specific features.

It requires Python 3.6 due to cruft  
It makes use of [discord.py](https://github.com/Rapptz/discord.py)

You will need to set some config options (especially the token) using the example config.

To obtain the clues.db for trivia please use [jeopardy-parser](https://github.com/whymarrh/jeopardy-parser)
