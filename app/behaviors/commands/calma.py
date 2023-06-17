from infraestructure.carbote.config import carbote

@carbote.instance.command(name='calma')
async def calm_there_fuck(ctx):
    await ctx.channel.send(f'{ctx.channel.mention} CALMA LÁ, PORRA, CALMA LÁ')
    
