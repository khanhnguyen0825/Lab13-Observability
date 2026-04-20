from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()

if os.getenv("LANGFUSE_BASE_URL") and not os.getenv("LANGFUSE_HOST"):
    os.environ["LANGFUSE_HOST"] = os.environ["LANGFUSE_BASE_URL"]

try:
    from langfuse import get_client, observe

    _langfuse_client = get_client()

    class _LangfuseContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            _langfuse_client.update_current_trace(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            _langfuse_client.update_current_span(**kwargs)

    langfuse_context = _LangfuseContext()
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

    langfuse_context = _DummyContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY"))
