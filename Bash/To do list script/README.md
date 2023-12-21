# To-Do List Script

This Bash script allows authorized users to manage their to-do lists and store files in different locations based on user accounts.

## Features

- Displays the current date and time.
- Authenticates users (eg. Elvis, Letty, Guest).
- Allows authorized users to update their to-do lists.
- Stores files in various locations based on user accounts.

## Requirements

- Bash (Bourne Again SHell)

## Usage

1. Clone the repository:

   ```bash
   git clone <repository_url>

## Navigate to the script directory
cd <script_directory>

## Make the script executable
chmod +x todo_script.sh

## Run the script
./todo_script.sh


## Follow the on-screen prompts to choose a user, enter a password (if required), view and update the to-do list, and store files.

## Configuration
Modify the users_passwords associative array in the script to set passwords for authorized users.

## Notes
For enhanced security, avoid storing passwords directly in the script in production environments.
Customize the script according to your specific requirements.
Be cautious when handling sensitive information and files.

## License
This script is released under the MIT License.
