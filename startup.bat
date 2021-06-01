@echo off
cls
echo Creating required folders.
mkdir downloaded_videos
mkdir output_images
mkdir uploaded_images
mkdir logs
echo Folders created.
echo.
echo Installing required libraries.
pip3 install -r requirements.txt -q
echo Required libraries installed.
echo.
cd %cd%
python config.py
echo.
echo Starting website
python app.py