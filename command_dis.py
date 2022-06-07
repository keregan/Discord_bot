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

global v_c
bot_command = commands.Bot(command_prefix='>')
client = discord.Client()

YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'False', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
               'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


@bot_command.event  # Event + news_day
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


async def genshin_hub(bot):
    channel = bot.get_channel(954827377085669396)
    vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
    vk_ver = "5.131"
    domain = "genshin_hub"

    reponse = requests.get('https://api.vk.com/method/wall.get',
                           params={
                               'access_token': vk_pars,
                               'v': vk_ver,
                               'domain': domain,
                               'count': 1,
                               'offset': 1
                           }
                           )
    posts = reponse.json()['response']['items']
    i = 0
    for post in posts:
        try:
            if "attachments" in post:
                post = post["attachments"]
                if post[0]["type"] == "photo":
                    for i in range(len(post)):
                        url_photo = post[i]['photo']['sizes'][-1]['url']
                        messages = await channel.history(limit=200).flatten()
                        word = url_photo
                        i = 0
                        for msg in messages:
                            if msg.content == word:
                                no_post_2 = 0
                                break
                            else:
                                no_post_2 = 1
                        if no_post_2 == 1:
                            await channel.send(url_photo)
                        await asyncio.sleep(1)
        except:
            pass


async def genshin_giarts(bot):
    channel = bot.get_channel(954827377085669396)
    vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
    vk_ver = "5.131"
    domain = "giarts"

    reponse = requests.get('https://api.vk.com/method/wall.get',
                           params={
                               'access_token': vk_pars,
                               'v': vk_ver,
                               'domain': domain,
                               'count': 1,
                               'offset': 1
                           }
                           )
    posts = reponse.json()['response']['items']

    i = 0
    for post in posts:
        try:
            if "attachments" in post:
                post = post["attachments"]
                if post[0]["type"] == "photo":
                    for i in range(len(post)):
                        url_photo = post[i]['photo']['sizes'][-1]['url']
                        if url_photo[11] == "9":
                            messages = await channel.history(limit=200).flatten()
                            word = url_photo
                            i = 0
                            for msg in messages:
                                if msg.content == word:
                                    no_post_2 = 0
                                    break
                                else:
                                    no_post_2 = 1
                            if no_post_2 == 1:
                                await channel.send(url_photo)
                            await asyncio.sleep(1)
        except:
            pass


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


async def promo_genshinimpact (bot):
    channel = bot.get_channel(982738188911132683)
    vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
    vk_ver = "5.131"
    domain = "genshinpromo"

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
    for post in data:
            text_post = post['text']
            if "Промокоды:" in text_post:
                promokod = 1
            else:
                promokod = 0

            messages = await channel.history(limit=200).flatten()
            i = 0
            for msg in messages:
                if msg.content == text_post:
                    no_post_2 = 0
                    break
                else:
                    no_post_2 = 1
            if no_post_2 == 1:
                if promokod == 1:
                    await channel.send("<@&983836821383442462> " + text_post)


@bot_command.command()  # Massage
async def ok(ctx):  # return answer
    await ctx.send('ok')


@bot_command.command()  # Music + radio
async def radio(ctx):  # Radio-list bot
    if ctx.author.voice is None:
        return await ctx.send("You are not connected to a voice channel")
    else:
        return await ctx.send(" Radio-list:\n>Energy\n>Dacha\n>Evropa\n")


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


@bot_command.command()  # Youtube_list
async def youtube_list(ctx, arg):  # Youtube
    arg = str(arg).replace("(", "")
    arg = str(arg).replace(')', '')
    arg = str(arg).replace(',', '')
    arg = str(arg).replace("'", "")
    channel = "982160360897396736"
    videosSearch = VideosSearch(arg, limit=5)
    res_name_1 = videosSearch.result()['result'][0]['title']
    res_url_1 = videosSearch.result()['result'][0]['link']
    res_name_2 = videosSearch.result()['result'][1]['title']
    res_url_2 = videosSearch.result()['result'][1]['link']
    res_name_3 = videosSearch.result()['result'][2]['title']
    res_url_3 = videosSearch.result()['result'][2]['link']
    res_name_4 = videosSearch.result()['result'][3]['title']
    res_url_4 = videosSearch.result()['result'][3]['link']
    res_name_5 = videosSearch.result()['result'][4]['title']
    res_url_5 = videosSearch.result()['result'][4]['link']

    await ctx.send("Для начала введите команду >p[номер]:")
    await ctx.send("1) " + res_name_1)
    await ctx.send("2) " + res_name_2)
    await ctx.send("3) " + res_name_3)
    await ctx.send("4) " + res_name_4)
    await ctx.send("5) " + res_name_5)


async def youtube_p1(ctx, bot):
    messages = await ctx.history(limit=20).flatten()
    word = ">y"
    i = 0
    for msg in messages:
        if word in msg.content:
            no_post_3 = 1
            name = msg.content
            break
        else:
            no_post_3 = 0

    if no_post_3 == 0:
        await ctx.send('Повторите запрос')
    else:
        voice_channel = ctx.message.author.voice.channel
        v_c = ctx.channel.guild.voice_client
        url_name = name.replace('>y ', '')
        videosSearch = VideosSearch(url_name, limit=1)
        res_url_1 = videosSearch.result()['result'][0]['link']

        await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.cache.remove()
            if 'https://' in res_url_1:
                info = ydl.extract_info(res_url_1, download=False)
        videotitle = info.get('title')

        URL = info['formats'][0]['url']

        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
        videotitle = info.get('title', 'Video   with ID: ' + info.get('id', 'unknown'))
        await ctx.send(f"Playing {videotitle}")
        videotitle = videotitle + "       "
        # while v_c.is_playing:
        #     await asyncio.sleep(1)
        #     videotitle = videotitle[1:] + videotitle[0]
        #     await bot.change_presence(status=discord.Status.online,
        #                               activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))


