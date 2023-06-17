
from infraestructure.carbote.config import carbote

@carbote.instance.command(name='amor')
async def love(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}, eu só quero alguém pra amar...')

