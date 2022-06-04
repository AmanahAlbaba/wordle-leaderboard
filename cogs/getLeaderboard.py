import pandas as pd
from nextcord.ext import commands
import os

class getLeaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leaderboard(self, ctx):
        rankedIds, rankedAvg = self.rank()
        if len(rankedIds) != 0:
            await ctx.send("LeaderBoard - Average Number of Guesses")
            for i in range (len(rankedAvg)):
                await ctx.send(str(int(i)+1) + ". <@" + str(rankedIds[i]) + ">: " + str(rankedAvg[i]))
            if (rankedIds[0] == '698958117966315540'):
              await ctx.send("Even though you're 'first' Yusuf, you're not REALLY first because your sample size is so small. I'm sure you learned this in stats")
        else:
            await ctx.send("There are no scores yet")

    def calcAvg (self):
        ids = []
        avg = []
        for filename in os.listdir():
            if (filename.endswith(".csv")):
                df = pd.read_csv(filename)
                avg.append(df['Score'].sum()/df['Score'].count())
                ids.append(filename.split(".")[0])
        return ids, avg

    def rank(self):
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
        return ids, avg

def setup(bot):
    bot.add_cog(getLeaderboard(bot))