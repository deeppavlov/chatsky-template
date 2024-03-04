import logging

from bot.pipeline import pipeline


logging.basicConfig(level=logging.INFO)

pipeline.run()
