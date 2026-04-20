import os
import logging
from dotenv import load_dotenv
from langfuse import Langfuse

# Enable debug logging for Langfuse
logging.basicConfig(level=logging.DEBUG)
os.environ["LANGFUSE_DEBUG"] = "True"

load_dotenv()

public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
secret_key = os.getenv("LANGFUSE_SECRET_KEY")
host = os.getenv("LANGFUSE_HOST") or "https://cloud.langfuse.com"

print(f"Testing with Host: {host}")
print(f"Public Key: {public_key}")

langfuse = Langfuse(public_key=public_key, secret_key=secret_key, host=host)

trace = langfuse.trace(name="debug-connection-test")
trace.span(name="hello-world")

print("Attempting to flush...")
langfuse.flush()
print("Flush called. If no error appeared above, it should be sent.")
