import discord
import asyncio
import random
from words import search, vocabulary

client = discord.Client()
shit_list = []

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author != message.server.me:
        for wordlist in search:
            for word in wordlist:
                if word in message.content.lower():
                    if wordlist is 'theres':
                        yield from client.send_message(message.channel, '*' + random.choice(search['theres']), tts=True)
                    if wordlist is 'shit':
                        shit_list.append(message.author.nick)
                        formatted_list = ["{0} x{1}\n".format(member,shit_list.count(member)) for member in set(shit_list)]
                        yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(vocabulary['nice']) + ' ' + random.choice(vocabulary['friend']), tts=True)
                        yield from client.send_message(message.channel, str.join("", formatted_list), tts=True)
        if message.server.me.nick.lower() in message.content.lower():
                yield from client.send_message(message.channel,'fuk u')
        yield from client.add_reaction(message, random.choice(vocabulary['emojis']))

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
