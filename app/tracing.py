from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()

# Map BASE_URL to HOST for Langfuse SDK
if os.getenv("LANGFUSE_BASE_URL") and not os.getenv("LANGFUSE_HOST"):
    os.environ["LANGFUSE_HOST"] = os.environ["LANGFUSE_BASE_URL"]

try:
    from langfuse import observe, get_client, propagate_attributes
    langfuse_client = get_client()

    class _LangfuseContextV4:
        def update_current_trace(self, **kwargs: Any) -> None:
            # v4 uses update_current_span for these attributes if not using propagate_attributes
            langfuse_client.update_current_span(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            if "usage" in kwargs:
                kwargs["usage_details"] = kwargs.pop("usage")
            
            # Use generation update if usage is provided
            if "usage_details" in kwargs or "model" in kwargs:
                langfuse_client.update_current_generation(**kwargs)
            else:
                langfuse_client.update_current_span(**kwargs)

    langfuse_context = _LangfuseContextV4()

except ImportError:
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None: pass
        def update_current_observation(self, **kwargs: Any) -> None: pass

    langfuse_context = _DummyContext()
    propagate_attributes = None


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
