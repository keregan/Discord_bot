import asyncio
import random
from asyncio import sleep
from dataclasses import replace
import ffmpeg
import discord
import requests
from bs4 import BeautifulSoup as BS, BeautifulSoup
from discord import ActivityType, Activity, FFmpegPCMAudio
from discord.ext import commands
from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch

global v_c, play_list, stoping
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
# Test: 982160360897396736
# News: 982738188911132683

play_list = []
stoping = []
bot_command = commands.Bot(command_prefix='>')
client = discord.Client()

YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
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


async def epic_games(bot):
    channel = bot.get_channel(982738188911132683)
    vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
    vk_ver = "5.131"
    domain = "-198731846"

    reponse = requests.get('https://api.vk.com/method/wall.get',
                           params={
                               'access_token': vk_pars,
                               'v': vk_ver,
                               'owner_id': domain,
                               'count': 1,
                               'offset': 1
                           }
                           )
    data = reponse.json()['response']['items']
    for post in data:
        try:
            text_post = post['text']
        except:
            text_post = 'pass'

    messages = await channel.history(limit=500).flatten()
    i = 0
    for msg in messages:
        if msg.content == text_post:
            no_post_2 = 0
            break
        else:
            no_post_2 = 1
    if no_post_2 == 1:
        await channel.send(text_post)


async def free_game(bot):
    channel = bot.get_channel(982738188911132683)
    vk_pars = "133a17f4133a17f4133a17f4421346fe9c1133a133a17f471a7b0c5bcca6560b561d7f0"
    vk_ver = "5.131"
    domain = "frexgames"

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
        try:
            text_post = post['text']
        except:
            text_post = ''
        try:
            img_post = post['attachments'][0]['photo']['sizes'][-1]['url']
        except:
            img_post = ''
    messages = await channel.history(limit=500).flatten()
    i = 0
    for msg in messages:
        if msg.content == text_post:
            no_post_2 = 0
            break
        else:
            no_post_2 = 1
    if no_post_2 == 1:
        await channel.send(text_post)
        await channel.send(img_post)


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

            messages = await channel.history(limit=600).flatten()
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


async def play_list_music(ctx):
    v_c = ctx.channel.guild.voice_client
    if v_c != True:
        print("a")
    else:
        print("b")


@bot_command.command()  # Massage
async def ok(ctx):  # return answer
    await ctx.send('ok')


@bot_command.command()  # Music
async def play(ctx, arg, bot):  # Http ran
    arg = str(arg).replace("(", "")
    arg = str(arg).replace(')', '')
    arg = str(arg).replace(',', '')
    arg = str(arg).replace("'", "")
    voice_channel = ctx.message.author.voice.channel
    v_c = ctx.channel.guild.voice_client
    if v_c is None:
        v_c = await voice_channel.connect()

    play_list.append(arg)

    while v_c.is_playing():
        print(play_list)
        await sleep(5)
    with YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.cache.remove()
        if 'https://' in arg:
            info = ydl.extract_info(play_list[0], download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{play_list[0]}", download=False)['entries'][0]
    videotitle = info.get('title')
    URL = info['formats'][0]['url']
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
    v_c.play(discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS), )  # after="play_next_song"
    videotitle = info.get('title', 'Video   with ID: ' + info.get('id', 'unknown'))
    await ctx.send(f"Playing {videotitle}")
    videotitle = videotitle + "       "
    play_list.pop(0)

    while v_c.is_playing:
        await asyncio.sleep(1)
        videotitle = videotitle[1:] + videotitle[0]
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=videotitle, type=discord.ActivityType.listening))
    while v_c.is_playing():
        await sleep(1)
    if not v_c.is_paused():
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Звук тишины", type=discord.ActivityType.listening))


async def pause(ctx):
    voice_client = ctx.channel.guild.voice_client
    if voice_client.is_playing():
        stoping = play_list.copy()
        play_list.clear()
        voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


async def stop(ctx, bot):
    voice_client = ctx.channel.guild.voice_client
    if voice_client.is_playing():
        play_list.clear()
        voice_client.stop()

        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Activity(name="Звуки тишины", type=discord.ActivityType.listening))
    else:
        await ctx.send("Бот и так молчит")


async def resume(ctx):
    voice_client = ctx.channel.guild.voice_client
    if voice_client.is_paused():
        play_list = stoping.copy()
        stoping.clear()
        await voice_client.resume()
    else:
        await ctx.send("Пауза - это святое")


async def skip(ctx, bot):
    voice_client = ctx.message.guild.voice_client
    print(play_list[0])
    if len(play_list) != 0:
        await ctx.send("Плейлист не пуст")
        # self.skip_votes.clear()
    else:
        await ctx.send("Плейлист пуст")
        # self.skip_votes.clear()


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


async def helping(ctx):  # Write-trigger bot
    await ctx.send("Commands bot:\n"
                   ">helping - Помощь по командам\n"
                   ">radio - Список доступных радио волн\n"
                   ">play [URL]- Проигрывание песен по ссылки\n"
                   ">playr [URL]- Проигрывание песен по ссылки c повтороением\n"
                   ">join - Подключить бота к каналу\n"
                   ">leave - Отключить бота от канала\n"
                   ">stop - Остановить песню")

