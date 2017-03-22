import discord
import asyncio
import random
from time import sleep

client = discord.Client()

shit_words = ['jacob',',maths','learning','dynamics']
emojis = ['🤓','🕍','🤗','🤑','😒','🤓','😤','🤡','🤥','👿','💀','👻','👽','👾','💩','☠','👶','🎅','👲','🙍','🚶']

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in')

@client.event
@asyncio.coroutine
def on_message(message):
    if message.content in shit_words:
        yield from client.send_message(message.channel, 'you have entered the shit list.', tts=True)
    displayed_emojis = []
    while True is True:
        if len(message.reactions) < 20:
            emoji = random.choice(emojis)
            displayed_emojis.insert(0,emoji)
            yield from client.add_reaction(message,emoji)
        else:
            emoji = displayed_emojis.pop()
            yield from client.remove_reaction(1message,emoji,client.user)
            emoji = random.choice(emojis)
            displayed_emojis.insert(0,emoji)
            yield from client.add_reaction(message,emoji)
        sleep(2000)

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
