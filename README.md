![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-2.3-lightgrey?logo=discord)
![Systemd](https://img.shields.io/badge/Service-systemd-brightgreen)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)


# Discord Cam Kick Bot  
Automatically enforce “camera-on” rules in Discord voice channels.

This bot monitors a specific voice channel and removes users who refuse to turn on their camera after a short grace period. It is designed for professional, educational, or moderated communities where on-camera presence is required.

---

## Features
- Detects users joining without a camera
- Gives a 20-second grace period
- Moves (kicks) non-compliant users out of the channel
- Supports whitelist roles that are never kicked
- Fully configurable through `.env`
- Activity & security logs
- Runs as a `systemd` service (auto-start & auto-restart)

---

### Instances Included in This Project

This repository powers **two official bot instances**:

* **Production bot** – runs exclusively on my community server.
* **Demo bot** – runs exclusively on a public test server for recruiters and developers.

Both use the same source code from this repository but operate on **separate tokens**, **separate environments**, and **separate servers**.

Invite URL for the production bot: [Production invite](https://discord.com/oauth2/authorize?client_id=1394511324431646870&permissions=17894400&integration_type=0&scope=bot)

---

## Official Demo Server

Demo Server: *(https://discord.gg/XRrC8EPsnC)*



### About The Demo Server

The demo server exists only to demonstrate the Discord Camera Kick Bot. It is just a demo environment, not a real community. No onboarding, no rules, no chat channels — only the bot in action.

To test the bot there:

- Join the cam-only voice channel


- Don't connect your CAM.


- The bot will automatically move you out after 20 seconds and send a message to you.


---


### About The Main Server(prints bellow):

The production bot is currently running in a production-grade Discord community (in construction), designed with:

- multi-language onboarding

- role-based access

- advanced permission architecture

- camera-on channels

- categories for data science, AI, and engineering

- professional server layout

(The main server is still private while being built).


<img src="prints/server.png" width="600">

<div style="display: flex; justify-content: space-around; align-items: flex-start;">
  <img src="prints/some channels.png" width="250" />
  <img src="prints/multilingue.png" width="250" />
  <img src="prints/some channels after choose.png" width="250" />
</div>




---

## Want to run this bot in your own server?

You absolutely can.

Just follow the installation steps in this README:

1. Create your own Discord Application
2. Add a Bot to it
3. Generate your bot token
4. Create a `.env` file based on the example
5. Install dependencies
6. Run it or deploy it as a service (systemd)

The architecture of this project was designed so that **anyone** can deploy their own instance safely.


---

## Installation (Developers)

1. Clone:
```
git clone https://github.com/celsomsilva/discord-cam-kick-bot.git
cd discord-cam-kick-bot
```

2. Optional venv:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install:
```
pip install -r requirements.txt
```

4. Configure `.env`
```
TOKEN=your_bot_token
CHANNEL_ID=your_target_voice_channel
WHITELIST_ROLE_IDS=your_list  example: 111111111,222222222
```

5. Test:
```
python3 bot.py
```

---


## systemd Service
Copy service:
```
sudo cp discordbot.service /etc/systemd/system/
```

Enable:
```
sudo systemctl daemon-reexec
sudo systemctl enable discordbot
sudo systemctl start discordbot
```

Logs:
```
journalctl -u discordbot -f
```

---


## Project Structure
```
discord-cam-kick-bot/
├── bot.py
├── .env.example
├── requirements.txt
├── discordbot.service
├── logs/
│   ├── activity.log
│   └── security.log
└── README.md
```

---


## Security
- No tokens hardcoded
- `.env` secrets
- Role hierarchy respected
- Safe logging	

---


## Author

This project was developed by an engineer and data scientist with a background in:

* Postgraduate degree in **Data Science and Analytics (USP)**
* Bachelor's degree in **Computer Engineering (UERJ)**
* Special interest in statistical models, interpretability, and applied AI

---

## Contact  

- [LinkedIn](https://linkedin.com/in/celso-m-silva)  
- Or open an [issue](https://github.com/celsomsilva/discord-cam-kick-bot/issues) 
