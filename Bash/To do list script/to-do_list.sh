#!/bin/bash
# To-Do List Script with Timestamp (including AM/PM)

declare -A users_passwords
users_passwords["Elvis"]="elvis_pass"
users_passwords["Letty"]="letty_pass"
users_passwords["Guest"]=""

# Get current date and time
current_date_time=$(date +"%Y-%m-%d %I:%M:%S %p")  # %p represents AM/PM
echo "Current Date and Time: $current_date_time"

# User authentication
PS3="Choose user by number: "
options=("Elvis" "Letty" "Guest")

select user_choice in "${options[@]}"; do
    case $user_choice in
        "Elvis" | "Letty" | "Guest")
            while true; do
                if [ -z "${users_passwords[$user_choice]}" ]; then
                    # No password for Guest
                    echo -e "\nAccess granted. You selected $user_choice (Guest)."
                    break
                else
                    # Ask for password for other users
                    echo "Enter password for $user_choice: "
                    read -s entered_password

                    if [ "$entered_password" == "${users_passwords[$user_choice]}" ]; then
                        echo -e "\nAccess granted. You selected $user_choice."
                        break
                    else
                        echo -e "\nAccess denied. Incorrect password. Try again."
                    fi
                fi
            done

            # To-Do List for the day
            todo_file="${user_choice}_to-do.txt"
            if [ -e "$todo_file" ]; then
                echo -e "\nTo-Do List for $user_choice today:"
                cat "$todo_file"
            else
                echo -e "\nNo to-do list found for $user_choice today."
            fi

            # Allow user to update the to-do list
            echo -e "\nEnter new task to add to the to-do list (press Ctrl+D to finish):"
            while read -r new_task; do
                timestamp=$(date +"%Y-%m-%d %I:%M %p")  # %p represents AM/PM
                echo "[$timestamp] $new_task" >> "$todo_file"
            done

            echo -e "\nTo-Do List updated for $user_choice."

            # Store files in different locations based on user accounts
            user_directory="${user_choice}_files"
            if [ ! -d "$user_directory" ]; then
                mkdir "$user_directory"
            fi

            echo "Creating and storing files in $user_directory..."
            touch "$user_directory/file1.txt"
            touch "$user_directory/file2.txt"
            echo "Files created successfully."

            ;;
        *)
            echo "Invalid choice. Please select a number between 1 and ${#options[@]}."
            ;;
    esac
    break
done
