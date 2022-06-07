import asyncio
import random
from asyncio import sleep
from dataclasses import replace
import command_dis
import discord
import requests
from bs4 import BeautifulSoup as BS, BeautifulSoup
from discord import ActivityType, Activity, FFmpegPCMAudio
from discord.ext import commands
from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch

bot_command = commands.Bot(command_prefix='>')
client = discord.Client()

YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'False', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
               'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


@bot_command.event
async def news_stopgame(bot):
    channel = bot.get_channel(982738188911132683)
    passers_1 = requests.get("https://stopgame.ru/news")
    html = BS(passers_1.content, 'html.parser')
    title = html.find('div', class_='caption')
    score = int(len(str(title)))
    old = (str(title))

    tegg = ""
    tred = 0
    j = 44
    while j < int(score):
        if old[j] == ">":
            j = int(score)
        else:
            tegg = tegg + old[j]
            j = j + 1
    score_2 = int(len(tegg))
    Remove_last = tegg[:score_2 - 1]
    ends = "https://stopgame.ru/" + Remove_last
    las_end = "Последнии новости на stopgame.ru: " + ends

    messages = await channel.history(limit=200).flatten()
    word = las_end
    i = 0
    for msg in messages:
        if msg.content == word:
            no_post_1 = 0
            break
        else:
            no_post_1 = 1

    if no_post_1 == 1:
        await channel.send(las_end)


async def joi_reactor(bot):
    channel = bot.get_channel(954827377085669396)
    url = "http://joyreactor.cc/tag/%D0%9C%D1%83%D0%BB%D1%8C%D1%82%D1%8D%D1%80%D0%BE%D1%82%D0%B8%D0%BA%D0%B0"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    text = requests.get(url, headers=headers)
    soup = BeautifulSoup(text.content, 'html.parser')
    div_1 = soup.find("div", class_="postContainer")
    div_2 = div_1.find("div", class_="post_content")
    image = div_2.find("a", class_="prettyPhotoLink").get("href")

    messages = await channel.history(limit=200).flatten()
    word = image
    i = 0
    for msg in messages:
        if msg.content == word:
            no_post_2 = 0
            break
        else:
            no_post_2 = 1
    if no_post_2 == 1:
        await channel.send(image)


async def news_genshinimpact(bot):
    channel = bot.get_channel(982738188911132683)
    vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
    vk_ver = "5.131"
    domain = "genshinimpact"

    reponse = requests.get('https://api.vk.com/method/wall.get',
                           params={
                               'access_token': vk_pars,
                               'v': vk_ver,
                               'domain': domain,
                               'count': 1,
                               'offset': 1
                           }
                           )
    data = reponse.json()['response']['items']
    vid_p = "https://vk.com/video"
    vid_post_1 = ''
    vid_post_2 = ''
    vid_img = ''
    for post in data:
        try:
            text_post = post['text']
        except:
            text_post = 'pass'

        try:
            if post['attachments'][0]['type']:
                img_post = post['attachments'][0]['photo']['sizes'][-1]['url']
            else:
                img_post = ''
        except:
            img_post = ''

        try:
            if post['owner_id']:
                vid_post_1 = post['owner_id']
            else:
                vid_post_1 = ''
        except:
            vid_post_1 = ''
        try:
            if post['attachments'][0]['type']:
                vid_post_2 = post['attachments'][0]['video']['id']
            else:
                vid_post_2 = ''
        except:
            vid_post2 = ''
        try:
            if post['attachments'][0]:
                vid_img = post['attachments'][0]['video']['image'][8]['url']
            else:
                vid_img = ''
        except:
            vid_img = ''

    vid_p = vid_p + str(vid_post_1) + "_" + str(vid_post_2)
    if vid_p == "https://vk.com/video" or vid_p == "https://vk.com/video-183293188_":
        vid_p = ''
    vk_poser = "Genshin Impact последнии новости:\n" + text_post + " *" + vid_p + "*"
    messages = await channel.history(limit=200).flatten()
    word = vk_poser
    i = 0
    for msg in messages:
        if msg.content == word:
            no_post_2 = 0
            break
        else:
            no_post_2 = 1
    if no_post_2 == 1:
        await channel.send(vk_poser)
        try:
            await channel.send(vid_img)
        except:
            pass
        try:
            await channel.send(img_post)
        except:
            pass


