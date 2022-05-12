from nextcord.ext import commands
from Key import TOKEN

bot = commands.Bot(command_prefix="$")

bot.load_extension("cogs.setScore")
bot.load_extension("cogs.getStats")
bot.load_extension("cogs.getLeaderboard")

bot.run(TOKEN)