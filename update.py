import requests
from bs4 import BeautifulSoup
import os
import subprocess
import time


def fetch_and_save(url, file_name, headers={}):
    # Check if the file exists and is not older than 1 hour then returning the latest content
    # else downloading the file and saving it
    if os.path.exists(file_name) and time.time() - os.path.getmtime(file_name) < 3600:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            return content
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_name, "wb") as f:
            f.write(response.content)
        print("File saved successfully")
        return response.content
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching {url}: {e}")
    except IOError as e:
        raise Exception(f"Error saving to {file_name}: {e}")

def main():
    try:
        novelbin = fetch_and_save(
            "https://novelbin.me/novel-book/shadow-slave", "novelbin.html")

        novel_soup = BeautifulSoup(novelbin, 'lxml')

        novel_chapters = novel_soup.find_all(class_="item-value")
        new_chapters = []
        for chapter in novel_chapters:
            chapter_title = chapter.find("a").text.strip()
            new_chapters.append(chapter_title)

        new_chapters = '\n'.join(new_chapters)
        subprocess.run(["notify-send", "New Chapters", new_chapters])
    except Exception as e:
        subprocess.run(["notify-send", "Error", str(e)])

if __name__ == "__main__":
    main()
