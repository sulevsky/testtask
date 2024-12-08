import logging
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, UTC

logger = logging.getLogger(__name__)


@dataclass
class Report:
    longitude: float
    latitude: float
    target_description: str


def _to_cot_type(target_description: str) -> str:
    match target_description:
        case "tank":
            return "a-h-G-E-V-A-T"
        case "ifv":
            return "a-h-G-E-V-A"
        case "infantry":
            return "a-h-G-U-C-I"
        case _:
            logger.error(f"Unknown target description: {target_description}")
            return "a-h-G"


def to_cot(report: Report) -> str:
    now = datetime.now(tz=UTC)
    now_formated = now.isoformat() + "Z"
    stale_time = now + timedelta(hours=1)
    stale_formated = stale_time.isoformat() + "Z"
    message_id = str(uuid.uuid4())
    cot_type = _to_cot_type(report.target_description)
    return f"""
        <event version="2.0" 
               uid="{message_id}"
               type="{cot_type}"
               time="{now_formated}"
               start="{now_formated}" 
               stale="{stale_formated}" 
               how="h-g">
            <point lat="{report.latitude}" lon="{report.longitude}"/>
            <detail>
                <contact callsign="{report.target_description}"/>
            </detail>
        </event>
        """
