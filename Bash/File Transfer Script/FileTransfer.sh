#!/bin/bash

# Configurable variables
source_directory=" # Please enter source directory here"
destination_directory=" # Please enter destination directory here"
file_size_limit=2000000 # 2MB in bytes
log_file="/mnt/d/File_transfer_logs.log"

# Function to check and install dependencies
check_and_install_dependency() {
    local command_name="$1"
    command -v "$command_name" >/dev/null 2>&1 || {
        echo >&2 "$command_name is required but not installed. Installing..."
        sudo apt-get install -y "$command_name" || {
            echo >&2 "Failed to install $command_name. Aborting."
            exit 1
        }
        echo "$command_name installed successfully."
    }
}

# Check and install dependencies
check_and_install_dependency "mv"

# Check for source directory existence
[ -d "$source_directory" ] || { echo >&2 "Source directory not found. Aborting."; exit 1; }

# Logging
exec &>> "$log_file"
echo "Script execution started at: $(date)"

# Error handling
set -e
trap 'echo "Error at line $LINENO"; exit 1' ERR

# Find files greater than 2MB in the source directory
find "$source_directory" -type f -size +"$file_size_limit"c -print0 |
  while IFS= read -r -d '' file; do
    # Extract relative path for preserving directory structure
    relative_path="${file#$source_directory/}"

    # Move the file to the destination directory
    if mv "$file" "$destination_directory/$relative_path"; then
        echo "Moved: $file"
    else
        echo >&2 "Failed to move: $file"
    fi
done

# Notification
if [ $? -eq 0 ]; then
    echo "File transfer completed successfully."
    # Add notification command here
else
    echo "File transfer failed. Check the log for details."
    # Add notification command here
fi

echo "Script execution completed at: $(date)"
