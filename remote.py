from threading import Thread
import json
import asyncio
import discord


with open("./config.json") as f:
	config = json.load(f)
	
discordToken = config["token"]

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

async def sendMessage(data,userID):
	channel = await client.fetch_user(userID)
	await channel.send(data)

def init():
	loop = asyncio.get_event_loop()
	loop.create_task(client.start(discordToken))
	Thread(target=loop.run_forever())
