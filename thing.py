import discord
import asyncio
import random

client = discord.Client()

nice_words = ['pal','buddy','friendo','mate','chum','associate','amigo','hombre','compadre','comrade','signore','homeboy','partner','my main man','bosom pal',]
shit_words = ['jacob','math','learning','dynamics','convolution','study','meme','bot','shit','#','richard','throat','laplace']
emojis = ['🤓','🕍','🛂','⛳','🤗','🈶','🤑','😒','🤓','😤','🤡','🤥','👿','💀','👻','👽','👾','💩','☠','👶','🎅','👲','🙍','🚶','🙃']
shit_list = []
theres = ['their','theyre','they are','there','theire','thier',"they're",'theirie','bear']

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
                yield from client.send_message(message.channel, str.join("", formatted_list), tts=True)
        yield from client.add_reaction(message, random.choice(emojis))

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
