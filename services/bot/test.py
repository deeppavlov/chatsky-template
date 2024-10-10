from json import load
from pathlib import Path

from chatsky.utils.testing import check_happy_path
import pytest


TEST_DATA_FILE = Path(__file__).parent / "test_data.json"

with open(TEST_DATA_FILE, "r") as fd:
    TEST_DATA = load(fd)["test_script"]


TEST_CASES = list(TEST_DATA.keys())
assert len(TEST_CASES) == 3


@pytest.mark.parametrize(
    "happy_path", TEST_CASES
)
def test_happy_paths(happy_path: str, monkeypatch):
    monkeypatch.delenv("TG_BOT_TOKEN_FILE", raising=False)
    monkeypatch.delenv("TG_BOT_TOKEN", raising=False)
    monkeypatch.delenv("DB_URI", raising=False)

    from .bot.pipeline import pipeline

    check_happy_path(pipeline, TEST_DATA[happy_path])
