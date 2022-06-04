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
                await message.channel.send("Stop using irate")
            if (id == '181058833790009345'):
                await message.channel.send("Stop using thank")
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
                        await message.channel.send("You probably googled the answer but wanted to seem less sus so you got it in 3 :unamused:")
                    elif (score == '4'):
                        await message.channel.send("Your just average :yawning_face:")
                    elif (score == '5'):
                        await message.channel.send("Could've been worse :poop:")
                    elif (score== '6'):
                        await message.channel.send("engineers dont need english anyways :skull:")
                    elif (score == 7):
                        await message.channel.send("engineers dont need english anyways :skull:")
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