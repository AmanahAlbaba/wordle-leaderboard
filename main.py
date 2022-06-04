import os
from nextcord.ext import commands
from keep_alive import keep_alive
my_secret = os.environ['TOKEN']
bot = commands.Bot(command_prefix="$")

bot.load_extension("cogs.setScore")
bot.load_extension("cogs.getStats")
bot.load_extension("cogs.getLeaderboard")
keep_alive()
bot.run(my_secret)

