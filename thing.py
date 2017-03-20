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
    print('saw message')
    for emoji in emojis:
        yield from client.add_reaction(message,emoji)
        yield from client.clear_reactions(message)
    if any(shit_words) in message:
         client.send_message(message.channel, 'you have entered the shit list.', tts=True)



client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
