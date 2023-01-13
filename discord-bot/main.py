# 893494789830500432 client
# ODkzNDk0Nzg5ODMwNTAwNDMy.YVcR3g.tNd-FxRrYm0yNShLWBhdaVjB7Fg token
# 534790011712

import discord

from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

from discord.ext import commands
from datetime import date, datetime, timedelta


# wrapper / decorator

message_user_lastseen = datetime.now()
message_name_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!', help_command=None)

#client = discord.Client()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("you typed: {0}".format(par))


@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="Tutorial Bot help",description="All available commands", color=0x42f5a7)
    emBed.add_field(name="help", value="Get help command", inline=False)
    emBed.add_field(name="test", value="Respond message that you've send", inline=False)
    emBed.add_field(name="send", value="Send hello message to user", inline=False)
    emBed.set_thumbnail(url='https://seeklogo.com/images/D/discord-icon-new-2021-logo-09772BF096-seeklogo.com.png')
    emBed.set_footer(text='test footer', icon_url='https://seeklogo.com/images/D/discord-icon-new-2021-logo-09772BF096-seeklogo.com.png')
    await ctx.channel.send(embed=emBed)


@bot.command()
async def send(ctx):
    print(ctx.channel)
    await ctx.channel.send('Hello')


@bot.event  # async / await
async def on_message(message):
    global message_lastseen
    if message.content == '!user':
        await message.channel.send(str(message.author.name) + ': Hello')
    elif message.content == 'นายชื่ออะไร' and datetime.now() >= message_user_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('ฉันชื่อ ' + str(bot.user.name))
        print('{0} run นายชื่ออะไร {2} next time to use {2}' .format(message.author.name, datetime.now(), message_lastseen))
    elif message.content == 'ผมชื่ออะไร' and datetime.now() >= message_name_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('นายชื่อ ' + str(message.author.name))
    elif message.content == '!logout':
        await bot.logout()
        await bot.process_commands(message)


@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if voice_client == None:
        await ctx.channel.send("Joined")
        await channel.connect()

    YLD_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not voice_client.is_playing():
        with YoutubeDL(YLD_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice_client.is_playing()
    else:
        await ctx.channel.send("Already playing song")
        return


@bot.command()
async def stop(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("bot is not connected to vc")
        return
    
    voice_client.stop()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


bot.run('ODkzNDk0Nzg5ODMwNTAwNDMy.YVcR3g.tNd-FxRrYm0yNShLWBhdaVjB7Fg')
