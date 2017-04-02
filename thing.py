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
        yield from client.add_reaction(message, random.choice(vocabulary['emojis']))
        if message.server.me.nick.lower() in message.content.lower():
                yield from client.send_message(message.channel,(vocabulary['response_list']))
        for wordlist_name, words in search.items():
            for word in words:
                if word in message.content.lower():
                    if wordlist_name is 'theres':
                        yield from client.send_message(message.channel, '*' + random.choice(search['theres']), tts=True)
                    if wordlist_name is 'toos':
                        yield from client.send_message(message.channel, '*' + random.choice(search['toos']), tts=True)
                    if wordlist_name is 'shit':
                        shit_list.append(message.author.nick)
                        formatted_list = ["{0} x{1}\n".format(member,shit_list.count(member)) for member in set(shit_list)]
                        yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(vocabulary['nice']) + ' ' + random.choice(vocabulary['friend']), tts=True)
                        yield from client.send_message(message.channel, str.join("", formatted_list), tts=True)
                    if wordlist_name is 'learning':
                        yield from client.send_message(message.channel,'learnding iz fun', tts=True)
                    if wordlist_name is 'friend':
                        yield from client.send_message(message.channel,"i ain't your " + word + ', ' + random.choice(vocabulary['friend']), tts=True)
                    if wordlist_name is 'toos':
                        yield from client.send_message(message.channel,"*" + random.choice(vocabulary['toos']), tts=True)
                    if wordlist_name is 'yours':
                        yield from client.send_message(message.channel,"*" + random.choice(vocabulary['yours']), tts=True)

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
