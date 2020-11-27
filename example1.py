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
    if message.content=="help" or message.content.startswith("도움말"):
        embed = discord.embed(title = "명령어", description = "** **", color=0xd1173b)
        embed.add_field(name = "청소 n", value = "적은 수 만큼 채팅을 삭제 할 수 있어여![메시지 관리권한 이상만 가능해여!]
        await message.channel.send(embed=embed)
    

app.run("token")