async def youtube_p2(ctx):
    messages = await ctx.history(limit=20).flatten()
    word = ">y"
    i = 0
    for msg in messages:
        if word in msg.content:
            no_post_3 = 1
            name = msg.content
            break
        else:
            no_post_3 = 0

    if no_post_3 == 0:
        await ctx.send('Повторите запрос')
    else:
        voice_channel = ctx.message.author.voice.channel
        v_c = ctx.channel.guild.voice_client
        url_name = name.replace('>y ', '')
        videosSearch = VideosSearch(url_name, limit=2)
        res_url_1 = videosSearch.result()['result'][1]['link']

        await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.cache.remove()
            if 'https://' in res_url_1:
                info = ydl.extract_info(res_url_1, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{res_url_1}", download=False)['entries'][0]
        videotitle = info.get('title')

        URL = info['formats'][0]['url']

        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
        videotitle = info.get('title', 'Video   with ID: ' + info.get('id', 'unknown'))
        await ctx.send(f"Playing {videotitle}")
        videotitle = videotitle + "       "


async def youtube_p3(ctx):
    messages = await ctx.history(limit=20).flatten()
    word = ">y"
    i = 0
    for msg in messages:
        if word in msg.content:
            no_post_3 = 1
            name = msg.content
            break
        else:
            no_post_3 = 0

    if no_post_3 == 0:
        await ctx.send('Повторите запрос')
    else:
        voice_channel = ctx.message.author.voice.channel
        v_c = ctx.channel.guild.voice_client
        url_name = name.replace('>y ', '')
        videosSearch = VideosSearch(url_name, limit=3)
        res_url_1 = videosSearch.result()['result'][2]['link']

        await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.cache.remove()
            if 'https://' in res_url_1:
                info = ydl.extract_info(res_url_1, download=False)

        videotitle = info.get('title')

        URL = info['formats'][0]['url']

        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
        videotitle = info.get('title', 'Video   with ID: ' + info.get('id', 'unknown'))
        await ctx.send(f"Playing {videotitle}")
        videotitle = videotitle + "       "


async def youtube_p4(ctx):
    messages = await ctx.history(limit=20).flatten()
    word = ">y"
    i = 0
    for msg in messages:
        if word in msg.content:
            no_post_3 = 1
            name = msg.content
            break
        else:
            no_post_3 = 0

    if no_post_3 == 0:
        await ctx.send('Повторите запрос')
    else:
        voice_channel = ctx.message.author.voice.channel
        v_c = ctx.channel.guild.voice_client
        url_name = name.replace('>y ', '')
        videosSearch = VideosSearch(url_name, limit=4)
        res_url_1 = videosSearch.result()['result'][3]['link']

        await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.cache.remove()
            if 'https://' in res_url_1:
                info = ydl.extract_info(res_url_1, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{res_url_1}", download=False)['entries'][0]
        videotitle = info.get('title')

        URL = info['formats'][0]['url']

        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
        videotitle = info.get('title', 'Video   with ID: ' + info.get('id', 'unknown'))
        await ctx.send(f"Playing {videotitle}")
        videotitle = videotitle + "       "


async def youtube_p5(ctx):
    messages = await ctx.history(limit=20).flatten()
    word = ">y"
    i = 0
    for msg in messages:
        if word in msg.content:
            no_post_3 = 1
            name = msg.content
            break
        else:
            no_post_3 = 0

    if no_post_3 == 0:
        await ctx.send('Повторите запрос')
    else:
        voice_channel = ctx.message.author.voice.channel
        v_c = ctx.channel.guild.voice_client
        url_name = name.replace('>y ', '')
        videosSearch = VideosSearch(url_name, limit=5)
        res_url_1 = videosSearch.result()['result'][4]['link']

        await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
        voice_channel = ctx.message.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        else:
            ctx.voice_client.stop()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.cache.remove()
            if 'https://' in res_url_1:
                info = ydl.extract_info(res_url_1, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{res_url_1}", download=False)['entries'][0]
        videotitle = info.get('title')

        URL = info['formats'][0]['url']

        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
        videotitle = info.get('title', 'Video   with ID: ' + info.get('id', 'unknown'))
        await ctx.send(f"Playing {videotitle}")
        videotitle = videotitle + "       "


@bot_command.command()  # Every_day_commands
async def join(ctx):  # Connect bot
    channel = ctx.author.voice.channel
    await channel.connect()


async def leave(ctx):  # Disconnect bot
    await ctx.voice_client.disconnect()


async def stop(ctx, bot):  # Stop music bot
    ctx.voice_client.stop()
    await bot.change_presence(status=discord.Status.online,activity=discord.Activity(name="Звуки тишины", type=discord.ActivityType.listening))


async def helping(ctx):  # Write-trigger bot
    await ctx.send("Commands bot:\n"
                   ">helping - Помощь по командам\n"
                   ">radio - Список доступных радио волн\n"
                   ">play [URL]- Проигрывание песен по ссылки\n"
                   ">playr [URL]- Проигрывание песен по ссылки c повтороением\n"
                   ">join - Подключить бота к каналу\n"
                   ">leave - Отключить бота от канала\n"
                   ">stop - Остановить песню")

