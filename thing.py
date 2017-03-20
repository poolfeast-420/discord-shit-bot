import discord
import asyncio
client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
@asyncio.coroutine
def on_message(message):
    print('saw message')
    yield from client.add_reaction(message,'\U0001F4A9')

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
