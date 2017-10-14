import pdfkit
import requests

urls = ["http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=1841",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=1814",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=594",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=575",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=610",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=641",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=663",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=692",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=712",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=1537",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=747",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=1584",
        "http://www.ztz.rybnik.pl/rj/index.php?id=przystanek&prz_id=114&tab_id=1577"]

ENCODING = "<!DOCTYPE html><html><head> <meta charset=\"utf-8\"></head><body> "
END = " <body></html>"


def get_tables(urls):
    tables = []
    for url in urls:
        response = requests.get(url)
        response.encoding = 'utf-8'
        response = response.text
        table = response[response.find("<table class=tabliczka>"):response.find("</table>")]
        table = ENCODING + table + END
        tables.append(table)
    return tables


def save_HTML(tables):
    for i, table in enumerate(tables, 1):
        with open("table%s.html" % i, 'w', encoding='utf-8') as f:
            f.write(table)


def save_PDF(tables):
    for i, table in enumerate(tables, 1):
        pdfkit.from_string(table, "table%s.pdf" % str(i))


if __name__ == "__main__":
    get_tables(urls)
    # save_HTML(get_tables(urls))
    save_PDF(get_tables(urls))
