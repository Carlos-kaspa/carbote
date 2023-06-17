import discord
from infraestructure.carbote.config import carbote
from infraestructure.datasource.airtable.client import airtable

embed_color=0xd10a07

@carbote.instance.command(name='tchola_list')
async def tchola_list(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}, eu só quero alguém pra amar...')

@carbote.instance.command(name='tchola')
async def tchola_list(ctx):
    #creates view as a section
    view = carbote.View()
    emoji = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    embed_title=discord.Embed(title=f'{ctx.channel.mention}, de 0 a 10... quanto você é tchôla?',  color=embed_color)

    # get tchola_rank from airtable
    # https://airtable.com/app2No4LTWrc7lY7l/tblYdJESulHZ1s0IK/viwuyQzz3dNGBLnmU?blocks=hide
    tchola_table = airtable.get_table('app2No4LTWrc7lY7l', 'tblYdJESulHZ1s0IK')

    #creates buttons
    for index in range(0,11):
        button = carbote.Button(label =f'{index}', style=discord.ButtonStyle.gray, custom_id=f'{index}')
        async def button_callback(interaction):
            print(interaction.data['custom_id'])
            print(interaction.user)
            tchola_value=interaction.data['custom_id']
            await interaction.response.defer()
            await interaction.message.add_reaction(emoji[int(tchola_value)])
            tchola_table.create({
                'id_discord': f'{interaction.user}', 
                'rank': int(tchola_value)
            })
        button.callback=button_callback
        view.add_item(button)

    await ctx.channel.send(embed=embed_title, view=view)
