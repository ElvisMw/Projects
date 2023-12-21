#!/bin/bash

# Function to get the current timestamp
get_timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

# Check if pidstat is installed
if command -v pidstat &> /dev/null; then
  echo "pidstat is already installed."
else
  # Install sysstat, which includes pidstat
  sudo apt-get update
  sudo apt-get install sysstat -y
fi

# Function to start resource monitoring using pidstat in the background
start_resource_monitoring() {
  pidstat -urd -h -p $$ 1 > resource_stats.txt 2>&1 &
}

# Prompt the user to enter the video URL
read -p "Enter the URL of the video: " video_url

# Check if the URL is provided
if [ -z "$video_url" ]; then
  echo "$(get_timestamp) Error: Video URL is required." >> error.txt
  exit 1
fi

# Destination folder where you want to save the downloaded video
destination_folder="D:\videos"

# Create the destination folder if it doesn't exist
mkdir -p "$destination_folder"

# Start resource monitoring in the background
start_resource_monitoring

# Use yt-dlp to download the video with specified format
yt-dlp -f 'best[height<=720]' -o "$destination_folder/%(title)s.%(ext)s" "$video_url" > stdout.txt 2> >(while read -r line; do echo "$(get_timestamp) $line" >> error.txt; done)

# Check if yt-dlp was successful
if [ $? -eq 0 ]; then
  echo "$(get_timestamp) Video downloaded successfully to $destination_folder"
else
  echo "$(get_timestamp) Error downloading the video. Check error.txt for details."
fi

# A secret from the Bible
echo "----------------------------------------------------"
echo "Psalm 18:29"
echo "With your help, I can defeat an army."
echo "If my God is with me, I can climb over enemy walls."
echo "----------------------------------------------------"

# Kill the pidstat process after the download is complete
pkill -f pidstat
