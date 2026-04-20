import os
import time
from dotenv import load_dotenv
from langfuse.decorators import observe, langfuse_context

load_dotenv()

# Set environment variables manually just in case
os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")
os.environ["LANGFUSE_HOST"] = os.getenv("LANGFUSE_HOST") or os.getenv("LANGFUSE_BASE_URL") or "https://cloud.langfuse.com"

@observe()
def test_function():
    print("Executing observed function...")
    langfuse_context.update_current_trace(
        name="diagnostic-trace",
        user_id="diag-user",
        tags=["diagnostic"]
    )
    time.sleep(1)
    print("Function done.")

if __name__ == "__main__":
    print(f"Public Key: {os.environ['LANGFUSE_PUBLIC_KEY']}")
    print(f"Secret Key: {os.environ['LANGFUSE_SECRET_KEY'][:10]}...")
    print(f"Host: {os.environ['LANGFUSE_HOST']}")
    
    test_function()
    
    # Force flush
    print("Flushing...")
    langfuse_context.flush()
    print("Done.")
