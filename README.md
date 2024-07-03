# Chatsky Project Template

This repository is a template for Chatsky projects.

## How to use it

### Clone the repo:

```shell
git clone https://github.com/deeppavlov/chatsky-template.git
cd chatsky-template
```

Alternatively, you can create a new repository using this one as a template via GitHub:

https://github.com/new?template_name=chatsky-template&template_owner=deeppavlov

### Edit project files

[0.] Install dependencies with
   ```shell
   (cd services/bot && pip install -r requirements.txt)
   ```
1. Write your custom functions (e.g. custom responses, custom services) into `bot/custom`.
2. Edit Chatsky script at `bot/script.py`.
3. Save Telegram bot token into `secrets/tg_token.txt`. (currently this template only supports telegram bots)

### Test the bot

#### With Python

```shell
(cd services/bot && pytest test.py)
```
#### With Docker

```shell
docker build --target test services/bot
```

### Run the bot

#### With Python

```shell
(export DB_URI="sqlite+aiosqlite:////$(pwd)/sqlite.db" TG_BOT_TOKEN_FILE="$(pwd)/secrets/tg_token.txt" && cd services/bot && python app.py)
```

#### With Docker Compose

```shell
docker compose up
```
