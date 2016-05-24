#!/bin/bash

# Set environment options to exit immediately if a non-zero status code
# appears from a command or within a pipe
set -o errexit
set -o pipefail

# Send out Slack notification(s)
invoke notify

# Build static files
cd fec
./manage.py compress

# Run migrations
./manage.py makemigrations
./manage.py migrate --noinput

# Run application
gunicorn fec.wsgi:application
