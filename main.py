from interactive import setConfig
from modules import setInterval
from imap_tools import MailBox
import asyncio
import json

try:
	f = open("config.json")
	config = json.load(f)
except IOError:
	config = setConfig()

import remote

loop = asyncio.get_event_loop()

imapHost = config["host"]
imapUser = config["user"]
imapPass = config["password"]
imapTag = config ["tag"]

discordID = config["discordID"]

def write(data):
	f = open("uid", "w")
	f.write(data)
	f.close()

def readUID():
	f = open("uid", "r")
	return f.read()

def checkUID(uid):
	return readUID() == uid

def send(data,userID):
	return loop.create_task(remote.sendMessage(data,userID))

def processMail(message):
	if checkUID(message.uid):
		return
	write(message.uid)
	data = message.text or message.html
	send(data, discordID)

def getMail():
	for message in mailbox.fetch(limit=1, reverse=True):
		return message

def mail():
	message = getMail()
	processMail(message)

mailbox = MailBox(imapHost).login(imapUser, imapPass, initial_folder=imapTag)

setInterval(mail,10)

remote.init()
