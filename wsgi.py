"""
SentinelAI X — Production WSGI Entry Point
Exposes `app` for WSGI HTTP servers like Gunicorn or uWSGI.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env without overriding existing environment variables
load_dotenv(override=False)

# Ensure runtime directories exist
data_dir = Path("data")
(data_dir / "reports").mkdir(parents=True, exist_ok=True)
(data_dir / "documents").mkdir(parents=True, exist_ok=True)

from app.main import app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "0.0.0.0" if (os.getenv("RENDER") or os.getenv("PORT")) else "127.0.0.1")
    debug = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1")
    app.run(host=host, port=port, debug=debug)
