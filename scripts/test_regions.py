import os
from langfuse import Langfuse
from dotenv import load_dotenv

load_dotenv()
pk = os.getenv("LANGFUSE_PUBLIC_KEY")
sk = os.getenv("LANGFUSE_SECRET_KEY")

print("Sending to EU...")
lang_eu = Langfuse(public_key=pk, secret_key=sk, host="https://eu.cloud.langfuse.com")
lang_eu.trace(name="TRACE_FROM_EU_REGION")
lang_eu.flush()

print("Sending to US...")
lang_us = Langfuse(public_key=pk, secret_key=sk, host="https://cloud.langfuse.com")
lang_us.trace(name="TRACE_FROM_US_REGION")
lang_us.flush()

print("Done. Check your dashboard!")
