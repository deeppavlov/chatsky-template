import logging

logger = logging.getLogger(__name__)


def pre_service(ctx):
    logger.info(f"starting processing request from {ctx.id}")
    logger.debug(str(ctx.last_request))


def post_service(ctx):
    logger.info("turn is over")
    logger.debug(str(ctx.last_response))
