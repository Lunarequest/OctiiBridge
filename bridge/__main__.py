import os
from dotenv import load_dotenv
from discordbridge import DiscordClient
load_dotenv()

# Run Discord Client
client = DiscordClient()
client.run(os.environ.get('DISCORD_BOT_TOKEN'))
__version__ = "1.0.0"