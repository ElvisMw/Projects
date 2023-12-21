# Video Downloader Script

This Bash script allows you to download a video from a given URL using the yt-dlp tool. It provides a simple interface to enter the video URL, handles errors, and saves the downloaded video to a specified destination folder.

## Prerequisites

Make sure you have the following installed on your system:

- Bash
- yt-dlp

## Usage

1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run the script by executing the following command:

    ```bash
    bash script.sh
    ```

4. Follow the on-screen prompts to enter the video URL.

## Configuration

You can customize the script by modifying the following variables:

- `destination_folder`: The folder where the downloaded video will be saved. Change the value to your preferred destination.

## Error Handling

Errors, if any, will be logged in the `error.txt` file. If the script encounters an issue, it will log a timestamped error message in the file.

## Logging

Successful downloads and additional information are logged in the `stdout.txt` file.

## Note

- The script uses the `yt-dlp` command to download the video with a specified format (`best[height<=720]`).

- Make sure to provide the correct video URL when prompted.

- In case of issues, refer to the `error.txt` file for details.

Feel free to contribute and improve this script!
