import sys
try:
    from langfuse.decorators import observe, langfuse_context
    print("Import success")
except Exception as e:
    print(f"Import failed: {e}")
    import langfuse
    print(f"Langfuse path: {langfuse.__file__}")
    print(f"Langfuse dir: {dir(langfuse)}")
    
    import os
    pkg_path = os.path.dirname(langfuse.__file__)
    print(f"Package contents: {os.listdir(pkg_path)}")
    if os.path.exists(os.path.join(pkg_path, "decorators")):
        print(f"Decorators dir contents: {os.listdir(os.path.join(pkg_path, 'decorators'))}")
