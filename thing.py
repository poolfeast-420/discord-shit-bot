import discord
import asyncio
import random
from time import sleep

client = discord.Client()

nice_words = ['pal','buddy','friendo','mate','chum','associate']
shit_words = ['jacob','math','learning','dynamics','convolution','study','meme']
emojis = ['🤓','🕍','🛂','⛳','🤗','🈶','🤑','😒','🤓','😤','🤡','🤥','👿','💀','👻','👽','👾','💩','☠','👶','🎅','👲','🙍','🚶','🙃']
shit_list = []

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in')

@client.event
@asyncio.coroutine
def on_message(message):
    print('Saw message')
    for shit_word in shit_words:
        if shit_word in message.content:
            print('Message contained nasty things')
            shit_list.append(message.author)
            yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(nice_words), tts=True)
            yield from client.send_message(message.channel, 'the shit list contains ' + str(shit_list))
    yield from client.add_reaction(message, random.choice(emojis))

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
