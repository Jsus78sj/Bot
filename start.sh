#!/bin/bash
# R3D Telegram Bot - First time setup and launch

echo "Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y ffmpeg redis-server

echo "Starting Redis..."
sudo service redis-server start

echo "Installing Python requirements..."
python3 -m pip install -r r3d.txt

# Run the main bot in a screen session
screen -dmS r3d python3 main.py

echo "Bot started in screen session 'r3d'."
echo "To attach: screen -r r3d"
echo "To stop: screen -X -S r3d quit"
