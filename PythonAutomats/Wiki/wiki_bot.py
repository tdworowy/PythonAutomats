import wikipedia
from Utils.utils import MyLogging

my_logging = MyLogging()


def get_random_wiki_page_title():
    my_logging.log().info("Get random wiki articular")
    article_title = wikipedia.random(1)
    my_logging.log().info(article_title)
    return article_title
