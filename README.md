# DFF Project Template

This repository is a template for DFF projects.

## How to use it

### Clone the repo:

```commandline
git clone https://github.com/deeppavlov/DFF-template.git
cd DFF-template
```

Alternatively, you can create a new repository using this one as a template via GitHub:

https://github.com/new?template_name=DFF-template&template_owner=deeppavlov

### Edit project files

[0.] Install dependencies with
   ```commandline
   pip install -r requirements.txt
   ```
1. Write your custom functions (e.g. custom responses, custom services) into `bot/custom`.
2. Edit DFF script at `bot/script.py`.
3. Save Telegram bot token into `secrets/tg_token.txt`. (currently this template only supports telegram bots)

### Test the bot

#### With Python

```commandline
pytest test.py
```
#### With Docker

```commandline
docker build --target test .
```

### Run the bot

#### With Python

```commandline
DB_URI="sqlite+aiosqlite:////$(pwd)/sqlite.db" TG_BOT_TOKEN_FILE="secrets/tg_token.txt" python app.py
```

#### With Docker

```commandline
docker compose up
```
