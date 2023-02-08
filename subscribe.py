import requests
from bs4 import BeautifulSoup

with open("index.html", "w", encoding="utf-8") as page:
    page.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
    page.write("<h1>Index of Subscribes</h1>\n")
    with open("subscribes.txt", "r", encoding="utf-8") as sub:
        url = sub.readline()
        while url:
            text = requests.get(url).text
            soup = BeautifulSoup(text, "xml")
            page.write(f"<a href='{soup.title.string}.html'>{soup.title.string}</a><br>\n")
            with open(f"{soup.title.string}.html", "w", encoding="utf-8") as f:
                f.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
                f.write(f"<h1>{soup.title.string}</h1>\n")
                for i in soup.select("item"):
                    f.write(f"<code>{i.pubDate.string}</code>\n")
                    f.write(f"<a href='{i.enclosure['url']}'>{i.title.string}</a><br>\n")
            url = sub.readline()
