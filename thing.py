import discord
import asyncio
import random
import datetime
import schedule
import time 
from words import search, vocabulary
from eventmaker import eventdetector, profilepicture, specialprofilechecker
from urllib.request import Request, urlopen

client = discord.Client()
shit_list = []
most_recent_channel = None

@asyncio.coroutine
def background_task():
    try:
        cusdiscord
    except NameError:
        cusdiscord = time.time()
    yield from client.wait_until_ready()
    yield from client.change_presence(status=discord.Status.invisible)
    while not client.is_closed:
        if specialprofilechecker is True:            
            yield from client.edit_profile(avatar=urlopen(profilepicture).read())  
        else:
            if (time.time() - cusdiscord) >= 800:
                yield from client.edit_profile(avatar=urlopen('http://temp_thoughts_resize.s3.amazonaws.com/50/c374f48ee73f51e0063231945cf27d/sticker_375x360.png').read())
                cusdiscord = time.time()
        if specialprofilechecker is True:
                yield from client.send_message(message.channel, random.choice(eventdetector), tts=True)
        yield from client.send_message(discord.Object(id='228814605923647488'),random.choice(vocabulary['nice']))
        yield from asyncio.sleep(60)        

@client.async_event
def on_typing(ch, user, when):
    try:
        cusdiscordsuxs
    except NameError:
        cusdiscordsuxs = time.time()
    if abs(time.time() - cusdiscordsuxs) > 60:
        print('you finally got good i see')
        yield from client.send_message(discord.Object(id='228814605923647488'),'That looks like a real nice message you have there',tts = True)
        
@client.async_event
def on_message(received_message):
    if received_message.channel.is_private:
         yield from client.send_message(last_message.channel, received_message.content)
    else:
        last_message = received_message
        triggered = False;
        emojis = random.choice(vocabulary['emojis'])
        if received_message.author != received_message.server.me:
            if received_message.server.me.nick.lower() in received_message.content.lower():
                    yield from client.send_message(received_message.channel, random.choice(vocabulary['angry']) )
            if 'knee' in received_message.content.lower():
                yield from client.delete_message(received_message)
                comment = vocabulary['bee']
                for split_message in [comment[character:character+1500] for character in range(0, len(comment), 1500)]:
                    yield from client.send_message(received_message.channel, split_message)                  
            if received_message.content.lower().startswith('hi '):
                avatar = urlopen(Request(received_message.author.avatar_url.replace('webp','jpeg'), headers={'User-Agent': 'Mozilla/5.0'})).read()
                #yield from client.edit_role(received_message.server, received_message.server.me.top_role, colour=received_message.author.color)
                yield from client.edit_profile(avatar=avatar, username=received_message.author.name)
                yield from client.change_presence(status=discord.Status.invisible)
                yield from client.change_nickname(received_message.server.me, received_message.author.nick)
                yield from client.delete_message(received_message)
                yield from client.send_message(received_message.channel, received_message.content + ' also i enjoy penis')
                return # Stop message processing here, because the message is gone, and we don't won't to compromise our identity
            if str(int(datetime.datetime.now().minute)) + 'clear' in received_message.content.lower():
                yield from client.purge_from(received_message.channel, before=datetime.datetime.now() - datetime.timedelta(minutes=15), check=lambda message:received_message.author == client.user)
                yield from client.delete_message(received_message)
                return
            for wordlist_name, words in search.items():
                for word in words:
                    if word in received_message.content.lower():
                        if wordlist_name in ['yours','theres']:
                            yield from client.send_message(received_message.channel, '*' + random.choice(vocabulary[wordlist_name]))
                        if wordlist_name is 'shia':
                            yield from client.send_message(received_message.channel, 'He\'s following you, about 30 feet back')
                        if wordlist_name in ['hitler','ussr']:
                            for phrase in vocabulary[wordlist_name]:
                                yield from client.send_message(received_message.channel, phrase)
                            emojis = ['🇭','🇮','🇪','🇱']
                        if wordlist_name is 'learning':
                            yield from client.send_message(received_message.channel,'existence is pain')
                            emojis = ['🇫','🇺','🇨','🇰']
                        if wordlist_name is 'friend':
                            yield from client.send_message(received_message.channel,"i ain't your " + word + ', ' + random.choice(vocabulary['friend']))
                            emojis = ['🇫','🇺','🇨','🇧','🇴','🇮']
                        if wordlist_name is 'shit':
                            shit_list.append(received_message.author)
                            emojis =  '💩'
                        if wordlist_name is 'instadeletecomments':
                            yield from client.send_message(received_message.channel, 'You have fucked up now', tts=True)
                            triggered = True;
                            yousucktimer = time.time()
                            shitauthor = received_message.author   
            if emojis is  '💩':
                formatted_list = []
                for user in set(shit_list):
                    name = user.display_name
                    entry = "{0} x{1}".format(name, shit_list.count(user))
                    formatted_list.append(entry)
                yield from client.send_message(received_message.channel, 'you have entered the shit list ' + random.choice(vocabulary['nice']) + ' ' + random.choice(vocabulary['friend']))
                yield from client.send_message(received_message.channel, str.join("\n", formatted_list))
            for emoji in emojis:
                yield from client.add_reaction(received_message, emoji)
            if triggered is True: 
                while (time.time() - yousucktimer) < 300: 
                    print('elmayo')
                    if received_message.author == shitauthor:
                        yield from client.delete_message(received_message)
                        yield from client.send_message(received_message.channel, 'Did you guys hear something?', tts=True)

client.loop.create_task(background_task())
client.run(input('token: '))
