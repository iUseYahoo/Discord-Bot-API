import discord
from discord.ext import commands
import requests, json

BOT_TOKEN = ""
PREFIX = "+"

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
  print("\n== BOT IS ONLINE==\n")

@client.command()
async def dictionary(ctx, *, msg):

    if msg is None:
        await ctx.send("Please enter a word")
    else:
        # get the port from config.json
        with open('config.json') as json_file:
            data = json.load(json_file)
            api_port = data['port']
            
            api = f'http://127.0.0.1:{api_port}/dictionary/?word={str(msg)}'
            json_file.close()

            r = requests.get(api).text

            await ctx.send(f"{str(r)}")


if __name__ == '__main__':
    client.run(BOT_TOKEN)
