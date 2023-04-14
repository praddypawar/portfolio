#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput

# Build Django app
python manage.py migrate
python manage.py collectstatic --noinput

# Deploy to Vercel
vercel --prod
