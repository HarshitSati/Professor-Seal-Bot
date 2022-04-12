from platform import platform
import discord
import os
import dotenv
client = discord.Client() 
dotenv.load_dotenv()
@client.event #Text events
async def on_ready():
  print('Logged in as {0.user} using Pycord!'.format(client))


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
@client.event #VC events
async def on_voice_state_update(member, before, after):

  joined_voice_channel = None
  if before.channel is None and after.channel is not None:
    joined_voice_channel = True
  else:
    joined_voice_channel = False
    
  guild = client.get_guild(id=957099166855733328) #Server ID
  role = guild.get_role(role_id=957250432789545010) #"ticket ID"role ID
  workspace = 957099167300354110 #tortoise workspace ID

  if joined_voice_channel and after.channel.id == workspace:  #joining new vc 
    await member.add_roles(role)
  elif before.channel is not None and after.channel is None: # leaving vc 
    await member.remove_roles(role)
  elif before.channel is not None and after.channel.id ==workspace: # hopping to workspacce
    await member.add_roles(role)
  elif before.channel is not None and after.channel.id !=workspace: # hopping from workspace
    await member.remove_roles(role)
  
#have to implement the joining various VCs feature
#TBD - Engagement metrics
client.run(os.getenv('TOKEN'))
