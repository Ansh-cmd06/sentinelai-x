"""
SentinelAI X — Gunicorn Production Configuration
Optimized for Render and cloud containerized deployments.
"""
import os

# Binding address and port
bind = f"0.0.0.0:{os.getenv('PORT', '5000')}"

# Worker processes and concurrency
# Default to 2 workers with 4 threads each for memory-efficient concurrency
workers = int(os.getenv("WEB_CONCURRENCY", "2"))
worker_class = "gthread"
threads = int(os.getenv("PYTHON_THREADS", "4"))

# Timeouts
timeout = int(os.getenv("GUNICORN_TIMEOUT", "120"))
keepalive = int(os.getenv("GUNICORN_KEEPALIVE", "5"))

# Logging to stdout / stderr for cloud container log collection
accesslog = "-"
errorlog = "-"
loglevel = os.getenv("LOG_LEVEL", "info")
