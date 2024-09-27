from chatsky import Message, RESPONSE, TRANSITIONS, LOCAL, Transition as Tr
import chatsky.conditions as cnd

from .custom.conditions import IsUpperCase
from .custom.services import pre_service, post_service


# todo: change this script to yours
SCRIPT = {
    "technical_flow": {
        "start_node": {
            TRANSITIONS: [
                Tr(
                    dst=("main_flow", "greeting_node"),
                    cnd=cnd.ExactMatch("/start")
                )
            ],
        },
        "fallback": {
            RESPONSE: "Error.",
        },
    },
    "main_flow": {
        LOCAL: {
            TRANSITIONS: [
                Tr(
                    dst="upper",
                    cnd=IsUpperCase()
                ),
                Tr(
                    dst="response",
                )
            ]
        },
        "greeting_node": {
            RESPONSE: "Hi, please say something.",
        },
        "upper": {
            RESPONSE: "Don't scream, please.",
        },
        "response": {
            RESPONSE: "Thank you.",
        },
    }
}

# todo: set pipeline parameters
START_NODE = ("technical_flow", "start_node")
FALLBACK_NODE = ("technical_flow", "fallback")

PRE_SERVICES = [pre_service]
POST_SERVICES = [post_service]
