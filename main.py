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

bot = commands.Bot(command_prefix='>')
client = discord.Client()

YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'False', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
               'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

global v_c


@bot.event
async def on_ready():  # Start bot
    print('Bot connect')
    while True:
        await command_dis.news_stopgame(bot)
        await asyncio.sleep(1)
        await command_dis.joi_reactor(bot)
        await asyncio.sleep(1)
        await command_dis.news_genshinimpact(bot)
        await asyncio.sleep(1)

        random_poss = random.randint(55, 180)
        await asyncio.sleep(random_poss)


@bot.command()
async def p(ctx, *arg):
    await command_dis.play(ctx, arg, bot)


@bot.command()
async def y(ctx, *arg):  # Youtube
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


@bot.command()
async def p1(ctx):
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
        # print(videosSearch.result())
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
        while v_c.is_playing:
            await asyncio.sleep(1)
            videotitle = videotitle[1:] + videotitle[0]
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        # while v_c.is_playing():
        #     await sleep(1)
        # if not v_c.is_paused():
        #     await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Звук тишины", type=discord.ActivityType.listening))


@bot.command()
async def p2(ctx):
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
        # print(videosSearch.result())
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
        while v_c.is_playing:
            await asyncio.sleep(1)
            videotitle = videotitle[1:] + videotitle[0]
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        # while v_c.is_playing():
        #     await sleep(1)
        # if not v_c.is_paused():
        #     await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Звук тишины", type=discord.ActivityType.listening))


@bot.command()
async def p3(ctx):
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
        # print(videosSearch.result())
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
        while v_c.is_playing:
            await asyncio.sleep(1)
            videotitle = videotitle[1:] + videotitle[0]
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        # while v_c.is_playing():
        #     await sleep(1)
        # if not v_c.is_paused():
        #     await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Звук тишины", type=discord.ActivityType.listening))


@bot.command()
async def p4(ctx):
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
        # print(videosSearch.result())
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
        while v_c.is_playing:
            await asyncio.sleep(1)
            videotitle = videotitle[1:] + videotitle[0]
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        # while v_c.is_playing():
        #     await sleep(1)
        # if not v_c.is_paused():
        #     await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Звук тишины", type=discord.ActivityType.listening))


@bot.command()
async def p5(ctx):
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
        # print(videosSearch.result())
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
        while v_c.is_playing:
            await asyncio.sleep(1)
            videotitle = videotitle[1:] + videotitle[0]
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
        # while v_c.is_playing():
        #     await sleep(1)
        # if not v_c.is_paused():
        #     await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Звук тишины", type=discord.ActivityType.listening))


@bot.command()
async def ok(ctx):  # Write-trigger bot 'ok'
    await command_dis.ok(ctx)


@bot.command()
async def radio(ctx):  # Radio list
    await command_dis.radio(ctx)


@bot.command()
async def Energy(ctx):  # Radio Energy
    await command_dis.redio_Energy(ctx, bot)


@bot.command()
async def Dacha(ctx):  # Radio Dacha
    await command_dis.redio_Dacha(ctx, bot)


@bot.command()
async def Evropa(ctx):  # Radio Evropa
    await command_dis.redio_Evropa(ctx, bot)


@bot.command()
async def join(ctx):  # Connect bot
    await command_dis.join(ctx)


@bot.command()
async def leave(ctx):  # Disconnect bot
    await command_dis.leave(ctx)


@bot.command()
async def stop(ctx):  # Stop music bot
    await command_dis.stop(ctx, bot)


@bot.command()
async def helping(ctx):  # Write-trigger bot
    await command_dis.helping(ctx)


bot.run('OTgxOTM0NzM1MDY2NTUwMzEy.GW_gVb.bdlkuj0_xH2wAGQSMrI595SDHcsy6xXHg8wORo')
