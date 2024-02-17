import os

from dff.pipeline import Pipeline
from dff.context_storages import context_storage_factory
from dff.messengers.telegram import PollingTelegramInterface

from . import script


def get_variable(var_name: str):
    secret_file = os.getenv(var_name + "_FILE")
    env_var = os.getenv(var_name)
    if secret_file is not None:
        with open(secret_file, "r") as fd:
            return fd.read()
    return env_var


DB_URI = get_variable("DB_URI")

TG_BOT_TOKEN = get_variable("TG_BOT_TOKEN")


messenger_interface = None

if TG_BOT_TOKEN is not None:
    messenger_interface = PollingTelegramInterface(token=TG_BOT_TOKEN)


pipeline = Pipeline.from_script(
    getattr(script, "SCRIPT"),
    start_label=getattr(script, "START_NODE"),
    fallback_label=getattr(script, "FALLBACK_NODE", None),
    pre_services=getattr(script, "PRE_SERVICES", []),
    post_services=getattr(script, "POST_SERVICES", []),
    context_storage=context_storage_factory(DB_URI) if DB_URI else None,
    messenger_interface=messenger_interface,
)
