from __future__ import annotations

import os
from typing import Any

try:
    from langfuse import observe, get_client, propagate_attributes
    langfuse_client = get_client()
    
    # We'll use a dummy context object that reminds us to use v4 patterns
    class _LangfuseContextV4:
        def update_current_trace(self, **kwargs: Any) -> None:
            # In v4, trace-level attributes should be set via propagate_attributes.
            # For backward compatibility, we can try to set them on the current span
            # but Langfuse v4 prefers propagation.
            from langfuse import propagate_attributes
            # This is tricky because update_current_trace was a one-shot call,
            # while propagate_attributes is a context manager.
            # We'll map what we can to update_current_span.
            langfuse_client.update_current_span(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            # Map usage to usage_details if present
            if "usage" in kwargs:
                kwargs["usage_details"] = kwargs.pop("usage")
            
            # In v4, we use update_current_generation if we have usage info
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
