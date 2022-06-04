import asyncio
from pickle import NONE
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import random
import youtube_dl
from discord.utils import get
import urllib.parse, urllib.request, re
from youtube_dl import YoutubeDL
from asyncio import sleep
import discord
from discord import ActivityType, Activity, FFmpegPCMAudio
from discord.ext import commands

global v_c
#
# intents = discord.Intents().all()
# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!', intents=intents)


bot = commands.Bot(command_prefix='>')
client = discord.Client()


@bot.event
async def on_ready():  # Start bot
    print('Bot connect')


@bot.command()
async def ok(ctx):  # Write-trigger bot
    await ctx.send('ok')


@bot.command()
async def radio(ctx):  # Radio-list bot
    channel = ctx.author.voice.channel
    await channel.connect()

    await ctx.send(" Radio-list:\n"
                   ">Energy\n"
                   ">Dacha\n"
                   ">Evropa\n")


@bot.command()
async def Energy(ctx):
    await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
    voice_channel = ctx.message.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    else:
        ctx.voice_client.stop()
    ctx.voice_client.play(FFmpegPCMAudio("https://pub0201.101.ru:8443/stream/air/mp3/256/99"), )


@bot.command()
async def Dacha(ctx):
    await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
    voice_channel = ctx.message.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    else:
        ctx.voice_client.stop()
    ctx.voice_client.play(FFmpegPCMAudio(
        "https://stream2.n340.com/12_dacha_28_reg_1093?type=.aac&UID=C21958B7AA80EA280465EA8518C6F363"), )


@bot.command()
async def Evropa(ctx):
    await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
    voice_channel = ctx.message.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    else:
        ctx.voice_client.stop()
    ctx.voice_client.play(FFmpegPCMAudio("https://ep256.hostingradio.ru:8052/europaplus256.mp3"), )


@bot.command()
async def NM(ctx):
    await bot.change_presence(activity=Activity(name="music", type=ActivityType.listening))
    voice_channel = ctx.message.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    else:
        ctx.voice_client.stop()
    ctx.voice_client.play(FFmpegPCMAudio("C:\\Music\\NM.mp3"), )


# YDL_OPTIONS = {'format': 'worstaudio/best',
#                'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
#                'key': 'FFmpegExtractAudio'}
YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'False', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
               'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


@bot.command()
async def play(ctx, *arg):  # Http ran
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

    URL = info['formats'][0]['url']

    v_c.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
    videotitle = info.get('title', 'Video   with ID: '+info.get('id', 'unknown'))
    await ctx.send(f"Playing {videotitle}")

    while v_c.is_playing():
        await sleep(1)
    # if not v_c.is_paused():
    # await v_c.disconnect()


@bot.command()
async def playr(ctx, arg):  # Http ran replay
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

    if v_c.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in arg:
                info = ydl.extract_info(arg, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]

        URL = info['formats'][0]['url']

        while True:
            v_c.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )
            while v_c.is_playing():
                await sleep(1)


@bot.command()
async def join(ctx):  # Connect bot
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):  # Disconnect bot
    await ctx.voice_client.disconnect()


@bot.command()
async def stop(ctx):  # Stop music bot
    ctx.voice_client.stop()


@bot.command()
async def helping(ctx):  # Write-trigger bot
    await ctx.send("Commands bot:\n"
                   ">helping - Помощь по командам\n"
                   ">radio - Список доступных радио волн\n"
                   ">play [URL]- Проигрывание песен по ссылки\n"
                   ">playr [URL]- Проигрывание песен по ссылки c повтороением\n"
                   ">join - Подключить бота к каналу\n"
                   ">leave - Отключить бота от канала\n"
                   ">stop - Остановить песню")



bot.run('OTgxOTM0NzM1MDY2NTUwMzEy.GW_gVb.bdlkuj0_xH2wAGQSMrI595SDHcsy6xXHg8wORo')
