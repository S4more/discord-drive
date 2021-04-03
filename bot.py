from discord.ext import commands, tasks
from drive import Drive
from configparser import ConfigParser

config = ConfigParser()
config.read("bot.ini")

import os

bot = commands.Bot(command_prefix=('!salva '))
drive = Drive()

@bot.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return

class Utils(commands.Cog):
    @commands.command(pass_context=True, name="foto", brief="Guarda uma imagem no google drive")
    async def foto(self, ctx, *args):
        title = '_'.join(args[:-1])
        os.system(f"wget -O ./imgs/{title} {args[-1]}")
        link = drive.upload_image(title, f"./imgs/{title}", ctx.author.name)
        os.system(f"rm ./imgs/{title}")
        await ctx.send(f"Foto salva com sucesso. Link: {link}")

    @foto.error
    async def foto_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'link':
                await ctx.send("A sintaxe do comando esta errada. Usagem certa: `salva foto titulo link`")

    @commands.command(pass_context=True, name="link", brief="Manda o link para a pasta do google drive.")
    async def link(self, ctx):
        await ctx.send(drive.get_folder_link())


bot.add_cog(Utils())

bot.run(config["BOT"]["TOKEN"])
