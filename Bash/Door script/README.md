# Door Control Script

This Bash script provides a simple door control system that allows you to open and close a door with a password prompt. It logs access information, including the date, time, and user.

## Features

- **Automatic Door Closure:** The door automatically closes after 20 seconds if left open.
- **Password Protection:** Users must enter a password (Elvis, Letty, or guest) to open the door.
- **Access Logging:** Access attempts are logged in a file for history purposes.
- **GUI Interface:** The script uses Zenity to display graphical user interface dialogs.

## Prerequisites

- **Zenity:** Ensure that Zenity is installed on your system. You can install it using your system's package manager.

## Usage

1. Make the script executable:

    ```bash
    chmod +x door_control.sh
    ```

2. Run the script:

    ```bash
    ./door_control.sh
    ```

3. Follow the on-screen instructions to open or close the door.

## Options

- **Open Door:** Opens the door, prompting for a password.
- **Close Door:** Manually closes the door.
- **Exit Script:** Exits the script.

## Notes

- Ensure that only one instance of the Zenity window is open at a time by avoiding concurrent openings.

## Author

[Elvis Mwanthi: elvismwanthi@gmail.com]
