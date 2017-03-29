import discord
import asyncio
import time
from random import randint

client = discord.Client()
last_message_time = time.time();

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in')

@client.event
@asyncio.coroutine
def on_message(message):
    print('Saw message')
    if message.author != message.server.me:
        for there in theres:
            if there in message.content:
                print('ohshitwaddup')
                yield from client.send_message(message.channel, '*' + random.choice(theres), tts=True)
        for shit_word in shit_words:
            if shit_word in message.content.lower():
                print('Message contained nasty things')
                shit_list.append(message.author.nick)
                formatted_list = ["{0}\n".format(member) for member in shit_list]
                yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(nice_words), tts=True)
                yield from client.send_message(message.channel, str.join("", formatted_list))       
        if (time.time() - last_message_time) > randit(10800,65628): 
            yield from client.send_message(message.channel, random.choice(daily_grilling), tts=True)
    last_message_time = time.time();
        yield from client.add_reaction(message, random.choice(emojis))
        
    #checks if the user has asked the bot a question, then give a random response from response list    
    if question_words message.content.lower():
        yield from client.send_message(message.channel, random.choice(question_responses), tts=True)
        
client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
