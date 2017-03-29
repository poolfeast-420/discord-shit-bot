import discord
import asyncio
import random
from wordlist import


client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Ready')

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author != message.server.me:
        for there in theres:
            if there in message.content.lower():
                yield from client.send_message(message.channel, '*' + random.choice(theres), tts=True)
        if message.server.me.nick.lower() in message.content.lower():
                yield from client.send_message(message.channel,'fuk u')
        for shit_word in shit_words:
            if shit_word in message.content.lower():
                shit_list.append(message.author.nick)
                formatted_list = ["{0} x{1}\n".format(member,shit_list.count(member)) for member in set(shit_list)]
                yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(nice_words) + ' ' + random.choice(friend_words), tts=True)
                yield from client.send_message(message.channel, str.join("", formatted_list), tts=True)
        yield from client.add_reaction(message, random.choice(emojis))

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
