#!/bin/bash

# Set up the main project directory
mkdir -p bank_api/app/{models,schemas,services,routes,utils}
mkdir -p bank_api/migrations
mkdir -p bank_api/.venv

# Create necessary files
touch bank_api/app/__init__.py
touch bank_api/app/app.py
touch bank_api/app/config.py
touch bank_api/app/db.py
touch bank_api/app/models/user.py
touch bank_api/app/schemas/user.py
touch bank_api/app/services/auth_service.py
touch bank_api/app/routes/auth_routes.py
touch bank_api/app/utils/__init__.py

# Create additional files
touch bank_api/requirements.txt
touch bank_api/run.py

echo "Project structure for 'bank_api' created successfully!"
