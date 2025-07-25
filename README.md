![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-2.3-lightgrey?logo=discord)
![Systemd](https://img.shields.io/badge/Service-systemd-brightgreen)
![License](https://img.shields.io/github/license/celsomsilva/discord-cam-kick-bot)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)


# Discord cam Kick Bot


A Discord bot that makes sure your members follow the rules in cam-only voice channels.

> This bot was created for the "AI Engineering, Data Science & Software Engineering Community" Discod server.  
> A place where voice channels will have **rules**, and cameras **must be on**.  
> Think of this bot as a bouncer equipped with a webcam detector.


---
## Features

- Monitors a specific voice channel
- Kicks users who don’t enable their camera in time (20 seconds) — **except for users with a specific role**
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
## Notes

- Make sure the bot has permission to move members out of the voice channel.
- The bot’s role must be **higher** than the roles of users it may need to remove, **except for users with a specific role**.
- The bot does **not** ban or kick from the server — only removes from the voice channel.



---
## How to use

1. Clone this repo:

```bash
git clone git@github.com:celsomsilva/discord-cam-kick-bot.git
cd discord-cam-kick-bot
```

2. Create a virtual environment (optional, but recommended)

Using `venv` ensures your dependencies are isolated and do not interfere with other Python projects.

```bash
python3 -m venv venv
source venv/bin/activate 
```

3. Create a .env file (based on .env.example) and set your values:

```env
TOKEN=your_discord_bot_token
CHANNEL_ID=123456789012345678
WHITELIST_ROLE_IDS=1234567890,9876543210
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the bot manually:

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

### .env.example

```env
TOKEN=your_discord_bot_token
CHANNEL_ID=your_voice_channel_id
WHITELIST_ROLE_IDS= your white list
```

Never commit your real .env file. 

---
##  Logs Directory

The bot creates logs inside a `logs/` folder:
- `activity.log` for general events
- `security.log` for permission issues or errors

> The folder is auto-created if it doesn't exist.  
> A `.gitkeep` placeholder is included to make sure it appears in this repository.


---
## Security

 - Secrets are never hardcoded:
All sensitive information such as bot tokens, API keys, and channel or role IDs are loaded securely from environment variables (.env), never stored directly in the source code or repository.

 - No tokens or user data are logged:
The bot does not log sensitive tokens or personal user data. Only relevant activity and security events (e.g., unauthorized access attempts, permission errors) are logged in a controlled manner to support auditing and debugging.

 - Role-based whitelist for protected members:
To prevent accidental or malicious removal of privileged users (e.g., admins, moderators), the bot uses a whitelist based on role IDs. This ensures that users with certain roles are immune from kick or move actions.

 - Permission checks respecting Discord hierarchy:
Before attempting to move or kick a member, the bot verifies the Discord role hierarchy and permission levels, ensuring it cannot perform actions on users with higher or equal permissions.

 - Limited scope of actions:
The bot only performs actions within a specific monitored voice channel, minimizing the risk of unintended behavior elsewhere in the server.

 - Error handling and logging:
All permission errors and exceptions are caught and logged safely without exposing sensitive information.



---
## Permissions

> **Important:** Remember that when developing a bot for Discord, the selected permissions must be carefully configured to ensure the bot works as intended.

For this bot to operate correctly, make sure it has the following permissions:

- **Connect** — to join voice channels  
- **Speak** — if you want it to play audio (optional)  
- **Move Members** — required to disconnect users from the voice channel  
- **View Channels** — to access the monitored channel    
- **Use Voice Activity / Use Camera** (optional)

Within the server, you can restrict these permissions to specific channels by removing the bot role’s global permissions and enabling them only in the desired channels (but it will disappear from the members list).

Minimal intents are included in the code.  
 If you want to add command handling or message reading, you'll need to enable additional intents and update the bot accordingly.

> To avoid using powerful roles like `Admin` or `Moderator` in the whitelist, you can create a harmless role (e.g., `basic role`) with no special permissions and assign it to trusted users.  
The bot will recognize them and **won’t remove them**, even if the camera is off.


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


