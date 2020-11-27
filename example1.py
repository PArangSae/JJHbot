import discord
from discord.ext import commands
import time
import random
 
app = commands.Bot(command_prefix='제이봇 ')
 
@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    tell = discord.Game("이 서버 전용 봇입니다.")
    await app.change_presence(status=discord.Status.online, activity=tell)

@app.command()
async def 안녕(ctx):
    await ctx.send("안녕하세여! 저는 이 서버를 무법하는 제이봇이에여!")

@app.command()
async def 잘가(ctx):
    await ctx.send("?? 저 여기 계속 있을 건데여!")

@app.command()
async def 싫어(ctx):
    await ctx.send("싫으세여? ㅠㅠ")

@app.command()
async def 고마워(ctx, *, user):
    await ctx.send("저도여! 항상 이 서버를 이용해주셔서 감사해여!")

app.run('Token')
