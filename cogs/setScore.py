from nextcord.ext import commands
import csv
import os
class setScore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        id=None
        if ('Wordle' in message.content and '/' in message.content):
            id = str(message.author.id)
            if (id == '698958117966315540'):
                await message.channel.send("You got lucky")

            for i in range (len(message.content)):
                if(message.content[i]=='/'):
                    score = message.content[i-1]
                    if (score == 'X'):
                        score = 7
                    if (score == '1'):
                        await message.channel.send("You definitely cheated :neutral_face:")
                    elif (score == '2'):
                        await message.channel.send("A bit sus :face_with_raised_eyebrow:")
                    elif (score == '3'):
                        await message.channel.send("Bruh :unamused:")
                    elif (score == '4'):
                        await message.channel.send("You did the bare minimum :yawning_face:")
                    elif (score == '5'):
                        await message.channel.send("At least you didn't get it in 6 :poop:")
                    elif (score== '6'):
                        await message.channel.send("L :clown:")
                    elif (score == 7):
                        await message.channel.send("RIP you suck :skull:")
                    break
            for file in os.listdir():
                if(file == str(id) + ".csv"):
                    temp = 1
                    break
                else:
                    temp = 0
            if temp==0:
                with open(str(id) + '.csv', 'a') as csvfile:
                    filewriter = csv.writer(csvfile)
                    filewriter.writerow(['Score'])
                    filewriter.writerow([score])
            else:
                with open(str(id) + '.csv', 'a') as csvfile:
                    filewriter = csv.writer(csvfile)
                    filewriter.writerow([score])

def setup(bot):
    bot.add_cog(setScore(bot))