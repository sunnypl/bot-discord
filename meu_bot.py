import discord
import os

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_member__join(self,member):
     guild = member.guild
     if guild.sytem_channel is not none:
     message = f'{member.mention} acabou de entra {guild.name} 
      await guild.sytem_channel.send(mensage)

 intents = discord.intents.default()
 intents.member = True


   async def on_message(self,message):
     print('Message from {0.author}:
{0.content}'format(message))
  if message.content == 'x!info':
  await message.channel.send(f'{message.author.name} informações do bot:{os.linesep} olá eu sou um bot!:{os.linesep} bot de moderação!:{os.linesep} bot de divulgação:{os.linesep} bot nuke e muito mas...')
client = MyClient(intents=intents)
client.run('MTAyMDM4MjUxNDc5NzM1MDkxMg.GMMJlY.HL4kwXO7_58FfVKD8KMqPFaK-fR-5Q_P1lMO2o')
