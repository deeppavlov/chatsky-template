from dff.script import Message
from dff.script import RESPONSE, TRANSITIONS, LOCAL
from dff.script.conditions import exact_match, true

from .custom.conditions import is_upper_case
from .custom.services import pre_service, post_service


# todo: change this script to yours
SCRIPT = {
    "technical_flow": {
        "start_node": {
            TRANSITIONS: {
                ("main_flow", "greeting_node"): exact_match(Message("/start")),
            },
        },
        "fallback": {
            RESPONSE: Message("Error."),
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
            RESPONSE: Message("Hi, please say something."),
        },
        "upper": {
            RESPONSE: Message("Don't scream, please."),
        },
        "response": {
            RESPONSE: Message("Thank you."),
        },
    }
}

# todo: set pipeline parameters
START_NODE = ("technical_flow", "start_node")
FALLBACK_NODE = ("technical_flow", "fallback")

PRE_SERVICES = [pre_service]
POST_SERVICES = [post_service]
