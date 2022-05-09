from discord import FFmpegPCMAudio, Activity, ActivityType
from discord.ext.commands import Bot
import os
import keep_alive
bot = Bot(command_prefix="-", help_command=None)

@bot.event
async def on_ready() -> None:
    print(f"Бот {bot.user} успешно запущен.")
    await bot.change_presence(activity=Activity(name="музончик :3",  type=ActivityType.listening)) #статус бота (Слушает ... (действие в кавычках))

    voice_channel = bot.get_channel(940190057556488222) #айди голосового канала
    player = await voice_channel.connect()
    player.play(FFmpegPCMAudio("http://s02.fjperezdj.com:8006/live")) #ссылка на радио. Указывать в кавычках.
    
keep_alive.keep_alive()
bot.run("TOKEN")
