import discord


class bot(discord.Client):
    async def on_ready(self):
        print("a")

    async def on_massage(self, massage):
        print("b")


client = bot()
client.run('OTgxOTM0NzM1MDY2NTUwMzEy.Gt4bvR.eJPHvYC3yqkC3Ggd_LkGJ1tVir2FDUnpCf92AA')
