import asyncio
import discord
import random
import re

app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    await app.change_presence(activity=discord.Game(name="jjh help"))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "jjh 고마워":
        await message.channel.send("JJH봇을 써주셔서 고마워여!!!")
    if message.content=="jjh help" or message.content.startswith("jjh 도움말"):
        embed = discord.Embed(title = "명령어", description = "**명령어 목록!**", color=0xd1173b)
        embed2 = discord.Embed(title = "jjh 청소 n", description = "적은 수 만큼 채팅을 삭제 할 수 있어여![메시지 관리권한 이상만 가능해여!]", color=0xd1173b)
        await message.channel.send(embed=embed)
        await message.channel.send(embed=embed2)
    if message.content.startswith("jjh 청소 "):
        if message.author.guild_permissions.manage_messages:
            try:
                cu = message.content[7:]
                if int(cu) < 1:
                    embed = discord.Embed(color=0xff0000)
                    embed.add_field(name = "계산오류", value = " \nn 에는 최소 1이 들어가야 합니다.", colour=0x0097ff, inline=True)
                    await message.channel.send(embed = embed)
                if int(cu) > 999:
                    embed = discord.Embed(color=0xebeb00)
                    embed.add_field(name = "주의", value = " \n설정된수가 1000이상일때는 렉이 있을 수 있습니다.", colour=0x0097ff, inline=True)
                    await message.channel.send(embed = embed)
                    p = 1
                    pass
                embed = discord.Embed(title = "청소 시작! :wastebasket:", description = cu + " 개의 메시지 청소준비..", colour=0x0097ff, inline=True)
                await message.channel.send(embed=embed)
                p = 1
                if p == 1:
                    cu = int(cu) + 2
                else:
                    cu = int(cu) + 1
                await message.channel.purge(limit=int(cu))
                if p == 1:
                    cu = int(cu) - 2
                else:
                    cu = int(cu) - 1
                        
                embed = discord.Embed(title = "청소 완료! :sparkles:", description = str(cu) + " 개의 메시지를 청소했어요!", colour=0x0097ff, inline=True)
                await message.channel.send(embed=embed)
            except ValueError:
                embed = discord.Embed(color=0xff0000)
                embed.add_field(name = "오류 - 구문", value = " \n청소 n 또는 n 에 정수가 들어가야 합니다", inline=True)
                await message.channel.send(embed = embed)
        else:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name = "오류 - 권한", value = " \n이 작업을 수행할 권한을 가지고 있지 않습니다.", inline=True)
            await message.channel.send(embed = embed)
    if message.content == "jjh 아재개그":
        p = random.randint(1, 4)
        if p == 1:
            embed = discord.Embed(title = ":laughing:", description = "싸움을 가장 잘하는 오리는? ~~**을지문덕**~~", colour=0x0097ff)
            await message.channel.send(embed=embed)
        elif p == 2:
            embed = discord.Embed(title = ":laughing:", description = "왕이 넘어지면? ~~**킹콩**~~", colour=0x0097ff)
            await message.channel.send(embed=embed)
        elif p == 3:
            embed = discord.Embed(title = ":laughing:", description = "액체이자 고체인 물질은? ~~**수증기**~~", colour=0x0097ff)
            await message.channel.send(embed=embed)
        elif p == 4:
            embed = discord.Embed(title = ":laughing:", description = "번개의 온도가 높은지 용앙 분출할 때의 온도가 더 높은지 정확하게 아는 법은? ~~**직접 경험하기**~~", colour=0x0097ff)
            await message.channel.send(embed=embed)
        await message.channel.send("아핳ㅎ하ㅏㅏ핳ㅎ하하하핳ㅎ하")
    if str(re.search(r'\[\[[^\]]*\]\]', message.content)) != "None":
        yadiyadi = re.search(r'\[\[[^\]]*\]\]', message.content)
        keyword = yadiyadi.group()
        repledkeyword = keyword.lstrip('[')
        repledkeyword = repledkeyword.lstrip("[")
        repledkeyword = repledkeyword.rstrip("]")
        repledkeyword = repledkeyword.rstrip("]")
        repledkeyword2 = repledkeyword.replace(" ", "_")
        keywordlink = "https://ko.wikipedia.org/wiki/" + repledkeyword2
        await message.channel.send("링크: "+keywordlink)

app.run("token")
