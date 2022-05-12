import pandas as pd
from nextcord.ext import commands
class getStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def myStats (self, ctx):
        totalScore = 0
        days = 0
        id = ctx.message.author.id
        try:
            df = pd.read_csv(str(id) + '.csv')
            totalScore = df['Score'].sum()
            days = df['Score'].count()
            avg = totalScore/days
            await ctx.send(f"```Stats for {ctx.author.name} \nTotal Number of wordles played: " + str(days) + "\nTotal Number of Guesses: " + str(totalScore) + "\nAverage Number of Guesses: " + str(avg) + "```")
        except OSError:
            await ctx.send("You do not have any plays yet")
def setup(bot):
    bot.add_cog(getStats(bot))