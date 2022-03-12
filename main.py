import requests
import pprint
from bs4 import BeautifulSoup


URL = "https://news.ycombinator.com/news"


def sort_posts_by_votes(hn_list):
    """Sorts list of posts by votes decending."""
    return sorted(hn_list, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    """Returns a dict of posts with points >= 100."""
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points >= 100:
                hn.append({"title": title, "link": href, "votes": points})

    return sort_posts_by_votes(hn)


def main():
    resp = requests.get(URL)

    soup = BeautifulSoup(resp.text, "html.parser")
    links = soup.select(".titlelink")
    subtext = soup.select(".subtext")

    pprint.pprint(create_custom_hn(links, subtext))


if __name__ == "__main__":
    main()
