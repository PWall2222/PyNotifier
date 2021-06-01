# PyNotifier

PyNotifier is a Python3 app that uses the IMAP protocol for sending you the last email contents of a tag to your discord DMs.

## Requisites

- Python3
- Discord.py
- Discord Bot Token

## Installing discord.py

If you are in linux:

```bash
python3 -m pip install -U discord.py
```

If you are on windows:

```bash
py -3 -m pip install -U discord.py
```

## Instalation

```bash
git clone https://github.com/PWall2222/PyNotifier
cd PyNotifier
python3 main.py
```

Now you will get a prompt with all the parameters you need to use, you can make your own config.json if thats what you are into. The structure is:

```json
{
  "host": "imap.mail.com",
  "user": "user@example.com",
  "password": "1234",
  "tag": "INBOX",
  "token": "<Discord Token>",
  "discordID": "<Discord ID>"
}
```

## Author

- **PWall** - *Initial work* - [PWall](https://github.com/PWall2222)

## License

This project is licensed under the GPL v3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [PurpleBooth](https://github.com/PurpleBooth), for doing a README.md template.
