#!/bin/bash

# Variables
door_status="closed"
door_open_time=0
login_file="login.txt"
lock_file="/tmp/door_control.lock"

# Function to log access
log_access() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$login_file"
}

# Function to close the door
close_door() {
    echo "Closing the door..."
    door_status="closed"
}

# Function to open the door
open_door() {
    # Check if the lock file is present (Zenity window is open)
    if [ -e "$lock_file" ]; then
        echo "Zenity window is already open. Please close it before opening again."
        return
    fi

    # Create the lock file
    touch "$lock_file"

    echo "Opening the door..."
    door_status="open"
    door_open_time=$(date +%s)

    # Display a message indicating that the door is open
    zenity --info --text="Door is open. It will automatically close after 20 seconds." &

    # Run the sleep in the background
    (sleep 20 && close_door && zenity --info --text="Door closed after 20 seconds." && log_access "Door closed automatically" && rm "$lock_file") &

    # Prompt for password
    password=$(zenity --password --title="Enter Password" --text="Enter password (Elvis/Letty/guest):")

    case $password in
        "Elvis" | "Letty" | "guest")
            zenity --info --text="Access granted. Welcome $password!"
            log_access "Access granted: $password"
            close_door
            ;;
        *)
            zenity --info --text="Access denied. Incorrect password."
            log_access "Access denied: $password"
            close_door
            ;;
    esac

    # Remove the lock file
    rm "$lock_file"
}

while true; do
    choice=$(zenity --list --title="Door Control" --column="Options" "Open Door" "Close Door" "Exit Script")

    case $choice in
        "Open Door")
            open_door
            ;;
        "Close Door")
            close_door
            ;;
        "Exit Script")
            echo "Exiting the script."
            exit 0
            ;;
        *)
            echo "Invalid choice. Exiting the script."
            exit 1
            ;;
    esac
done
