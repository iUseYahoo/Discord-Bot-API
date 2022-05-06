# BotAPI-Dictionary
A discord bot with its own API, With a dictionary search function.

# What is this repoository?
- This repository is a discord bot which also contains a API for the discord bot to communicate with and pull the meaning of a certain word they enter if the item is in the database.

# Downloads and Requirements
### Discord Requirement(s)
- [Discord Bot Token](https://discord.com/developers/applications) - (REQUIRED)

### Software Requirements
- [Python](https://www.python.org/downloads/) - (REQUIRED)
- [SQLite DB Browser](https://sqlitebrowser.org/dl/) - (OPTIONAL, If you want to add more words to the database.)

# Python Package Requirements
- [Flask](https://pypi.org/project/Flask/) - (REQUIRED)
- [BeautifulSoup](https://pypi.org/project/bs4/) - (REQUIRED, If you want to use the whois API endpoint)

# Setup
- 1. Open [config.json](https://github.com/iUseYahoo/Discord-Bot-API-Dictionary/blob/main/config.json) and set a port for the API and Bot to use.
- 2. Open the Discord Bot [main.py](https://github.com/iUseYahoo/Discord-Bot-API-Dictionary/blob/main/Discord%20Bot/main.py) file and set the [token](https://github.com/iUseYahoo/Discord-Bot-API-Dictionary/blob/main/config.json#L3) to your [Discord Bot](https://discord.com/developers/applications)'s token.

# Notes
- 1. The Discord Bot will automatically use the port the API is using.
- 2. The Server will automatically save its port that its using to the config.json file.
- Final: The port will automatically save and be detected and used.
