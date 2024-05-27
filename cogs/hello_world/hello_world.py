import discord
from discord import app_commands
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "hello", description = "hello world")
    async def hello(self, interaction: discord.Interaction):
        # 回覆使用者的訊息
        await interaction.response.send_message("hello world!")



# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))