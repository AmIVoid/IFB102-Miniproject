#!/bin/bash
clear
echo "Creating required folders."
mkdir -p downloaded_videos
mkdir -p output_images
mkdir -p uploaded_images
mkdir -p logs
echo "Folders created."
echo ""
echo "Installing required libraries."
pip3 install -r requirements.txt -q
echo "Required libraries installed."
echo ""
python3 ./config.py
echo ""
echo "Starting website"
python3 ./app.py
