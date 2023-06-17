
from app.infraestructure.carbote.config import Carbote


@Carbote.event
async def on_ready():
    print(f'We have logged in as {Carbote.user}')