# File Transfer Script

This Bash script automates the process of transferring large files from a source directory to a destination directory based on a configurable size limit. It also logs the transfer details for reference.

## Configuration

Configure the script by modifying the following variables in the script:

- **Source Directory:** The directory containing the files to be transferred.
- **Destination Directory:** The directory where files will be moved.
- **File Size Limit:** The maximum size of files to be transferred (default is set to 2MB).
- **Log File:** The path to the log file where script execution details will be recorded.

## Prerequisites

Ensure that the following command-line utility is installed on your system:

- **mv:** The \`mv\` command is used for file movement.

You can install it using the following command:

\`\`\`bash
sudo apt-get install mv
\`\`\`

## Usage

1. Make the script executable:
    chmod +x file_transfer.sh
  

2. Run the script:
    ./file_transfer.sh
 

3. Monitor the script execution in the console and check the log file for detailed information.

## Features

- **Dependency Check:** The script checks for the necessary dependencies and installs them if missing.
- **Logging:** Script execution details are logged to a specified log file.
- **Error Handling:** The script handles errors gracefully and provides detailed error messages.
- **File Transfer Notification:** Notify the user upon successful or failed file transfers (notification command can be added).

## Logging

The script logs details about its execution in the specified log file. The log includes timestamps, moved file paths, and any errors encountered during execution.

## Notifications

Notifications are provided at the end of the script execution based on whether the file transfer was successful or encountered errors. You can customize the notification command in the script according to your preferences.

## Author

[Elvis Mwanthi: elvismwanthi@gmail.com]
