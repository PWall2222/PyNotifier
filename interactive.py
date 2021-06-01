import json

def setConfig():
	config = {}
	config["host"] = input("Whats your IMAP host?")
	config["user"] = input("Whats your IMAP user?")
	config["password"] = input("Whats your IMAP password?")
	config["tag"] = input("What IMAP tag do you wanna read from?")
	config["token"] = input("Whats your discord bot token?")
	config["discordID"] = input("Whats your discord ID?")

	configJSON = json.dumps(config)

	with open("./config.json", "w") as f:
		f.write(configJSON)

	return config