import discord
import asyncio
import random

client = discord.Client() 

startTime = time.time();
endTime = startTime + 34980;
commentTime = time.time();

    
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
        yield from client.add_reaction(message, random.choice(emojis))
        
    #checks if the user has asked the bot a question, then give a random response from response list    
    if question_words && name_words in message.content.lower():
        yield from client.send_message(message.channel, random.choice(question_responses), tts=True)
    #picks a random time from within provided set, later get it to respond to next messager in chat                     
    if rand(startTime,EndTime) > (previous_comment - time.time()):
        yield from client.send_message(message.channel, random.choice(daily_grilling), tts=True)
        
client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
