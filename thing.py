import discord
import asyncio
import random

client = discord.Client()

nice_words = ['pal','buddy','friendo','mate','chum','associate']
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
                shit_list.append(message.author.nick)
                formatted_list = ["{0} x{1}\n".format(member,shit_list.count(member)) for member in set(shit_list)]
                yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(nice_words), tts=True)
                yield from client.send_message(message.channel, str.join("", formatted_list))
        yield from client.add_reaction(message, random.choice(emojis))

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
