import os

from chatsky import Pipeline
from chatsky.context_storages import context_storage_factory
from chatsky.messengers.telegram import LongpollingInterface

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
    messenger_interface = LongpollingInterface(token=TG_BOT_TOKEN)


pipeline = Pipeline(
    script=script.SCRIPT,
    start_label=script.START_NODE,
    fallback_label=script.FALLBACK_NODE,
    pre_services=script.PRE_SERVICES,
    post_services=script.POST_SERVICES,
    context_storage=context_storage_factory(DB_URI) if DB_URI else None,
    messenger_interface=messenger_interface,
)
