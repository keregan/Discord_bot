import asyncio
import random
import discord
from discord.ext import commands

import command_dis

bot = commands.Bot(command_prefix='>')
client = discord.Client()

YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'False', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
               'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

global v_c


def main():
    @bot.event
    async def on_ready():  # Start bot
        print('Bot connect')
        # while True:
        #     await command_dis.free_game(bot)
        #
        #     # await command_dis.news_stopgame(bot)  # StopGame news
        #     await asyncio.sleep(1)
        #     await command_dis.news_genshinimpact(bot)  # GenshinImpact news
        #     await asyncio.sleep(1)
        #     await command_dis.genshin_hub(bot)  # GenshinImpact art
        #     await asyncio.sleep(1)
        #     await command_dis.genshin_giarts(bot)  # GenshinImpact art
        #     await asyncio.sleep(1)
        #     await command_dis.promo_genshinimpact(bot)
        #     await asyncio.sleep(1)
        #     await command_dis.epic_games(bot)
        #     random_poss = random.randint(55, 180)
        #     await asyncio.sleep(random_poss)

    @bot.command()
    async def stop(ctx):
        await command_dis.stop(ctx, bot)

    @bot.command()
    async def skip(ctx):
        await command_dis.skip(ctx)

    @bot.command()
    async def pause(ctx):
        await command_dis.pause(ctx)

    @bot.command()
    async def resume(ctx):
        await command_dis.resume(ctx)

    @bot.command()
    async def p(ctx, *arg):
        await command_dis.play(ctx, arg, bot)

    @bot.command()
    async def y(ctx, *arg):  # Youtube_list
        await command_dis.youtube_list(ctx, arg)

    @bot.command()
    async def p1(ctx):
        await command_dis.youtube_p1(ctx, bot)

    @bot.command()
    async def p2(ctx):
        await command_dis.youtube_p2(ctx, bot)

    @bot.command()
    async def p3(ctx):
        await command_dis.youtube_p3(ctx, bot)

    @bot.command()
    async def p4(ctx):
        await command_dis.youtube_p4(ctx, bot)

    @bot.command()
    async def p5(ctx):
        await command_dis.youtube_p5(ctx, bot)

    @bot.command()
    async def o(ctx):  # Write-trigger bot 'ok'
        await command_dis.o(ctx)

    @bot.command()
    async def join(ctx):  # Connect bot
        await command_dis.join(ctx, bot)

    @bot.command()
    async def leave(ctx):  # Disconnect bot
        await command_dis.leave(ctx, bot)

    @bot.command()
    async def helping(ctx):  # Write-trigger bot
        await command_dis.helping(ctx)


if __name__ == '__main__':
    main()
bot.run('OTgxOTM0NzM1MDY2NTUwMzEy.GYP2_i._iB6UWT2zepdC4LOPboN2xdW2X93umRajS6VuA')
