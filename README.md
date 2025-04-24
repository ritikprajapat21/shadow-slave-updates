# Shadow Slave Novel Update Notifier

This Python script checks the novel website [NovelBin](https://novelbin.me/novel-book/shadow-slave) for new chapters of the "Shadow Slave" novel and sends a desktop notification listing the latest chapters.

## Functionality

1.  **Fetches Webpage:** Downloads the HTML content of the Shadow Slave novel page on NovelBin.
2.  **Caches Content:** Saves the downloaded HTML to `novelbin.html`. If the file exists and is less than 1 hour old, it uses the cached version instead of downloading again.
3.  **Parses Chapters:** Uses BeautifulSoup to parse the HTML and extract the list of chapter titles.
4.  **Sends Notification:** Uses the `notify-send` command (common on Linux systems) to display a desktop notification containing the list of fetched chapter titles.
5.  **Error Handling:** If any error occurs during fetching, saving, or parsing, it sends an error notification.

## Dependencies

*   **Python 3:** The script is written in Python 3.
*   **requests:** Used for making HTTP requests to fetch the webpage.
*   **beautifulsoup4:** Used for parsing the HTML content.
*   **lxml:** An efficient HTML parser used by BeautifulSoup.
*   **notify-send:** A command-line utility for sending desktop notifications (usually pre-installed on Linux distributions with desktop environments like GNOME, KDE, XFCE).

## Installation

1.  **Clone the repository (or download the script):**
    ```bash
    # If you have git installed
    # git clone https://github.com/ritikprajapat21/shadow-slave-updates.git updates
    # cd updates

    # Or just save the update.py script
    ```
2.  **Install Python dependencies:**
    It's recommended to use a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirement.txt
    ```
    If `requirement.txt` doesn't exist, you can install manually:
    ```bash
    pip install requests beautifulsoup4 lxml
    ```
3.  **Ensure `notify-send` is installed:**
    On Debian/Ubuntu-based systems:
    ```bash
    sudo apt update
    sudo apt install libnotify-bin
    ```
    On Fedora:
    ```bash
    sudo dnf install libnotify
    ```
    Check your distribution's package manager if you use a different Linux flavor. This script might not work as intended on macOS or Windows without modifications or alternative notification methods.

## Usage

Run the script directly from your terminal:

```bash
python update.py
```

The script will then fetch the chapter list (or use the cache) and display a desktop notification. You can set this up as a cron job or systemd timer to run periodically.

## Note

Web scraping can be fragile. If the structure of the NovelBin website changes, this script may stop working correctly and will need to be updated.
