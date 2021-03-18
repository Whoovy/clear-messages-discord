#---CONFIG---

token = "TOKEN_HERE" 
prefix = "!" # 

#--- BOT ---

import discord
from discord.ext import commands

print("[Info] Logging into Discord")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("\n\n[Welcome] Ready! I await your command..") 
    print(f"[Welcome] Name: {bot.user.name}")
    print(f"[Welcome] ID: {bot.user.id}\n\n")

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"[Complete] Removed {passed} messages with {failed} fails")

bot.run(token, bot=False)
