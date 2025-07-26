import discord
from discord.ext import commands
import os
from fastapi import FastAPI
import uvicorn
import asyncio

app = FastAPI()
@app.get("/health")
async def health():
    return {"status": "ok"}

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！ボット稼働中！")

async def main():
    config = uvicorn.Config(app, host="0.0.0.0", port=8080, log_level="info")
    server = uvicorn.Server(config)
    await asyncio.gather(server.serve(), bot.start(os.getenv("DISCORD_TOKEN")))

if __name__ == "__main__":
    asyncio.run(main())