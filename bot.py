import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio 
import logging

# === Load environment variables ===
load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

if not TOKEN or not CHANNEL_ID:
    raise ValueError("Missing TOKEN or CHANNEL_ID.")

# === Setup logs directory ===
os.makedirs("logs", exist_ok=True)

def log_event(log_type, message):
    file = "logs/security.log" if log_type == "security" else "logs/activity.log"
    with open(file, "a") as f:
        f.write(f"[{log_type.upper()}] {message}\n")

# === Initialize the bot with required intents ===
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# === Event: Bot is ready ===
@bot.event
async def on_ready():
    log_event("activity", f"Bot is connected as {bot.user}")

# === Event: Member joins a voice channel ===
@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == CHANNEL_ID:
        log_event("activity", f"{member} joined the monitored voice channel.")

        await asyncio.sleep(20)

        # Check if still in the same channel
        if member.voice and member.voice.channel and member.voice.channel.id == CHANNEL_ID:
            if member.voice.self_video:
                log_event("activity", f"{member} has camera ON. No action taken.")
            else:
                try:
                    await member.move_to(None)
                    log_event("activity", f"{member} was removed after 20 seconds with camera OFF.")

                    try:
                        await member.send(
                        "You were removed from the voice channel because you stayed longer than 20 seconds. "
                        "This channel is monitored and not intended for idle presence."

                        )
                        log_event("activity", f"DM sent to {member}.")
                    except discord.Forbidden:
                        log_event("security", f"Could not send DM to {member}.")
                    except Exception as e:
                        log_event("security", f"DM error to {member}: {e}")

                except Exception as e:
                    log_event("security", f"Failed to move {member}: {e}")

if __name__ == "__main__":
    bot.run(TOKEN)

