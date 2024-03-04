from json import load
from pathlib import Path

from dff.utils.testing import check_happy_path
from dff.script import Message
import pytest

from .bot.pipeline import pipeline


TEST_DATA_FILE = Path(__file__).parent / "test_data.json"

with open(TEST_DATA_FILE, "r") as fd:
    TEST_DATA = load(fd)["test_script"]


TEST_CASES = list(TEST_DATA.keys())
assert len(TEST_CASES) == 3


@pytest.mark.parametrize(
    "happy_path", TEST_CASES
)
def test_happy_paths(happy_path: str):
    check_happy_path(pipeline, tuple(map(lambda l: (Message(text=l[0]), Message(text=l[1])), TEST_DATA[happy_path])))
