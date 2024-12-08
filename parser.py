import logging

from cot_seriliazer import Report

logger = logging.getLogger(__name__)


def parse_message(text: str | None) -> Report | str:
    if text is None:
        return "Message is empty"
    sanitized = text.strip()
    if text is None:
        return "Message is empty"
    spilt = sanitized.split(" ")
    if len(spilt) != 3:
        logger.info(f"Invalid message, not all parts: {sanitized}")
        return "Invalid message, must be 3 parts"
    longitude = try_to_float(spilt[0].strip())
    if longitude is None:
        logger.info(f"Invalid message, not valid longitude: {sanitized}")
        return "Invalid message, not valid longitude"
    latitude = try_to_float(spilt[1].strip())
    if latitude is None:
        logger.info(f"Invalid message, not valid latitude: {sanitized}")
        return "Invalid message, not valid latitude"

    target_target_description = spilt[2].strip().lower()
    if len(target_target_description) == 0:
        logger.info(f"Invalid message, not valid target_description: {sanitized}")
        return "Invalid message, not valid target_description"
    return Report(longitude, latitude, target_target_description)


def try_to_float(text: str) -> float | None:
    try:
        return float(text)
    except ValueError:
        return None
