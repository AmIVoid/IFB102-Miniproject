#!/bin/bash
echo "Creating required folders."
mkdir -p downloaded_videos
mkdir -p output_images
mkdir -p uploaded_images
echo "Folders created."
echo ""
echo "Installing required libraries."
$1/bin/pip install -r requirements.txt
echo "Required libraries installed."