import discord
import asyncio
import random

client = discord.Client()

friend_words = ['pal','buddy','boi','friendo','mate','chum','associate','amigo','hombre','compadre','comrade','homeboy','partner','main man','bosom pal','informal homeboy','informal gabba','absolute no life little bitch human trash mega faggot']
shit_words = ['jacob','math','learning','dynamics','convolution','study','meme','bot','shit','#','richard','throat','laplace','boi','lmao','lol','wow','rofl','doge']
emojis = ['🤓','🕍','🛂','⛳','🤗','🈶','🤑','😒','🤓','😤','🤡','🤥','👿','💀','👻','👽','👾','💩','☠','👶','🎅','👲','🙍','🚶','🙃']
shit_list = []
nice_words = ['cool','radical','sweet','beautiful','gorgeous','perfect','amazing','irresistible','tasty','delicious','signor','divine','knockout','weeb trash','ravishing','heavenly','foxy','smashing','autistic','vile','degenerate','crispy','ripe','hygenic']
theres = ['their','theyre','they are','there','theire','thier',"they're",'theirie','bear','thire']

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

        for shit_word in shit_words:
            if shit_word in message.content.lower():
                shit_list.append(message.author.nick)
                formatted_list = ["{0} x{1}\n".format(member,shit_list.count(member)) for member in set(shit_list)]
                yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(nice_words) + ' ' + random.choice(friend_words), tts=True)
                yield from client.send_message(message.channel, str.join("", formatted_list), tts=True)
        yield from client.add_reaction(message, random.choice(emojis))

client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