@bot_command.command()
async def ok(ctx):
    await ctx.send('ok')
    # return answer


@bot_command.command()
async def radio(ctx):  # Radio-list bot
    if ctx.author.voice is None:
        return await ctx.send("You are not connected to a voice channel")
    else:
        return await ctx.send(" Radio-list:\n>Energy\n>Dacha\n>Evropa\n")


@bot_command.command()
async def redio_Energy(ctx, bot):
    if ctx.author.voice is None:
        return await ctx.send("You are not connected to a voice channel")
    else:
        if ctx.author.voice.channel is None:
            channel = ctx.author.voice.channel
            await channel.connect()
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Activity(name="Radio Energy", type=discord.ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()
        ctx.voice_client.play(FFmpegPCMAudio("https://pub0201.101.ru:8443/stream/air/mp3/256/99"), )


@bot_command.command()
async def redio_Dacha(ctx, bot):
    if ctx.author.voice is None:
        return await ctx.send("You are not connected to a voice channel")
    else:
        if ctx.author.voice.channel is None:
            channel = ctx.author.voice.channel
            await channel.connect()
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Activity(name="Radio Dacha", type=discord.ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()
        ctx.voice_client.play(FFmpegPCMAudio(
            "https://stream2.n340.com/12_dacha_28_reg_1093?type=.aac&UID=C21958B7AA80EA280465EA8518C6F363"), )


@bot_command.command()
async def redio_Evropa(ctx, bot):
    if ctx.author.voice is None:
        return await ctx.send("You are not connected to a voice channel")
    else:
        if ctx.author.voice.channel is None:
            channel = ctx.author.voice.channel
            await channel.connect()
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Activity(name="Radio Evropa", type=discord.ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()
        ctx.voice_client.play(FFmpegPCMAudio("https://ep256.hostingradio.ru:8052/europaplus256.mp3"), )


@bot_command.command()
async def join(ctx):  # Connect bot
    channel = ctx.author.voice.channel
    await channel.connect()


@bot_command.command()
async def leave(ctx):  # Disconnect bot
    await ctx.voice_client.disconnect()


@bot_command.command()
async def stop(ctx, bot):  # Stop music bot
    ctx.voice_client.stop()
    await bot.change_presence(status=discord.Status.online,activity=discord.Activity(name="Звуки тишины", type=discord.ActivityType.listening))


@bot_command.command()
async def helping(ctx):  # Write-trigger bot
    await ctx.send("Commands bot:\n"
                   ">helping - Помощь по командам\n"
                   ">radio - Список доступных радио волн\n"
                   ">play [URL]- Проигрывание песен по ссылки\n"
                   ">playr [URL]- Проигрывание песен по ссылки c повтороением\n"
                   ">join - Подключить бота к каналу\n"
                   ">leave - Отключить бота от канала\n"
                   ">stop - Остановить песню")


@bot_command.command()
async def play(ctx, arg, bot):  # Http ran
    arg = str(arg).replace("(", "")
    arg = str(arg).replace(')', '')
    arg = str(arg).replace(',', '')
    arg = str(arg).replace("'", "")
    voice_channel = ctx.message.author.voice.channel
    v_c = ctx.channel.guild.voice_client
    if v_c is None:
        v_c = await voice_channel.connect()
    else:
        ctx.voice_client.stop()

    with YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.cache.remove()
        if 'https://' in arg:
            info = ydl.extract_info(arg, download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            # videotitle = info.get('title')
            # await ctx.send(f"{videotitle}")
    videotitle = info.get('title')
    URL = info['formats'][0]['url']
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name = videotitle, type = discord.ActivityType.listening))
    v_c.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
    videotitle = info.get('title', 'Video   with ID: ' + info.get('id', 'unknown'))
    await ctx.send(f"Playing {videotitle}")
    videotitle = videotitle + "       "
    while v_c.is_playing:
        await asyncio.sleep(1)
        videotitle = videotitle[1:] + videotitle[0]
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name = videotitle, type = discord.ActivityType.listening))
    while v_c.is_playing():
        await sleep(1)
    if not v_c.is_paused():
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name = "Звук тишины", type = discord.ActivityType.listening))
    # await v_c.disconnect()