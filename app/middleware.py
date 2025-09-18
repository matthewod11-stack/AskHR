import time, uuid, logging
from starlette.middleware.base import BaseHTTPMiddleware
from .error_utils import get_request_id

class RequestIdLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        rid = get_request_id(dict(request.headers)) or str(uuid.uuid4())
        # expose the id to handlers and echo it back in the response
        request.state.request_id = rid
        start = time.time()
        try:
            response = await call_next(request)
        finally:
            dur = int((time.time() - start) * 1000)
            logging.getLogger("askhr").info(
                f"{request.method} {request.url.path} {dur}ms",
                extra={"request_id": rid},
            )
        response.headers["X-Request-ID"] = rid
        return response
