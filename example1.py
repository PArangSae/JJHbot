import asyncio
import discord

app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    await app.change_presence(game=discord.Game(name="JJH봇이에여!", type=1))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "고마워":
        await message.channel.send("JJH봇을 써주셔서 고마워여!!!")

app.run("token")
