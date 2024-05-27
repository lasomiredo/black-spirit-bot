import os, asyncio
import config
import discord
from discord.ext import commands
from discord.app_commands import Choice


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")


@bot.tree.command(name = "extension", description="load/unload/reload extension")
@discord.app_commands.describe(action="select the action", extension_name="input extension's name")
@discord.app_commands.choices(
    action=[
        Choice(name="load extension", value="load"),
        Choice(name="unload extension", value="unload"),
        Choice(name="reload extension", value="reload")
    ]
)
async def extension_action(interaction: discord.Interaction, action:str, extension_name: str):
    match action:
        case "load":
            await bot.load_extension(f"cogs.{extension_name}")
            await interaction.response.send_message(f"cogs.{extension_name} has been loaded.")
        case "unload":
            await bot.unload_extension(f"cogs.{extension_name}")
            await interaction.response.send_message(f"cogs.{extension_name} has been unloaded.")
        case "reload":
            await bot.reload_extension(f"cogs.{extension_name}")
            await interaction.response.send_message(f"cogs.{extension_name} has been reloaded.")


async def load_extensions():
    for root, dirs, files in os.walk(".\cogs"):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        # for dir_name in dirs:
        #     print(os.path.join(root, dir_name))
        for file_name in files:
            file_name = (os.path.join(root, file_name))
            if file_name.endswith(".py"):
                file_name = file_name.lstrip(".").rstrip(".py").replace("\\", ".")
                await bot.load_extension(file_name)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(config.DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
