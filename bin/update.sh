#!/bin/sh
set -e

cd /home/nurulid/app-fastapi-docker-compose
echo "Updating code..."
git fetch origin
git reset --hard origin/main

echo "Building new images..."
docker compose -f docker-compose.prod.yml build

echo "Deploying with rolling update..."
docker compose -f docker-compose.prod.yml up -d --no-deps --build

echo "Deployment successful!"