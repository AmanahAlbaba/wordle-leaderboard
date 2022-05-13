import pandas as pd
from nextcord.ext import commands
import os

class getStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def myStats (self, ctx):
        id = ctx.message.author.id
        try:
            df = pd.read_csv(str(id) + '.csv')
            totalScore = df['Score'].sum()
            days = df['Score'].count()
            avg = totalScore/days
            ranking = self.rank(id)
            await ctx.send(f"```Stats for {ctx.author.name} \nTotal Number of wordles played: " + str(days) + "\nTotal Number of Guesses: " + str(totalScore) + "\nAverage Number of Guesses: " + str(avg)  + "\nRanking: " + str(ranking) + "```")
        except OSError:
            await ctx.send("You do not have any plays yet")

    def calcAvg (self):
        ids = []
        avg = []
        for filename in os.listdir():
            if (filename.endswith(".csv")):
                df = pd.read_csv(filename)
                avg.append(df['Score'].sum()/df['Score'].count())
                ids.append(filename.split(".")[0])
        return ids, avg

    def rank(self, id):
        ids, avg = self.calcAvg()
        for i in range(len(avg)):
            swap = False
            for j in range(len(avg) - i - 1):
                if (avg[j] > avg[j+1]):
                    temp = avg[j]
                    avg[j] = avg[j+1]
                    avg[j+1] = temp
                    temp = ids[j]
                    ids[j] = ids[j+1]
                    ids[j+1] = temp
                    swap = True
            if (swap != True):
                break;
        for i in range (len(avg)):
            if (str(ids[i]) == str(id)):
                break

        return (i+1)

def setup(bot):
    bot.add_cog(getStats(bot))