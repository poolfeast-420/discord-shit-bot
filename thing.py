import discord
import asyncio
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
    for emoji in emojis:
        yield from client.add_reaction(message,emoji)
        yield from client.remove_reaction(message,emoji,client.user)

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
