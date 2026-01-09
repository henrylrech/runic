import discord
from discord.ext import commands
from handlers import roll, is_valid_expression
from secret import TOKEN

def run_bot():
    bot = commands.Bot(command_prefix='*', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f'{bot.user} is running!')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        if is_valid_expression(message.content):
            result = roll(message.content)
            if result is not None:
                await message.channel.send(result)

        await bot.process_commands(message)

    bot.run(TOKEN, log_handler=None)
