import pathlib

file_path = pathlib.Path("venv/lib/python3.13/site-packages/flask_gravatar/__init__.py")
# For Render's default venv location, adjust path if needed
if not file_path.exists():
    file_path = pathlib.Path(".venv/lib/python3.13/site-packages/flask_gravatar/__init__.py")

if file_path.exists():
    text = file_path.read_text()
    # Replace old import
    text = text.replace(
        "from flask import _request_ctx_stack, current_app, has_request_context, request",
        "from flask import current_app, has_request_context, request, g"
    )
    # Replace _request_ctx_stack usage
    text = text.replace("_request_ctx_stack.top", "request if has_request_context() else None")
    file_path.write_text(text)
    print("✅ Patched flask_gravatar for Flask 3.x")
else:
    print("⚠️ flask_gravatar not found, skipping patch")
