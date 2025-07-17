![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-2.3-lightgrey?logo=discord)
![Systemd](https://img.shields.io/badge/Service-systemd-brightgreen)
![License](https://img.shields.io/github/license/celsomsilva/discord-cam-kick-bot)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)


# Discord CAM Kick Bot


A Discord bot that makes sure your members follow the rules in video-only voice channels.

> This bot was created for the "AI Engineering, Data Science & Software Engineering Community" Discod server.  
> A place where voice channels will have **rules**, and cameras **must be on**.  
> Think of this bot as a bouncer equipped with a webcam detector.


---
## Features

- Monitors a specific voice channel
- Kicks users who don’t enable their camera in time (20 seconds)
- Sends a DM with a reason for the kick
- Runs as a `systemd` service (auto-start on boot)
- Secure `.env` file for token and config



---
## Why?

Some Discord servers have "camera-on" only channels.  
This bot helps enforce the rule — politely but firmly.



---
## Structure


```
discord-cam-kick-bot/
├── logs/
├── bot.py
├── .env.example
├── requirements.txt
├── discordbot.service
└── README.md
```


---
## How to use

1. Clone this repo:

```bash
git clone git@github.com:celsomsilva/discord-cam-kick-bot.git
cd discord-cam-kick-bot
```

2. Create a .env file (based on .env.example) and set your values:

```env
TOKEN=your_bot_token
CHANNEL_ID=your_voice_channel_id
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the bot manually:

```bash
python3 bot.py
```

Or set it up as a Linux service for auto-start on boot:

```bash
sudo cp discordbot.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable discordbot
sudo systemctl start discordbot
```
To check the status:

```bash
sudo systemctl status discordbot
```


---
##  Logs Directory

The bot creates logs inside a `logs/` folder:
- `activity.log` for general events
- `security.log` for permission issues or errors

> The folder is auto-created if it doesn't exist.  
> A `.gitkeep` placeholder is included to make sure it appears in this repository.


---
## Security


 - Secrets are never hardcoded

 - No tokens or user data are logged
 
 
 
--- 
## .env.example

```env
TOKEN=your_discord_bot_token
CHANNEL_ID=your_voice_channel_id
```

Never commit your real .env file. 



---
## Permissions

> **Important:** Remember that when developing a bot for Discord, the selected permissions must be carefully configured to ensure the bot works as intended.

For this bot to operate correctly, make sure it has the following permissions:

- **Connect** — to join voice channels  
- **Speak** — if you want it to play audio (optional)  
- **Move Members** — required to disconnect users from the voice channel  
- **View Channels** — to access the monitored channel    
- **Use Voice Activity / Use Camera** (optional)

> Within the server, you can restrict these permissions to specific channels by removing the bot role’s global permissions and enabling them only in the desired channels (but it will disappear from the members list).

> Minimal intents are included in the code.  
  If you want to add command handling or message reading, you'll need to enable additional intents and update the bot accordingly.


---
## About `discordbot.service` file in this repository

The `discordbot.service` is a systemd unit file that ensures your Discord bot runs as a background service on Linux systems.


### Purpose

Running your bot as a service provides:

- **Automatic start** at system boot.
- **Auto-restart** in case of failure.
- **Centralized logging** via `journalctl`.


### How to Use

1. Adjust the file and copy to `/etc/systemd/system/discordbot.service`
2. Reload systemd: `sudo systemctl daemon-reexec`
3. Enable the service: `sudo systemctl enable discordbot`
4. Start the bot: `sudo systemctl start discordbot`
5. Check status/logs: `sudo systemctl status discordbot` or `journalctl -u discordbot`



---
## Environment

- This guide assumes a Linux environment.  
  Windows users may adapt with WSL, but Linux is preferred for ease of use.

- Oracle Cloud’s Always Free instances(VM.Standard.E2.1.Micro), but **its use is not required**.


--- 
## License

MIT. Use it, fork it, break it, improve it. 


