import os
from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()

public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
secret_key = os.getenv("LANGFUSE_SECRET_KEY")
host = "https://cloud.langfuse.com"

print(f"Public Key: {public_key}")
print(f"Secret Key: {secret_key[:10]}...")

langfuse = Langfuse(public_key=public_key, secret_key=secret_key, host=host)

try:
    trace = langfuse.trace(name="test-final-diag")
    print(f"Trace created: {trace.id}")
    langfuse.flush()
    print("Flush completed.")
except Exception as e:
    print(f"Error: {e}")
