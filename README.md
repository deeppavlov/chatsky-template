# Chatsky Project Template

This repository is a template for Chatsky projects.

The bot presented here is fully-functional with a very simple script that should
be overwritten with yours (more on that in the next section).

This bot uses SQLite to store dialog history. Refer to the [context storage tutorials](https://deeppavlov.github.io/chatsky/tutorials/index_context_storages.html)
if you'd like to use a different DB engine.

This bot uses Telegram as an interface. Refer to the [interface tutorials](https://deeppavlov.github.io/chatsky/tutorials/index_interfaces.html)
if you'd like to use different means of communicating.

## How to use

### [Step 0] System requirements

1. A unix system (e.g. Ubuntu 22.04) is recommended. Although both Chatsky and this template
    support other systems such as Windows, the instructions below are for unix systems.
2. [Git](https://git-scm.com/downloads) to clone this repository.
3. |Option 1| [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
   if you want to run the bot inside a docker container.
4. |Option 2| [Python 3.9+](https://www.python.org/downloads/) if you don't want to use docker.

### [Step 1] Clone the repo

```shell
git clone https://github.com/deeppavlov/chatsky-template.git
cd chatsky-template
```

Alternatively, you can create a new repository using this one as a template via GitHub:

https://github.com/new?template_name=chatsky-template&template_owner=deeppavlov

### [Step 2] Edit project files

1. Write your custom functions (e.g. custom responses, custom services) into `services/bot/bot/custom`.
2. Edit Chatsky script at `services/bot/bot/script.py`.
3. Save Telegram bot token into `secrets/tg_token.txt`.

### [Step 3] Test the bot

#### With Python

First, move to the bot directory:

```shell
cd services/bot
```

Next, install project dependencies:

```shell
pip install -r requirements.txt
```

Finally, run tests:

```shell
pytest test.py
```

#### With Docker

```shell
docker build --target test services/bot
```

### [Step 4] Run the bot

#### With Python

First, you need to be in the root directory of the project.

If you've done the previous step, run
```shell
cd ../..
```
to return from the `services/bot` directory.

Next, install project dependencies (if you haven't done so yet):

```shell
(cd services/bot && pip install -r requirements.txt)
```

Deploy the bot to telegram with:

```shell
(export DB_URI="sqlite+aiosqlite:////$(pwd)/sqlite.db" TG_BOT_TOKEN_FILE="$(pwd)/secrets/tg_token.txt" && cd services/bot && python app.py)
```

#### With Docker Compose

```shell
docker compose up
```
