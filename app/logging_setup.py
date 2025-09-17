import logging
import json
import sys
from datetime import datetime

class JsonLogFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "ts": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "msg": record.getMessage(),
            "request_id": getattr(record, "request_id", None),
            "module": record.module,
        }
        return json.dumps(log)

logger = logging.getLogger("askhr")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonLogFormatter())
logger.handlers = [handler]
logger.propagate = False
