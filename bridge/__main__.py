import os
from dotenv import load_dotenv
from discordbridge import DiscordClient
from . import constants
constants.init()
load_dotenv()

# Run Discord Client
client = DiscordClient()
client.run(os.environ.get('DISCORD_BOT_TOKEN'))
__version__ = "1.0.0"