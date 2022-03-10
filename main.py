import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get("https://news.ycombinator.com/news")

    print(resp.text)


if __name__ == "__main__":
    main()
