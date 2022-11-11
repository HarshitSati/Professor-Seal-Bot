#this is not the production code
from platform import platform
import discord
import os
import dotenv
import random

dotenv.load_dotenv()
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='ps!')
@bot.event
async def on_ready():
  print('Logged in as {0.user} using Pycord!'.format(bot))
  await bot.change_presence(activity=discord.Streaming(platform = "YouTube",name="Study With Tina", url="https://www.youtube.com/watch?v=RLez2bI9Hb8"))


# @client.event #count the number users messaging and VC joins per day
# async def on_message(message):
#   if message.author == client.user:
#     return
#   username = str(message.author)
#   engagement_dict_text = {}
#   member_count=0
#   if username not in engagement_dict_text:
#     member_count =1
#   else:
#     member_count+=1
#   engagement_dict_text[username] = [member_count, message.author.id]
#   await message.channel.send(engagement_dict_text)
@bot.event #VC events
async def on_voice_state_update(member, before, after):

  joined_voice_channel = None
  if before.channel is None and after.channel is not None:
    joined_voice_channel = True
  else:
    joined_voice_channel = False
    
  guild = bot.get_guild(id=957099166855733328) #Server ID
  role = guild.get_role(role_id=957250432789545010) #"Focus mode ID"role ID
  workspace = 957099167300354110 #tortoise workspace ID

  if joined_voice_channel and after.channel.id == workspace:  #joining new vc 
    await member.add_roles(role)
  elif before.channel is not None and after.channel is None: # leaving vc 
    await member.remove_roles(role)
  elif before.channel is not None and after.channel.id ==workspace: # hopping to workspacce
    await member.add_roles(role)
  elif before.channel is not None and after.channel.id !=workspace: # hopping from workspace
    await member.remove_roles(role)
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  hype_emotes = ['<:pepeHypeDracula:966579300922966016>', '<:pepeHypeReal:965963373751709746>','<:doggie:970324310302531696>','<:dumbFuckJuice:960056015896866816>']
  if message.channel.id == 957099166855733333:
    await message.add_reaction(random.choice(hype_emotes))
  if message.channel.id == 957099166855733334:
    await message.add_reaction(random.choice(hype_emotes))

#to migrate to @has_permissions method
  allowed_members= [520984605587931157, 431294785676902400, 693066112111345727, 790789116128264192]
  if message.author.id in allowed_members and message.content.startswith('ps!say'):
    try:
      channel = bot.get_channel(int(message.content[-19:-1]))
      await channel.send(message.content[6:-21])  
    except:
       try:
        await message.channel.send(message.content[6:])  
       except:
        pass

@bot.event
async def on_member_join(member):
    channel =bot.get_channel(957099166855733333)
    await channel.send(f"> {member.mention} Welcome to the server 🌻!<:TinaHeyGuys:953824368927060008>\n\n> We usually use <#813485727400591440> to **chat** while **studying** in its accompanying VC (Voice channel) <#813199122999803924> and playing music.<a:DinoChuuHug:949349589587222578>\n> Some channels are invisible until you choose roles based on your preference. Please head over to <#964508901468946482> and react with the right emoji to access the concerned channels.<a:catjam:844846463027511296> \n> You can check <#932356697761148928> for more information or ask questions in <#810525582869266454> <:HeartTurtle:869132564902846515>.\n> Need help of server staff? Open a ticket through <#842121959722582066><a:dancedance:946373759282069514>")




#have to implement the joining various VCs feature
#TBD - Engagement metrics
bot.run(os.getenv('TOKEN'))

