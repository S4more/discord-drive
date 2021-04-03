from discord.ext import commands, tasks
from drive import Drive
from configparser import ConfigParser
import sys
from video_downloader import VideoDownloader

config = ConfigParser()
config.read("bot.ini")

import os

bot = commands.Bot(command_prefix=('!salva '))
drive = Drive()
videoDownloader = VideoDownloader()

class Utils(commands.Cog):
    @commands.has_any_role('Tchola', 'Kapopeiro', 'New Tchola')
    @commands.command(pass_context=True, name="foto", brief="Guarda uma imagem no google drive")
    async def foto(self, ctx, *args):
        title = '_'.join(args[:-1])
        if 'http' in args[-1]:
            link = args[-1]

            if any(website in link for website in ['facebook', 'youtube']):
                ext = videoDownloader.download(link, title)
                title += f".{ext}"
            else:
                os.system(f"wget -O ./imgs/{title} {link}")

        else:
            try:
                link = ctx.message.attachments[0].url
                title = '_'.join(args)
                os.system(f"wget -O ./imgs/{title} {link}")
            except:
                await ctx.send("Alguma coisa deu errado")
                return;

        link = drive.upload_image(title, f"./imgs/{title}", ctx.author.name)
        os.system(f"rm ./imgs/{title}")
        await ctx.send(f"Foto salva com sucesso. Link: {link}")

#    @foto.error
#    async def foto_handler(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            if error.param.name == 'link':
#                await ctx.send("A sintaxe do comando esta errada. Usagem certa: `salva foto titulo link`")

    @commands.command(pass_context=True, name="link", brief="Manda o link para a pasta do google drive.")
    async def link(self, ctx):
        await ctx.send(drive.get_folder_link())


bot.add_cog(Utils())

if __name__ == '__main__':
    bot.run(config["BOT"]["TOKEN"])
