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

        bad_sql = open('../bad_sql.txt', 'r')

        for line in bad_sql:
            if msg in line:
                bad_sql.close()
                await ctx.send("You're a bad person, But nice try.")
                await ctx.send("https://tenor.com/view/facepalm-double-crowd-funny-omg-gif-16929018")

        # get the port from config.json
        with open('../config.json') as json_file:
            data = json.load(json_file)
            api_port = data['port']
            
            api = f'http://127.0.0.1:{api_port}/dictionary/?word={str(msg)}'
            json_file.close()

            r = requests.get(api).text

            await ctx.send(f"{str(r)}")


if __name__ == '__main__':
    with open('../config.json') as json_file:
        data = json.load(json_file)
        api_port = data['port']
        print("The bot will use the API port: " + str(api_port))
    
        json_file.close()
    
    client.run(BOT_TOKEN)
