import random
import discord
from infraestructure.carbote.config import carbote
from infraestructure.datasource.airtable.client import airtable


embed_color=0xd10a07

@carbote.instance.command(name='cbm')
#the content will contain the question, which must be answerable with a set of three emojis
#that represent marry, kiss or kill options
async def marry_kiss_kill(ctx):
    print("Creating the marry kiss kill poll")
    #create the embed file
    #TODO: CHANGE IT FOR A CHANNEL MENTION LATER
    embed=discord.Embed(title=f"CASA, BEIJA OU MATA", description="Reaja com 👰 para CASA, 💋 para BEIJA e 💀 para MATA",  color=embed_color)
    #set the author and icon
    #   embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url) 
    print("Embed created")

    #send the embed 
    poll_title = await ctx.channel.send(embed=embed)

    #get options from airtable
    #https://airtable.com/app2No4LTWrc7lY7l/tblZCQiyCBh5v6HB6/viwo4B0Fdh5tf0rHK?blocks=hide
    cbm_table = airtable.api.all('app2No4LTWrc7lY7l', 'tblZCQiyCBh5v6HB6')   
    
    options = []
    #get random entry from db
    for _ in range(3):
        index = random.randint(1, len(cbm_table)+1)
        while cbm_table[index] in options:
            index = random.randint(1, len(cbm_table)+1)

        options.append(cbm_table[index])

    #mount option view
    for option in options:
        #create option message
        name=option['fields']['nome']
        embed_option=discord.Embed(description=f'{name}',  color=0xd10a07)
        
        #creates view as a section
        view = carbote.View()

        #creates buttons
        marry_button = carbote.Button(label = "Casa", emoji='👰' ,style=discord.ButtonStyle.green)
        kiss_button = carbote.Button(label = "Beija", emoji='💋', style=discord.ButtonStyle.gray)
        kill_button= carbote.Button(label = "Mata", emoji='💀', style=discord.ButtonStyle.red)

        #add react buttons
        view.add_item(marry_button)
        view.add_item(kiss_button)
        view.add_item(kill_button)

        #add callback to buttons
        async def marry_callback(interaction):
            await interaction.response.defer()
            await interaction.message.add_reaction("👰")
        async def kiss_callback(interaction):
            await interaction.response.defer()
            await interaction.message.add_reaction("💋")
        async def kill_callback(interaction):
            await interaction.response.defer()
            await interaction.message.add_reaction("💀")
        marry_button.callback = marry_callback
        kiss_button.callback = kiss_callback
        kill_button.callback = kill_callback

        #send message
        message = await ctx.channel.send(embed=embed_option, view=view)