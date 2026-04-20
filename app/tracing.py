from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()

if os.getenv("LANGFUSE_BASE_URL") and not os.getenv("LANGFUSE_HOST"):
    os.environ["LANGFUSE_HOST"] = os.environ["LANGFUSE_BASE_URL"]

try:
    from langfuse.decorators import observe, langfuse_context
except Exception:  # pragma: no cover

    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func

        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            pass

        def update_current_observation(self, **kwargs: Any) -> None:
            pass

    langfuse_context = _DummyContext()
    propagate_attributes = None


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY"))
