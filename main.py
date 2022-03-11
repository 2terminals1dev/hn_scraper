import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/news"


def main():
    resp = requests.get(URL)
    print(resp.text)


if __name__ == "__main__":
    main()
