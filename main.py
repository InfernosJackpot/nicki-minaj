import random
import time
import webbrowser

urls = [
    "https://www.pornhub.com/view_video.php?viewkey=ph6161b3bbbc5ec",
    "https://www.youtube.com/watch?v=CUj2AWEJnwQ",
    "https://www.youtube.com/watch?v=LDZX4ooRsWs",
    "https://www.youtube.com/watch?v=SeIJmciN8mo",
]


def open_website():
    random_url = random.randint(0, len(urls) - 1)
    webbrowser.open(urls[random_url])

if __name__ == '__main__':
    while True:
        time.sleep(random.randint(60, 520))
        open_website()
