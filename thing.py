import discord
import asyncio
import random
import datetime
from words import search, vocabulary

client = discord.Client()
shit_list = []

@client.event
@asyncio.coroutine
def on_message(message):
    shitdetector = False;
    if message.author != message.server.me:
        if message.server.me.nick.lower() in message.content.lower():
                yield from client.send_message(message.channel, random.choice(vocabulary['angry']), tts=True)
        if 'bee' in message.content.lower():
            comment = vocabulary['bee']
            for split_message in [comment[character:character+2000] for character in range(0, len(comment), 2000)]:
                yield from client.send_message(message.channel, split_message)
        if 'tuesday' in message.content.lower():
            yield from client.send_message(message.channel, 'Existence is pain', tts=True)
        if str(int(datetime.datetime.now().minute)) + 'clear' in message.content.lower():
            yield from client.purge_from(message.channel, before=datetime.datetime.now() - datetime.timedelta(minutes=15), limit=100, check=lambda message:message.author == client.user)
        for wordlist_name, words in search.items():
            for word in words:
                if word in message.content.lower():
                    if wordlist_name in ['toos','yours','theres']:
                        yield from client.send_message(message.channel, '*' + random.choice(vocabulary[wordlist_name]), tts=True)
                    if wordlist_name is 'shit':
                        shit_list.append(message.author.nick)
                        formatted_list = ["{0} x{1}\n".format(member,shit_list.count(member)) for member in set(shit_list)]
                        yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(vocabulary['nice']) + ' ' + random.choice(vocabulary['friend']), tts=True)
                        yield from client.send_message(message.channel, str.join("", formatted_list), tts=True)
                        yield from client.add_reaction(message, '💩')
                        shitdetector = True;
                    if wordlist_name in ['hitler','ussr']:
                        for phrase in vocabulary[wordlist_name]:
                            yield from client.send_message(message.channel, phrase, tts=True)
                    if wordlist_name is 'learning':
                        yield from client.send_message(message.channel,'learnding iz fun', tts=True)
                    if wordlist_name is 'friend':
                        yield from client.send_message(message.channel,"i ain't your " + word + ', ' + random.choice(vocabulary['friend']), tts=True)
        if shitdetector is False:
            yield from client.add_reaction(message, random.choice(vocabulary['emojis']))

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
