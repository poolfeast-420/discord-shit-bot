import discord
import asyncio
import time
from random import randint

client = discord.Client()
last_message_time = time.time();

friend_words = ['pal','buddy','boi','friendo','mate','chum','associate','amigo','fagotron','hombre','compadre','comrade','homeboy','partner','main man','bosom pal','informal homeboy','informal gabba','absolute no life little bitch human trash mega faggot']
shit_words = ['jacob','math','learning','dynamics','convolution','study','meme','bot','shit','#','richard','throat','laplace','boi','lmao','stat','lol','jag','wow','rofl','doge','john gear']
emojis = ['🤓','🕍','🛂','⛳','🤗','🈶','🤑','😒','🤓','😤','🤡','🤥','👿','💀','👻','👽','👾','💩','☠','👶','🎅','👲','🙍','🚶','🙃']
shit_list = []
nice_words = ['cool','radical','sweet','beautiful','gorgeous','perfect','amazing','irresistible','tasty','delicious','signor','divine','knockout','weeb trash','ravishing','heavenly','foxy','smashing','autistic','vile','degenerate','crispy','ripe','hygenic']
theres = ['their','theyre','they are','there','theire','thier',"they're",'theirie','bear','thire']
daily_grilling = ['Get the fuck of discord you little bitch','why are you always on discord? Must be because you have no real friends','Get of discord and follow your destony, working at Maccas forever']

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
        if str(message.server.me.nick).lower() in message.content.lower():
                yield from client.send_message(message.channel,'fuk u')
        for shit_word in shit_words:
            if shit_word in message.content.lower():
                shit_list.append(message.author.nick)
                formatted_list = ["{0}\n".format(member) for member in shit_list]
                yield from client.send_message(message.channel, 'you have entered the shit list ' + random.choice(nice_words), tts=True)
                yield from client.send_message(message.channel, str.join("", formatted_list))       
        if (time.time() - last_message_time) > randint(9000,30000): 
            yield from client.send_message(message.channel, random.choice(daily_grilling), tts=True)
        last_message_time = time.time();
        yield from client.add_reaction(message, random.choice(emojis))
        
    #checks if the user has asked the bot a question, then give a random response from response list    
    if question_words message.content.lower():
        yield from client.send_message(message.channel, random.choice(question_responses), tts=True)
        
client.run('MjkzMjMyMTMzMjgyMjAxNjAy.C7DqOw.ujB3abjJtzTkHHXf6hLXFGJ1UU0')
