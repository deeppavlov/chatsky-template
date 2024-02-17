from dff.script import Message
from dff.script import RESPONSE, TRANSITIONS, LOCAL
from dff.script.conditions import exact_match, true

from .custom.conditions import is_upper_case
from .custom.services import final_service


# todo: change this script to yours
SCRIPT = {
    "technical_flow": {
        "start_node": {
            TRANSITIONS: {
                ("main_flow", "greeting_node"): exact_match(Message(text="/start")),
            },
        },
        "fallback": {
            RESPONSE: Message(text="Error."),
        },
    },
    "main_flow": {
        LOCAL: {
            TRANSITIONS: {
                "upper": is_upper_case,
                "response": true(),
            },
        },
        "greeting_node": {
            RESPONSE: Message(text="Hi, please say something."),
        },
        "upper": {
            RESPONSE: Message(text="Don't scream, please."),
        },
        "response": {
            RESPONSE: Message(text="Thank you."),
        },
    }
}

# todo: set pipeline parameters
START_NODE = ("technical_flow", "start_node")
FALLBACK_NODE = ("technical_flow", "fallback")

PRE_SERVICES = [final_service]
POST_SERVICES = []
