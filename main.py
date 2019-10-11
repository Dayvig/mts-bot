# bot.py
import os
import json
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
cirno_data = None
prefix = '!'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print('Loading mod data')
    load_data(cirno_data, 'cirno')
    
def load_data(data_field, mod_id):
    with open(f'data/{mod_id}/items.json') as json_file:
        data_field = json.load(json_file)
    print(f'Loaded {mod_id}!')

def is_command(message):
    return message.content.startswith(prefix)

def del_char(string, index):
    return ''.join((char for idx, char in enumerate(string) if idx not in indexes))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if is_command(message):
        message.content = del_char(message, len(prefix))
        get_id(message)
        
def get_id(message):
    s = message.content.lower()
    tokenized_message  = s.split(' ')[0]
    id_map(message.channel, tokenized_message)
    
def id_map(channel, tokenized_message):
    map = {
            'cirno': cirno_data
    }
    do_command(channel, tokenized_message, map.get(tokenized_message[1], print('wtf are u doing')))
    

def do_command(channel, tokenized_message, data):
    commands = {
        'card': card
    }
    callback = commands.get(tokenized_message[0])
    callback(channel, tokenized_message, data)

@client.event
async def card(channel, tokenized_message, data):
    await channel.send('pog')

client.run(token)

