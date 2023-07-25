# gunicorn_config.py

import multiprocessing

# Gunicorn configuration
bind = "0.0.0.0:8000"  # The address and port to bind Gunicorn to
workers = multiprocessing.cpu_count() * 2 + 1  # The number of worker processes
worker_class = "sync"  # The type of worker process to use (sync, gthread, etc.)
timeout = 60  # Timeout for handling requests
max_requests = 1000  # Number of requests a worker will process before restarting
graceful_timeout = 30  # Timeout for graceful worker shutdown
errorlog = "-"  # Log to stdout

# Django-specific settings
# Change to the project directory
django_settings = "./src/feme_core/settings.py"  # Set the Django settings module
