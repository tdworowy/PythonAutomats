import re

import requests
from Utils.utils import MyLogging
from bs4 import BeautifulSoup

logger = MyLogging()


def get_youtube_url(query):
    logger.log().info(query)
    response = requests.get(
        "https://www.youtube.com/results?search_query=%s" % query
    ).text
    soup = BeautifulSoup(response, "html.parser")
    urls = soup.find_all(href=True)
    links = [re.search('.*href="/watch.*', str(url)) for url in urls]
    links = [link.group(0) for link in links if link is not None]
    links = [re.search('href="/watch.*"', link).group(0) for link in links]
    return (
        "https://www.youtube.com/%s"
        % links[0][links[0].index("watch") : links[0].index('">')]
    )


if __name__ == "__main__":
    print(get_youtube_url("Test"))
