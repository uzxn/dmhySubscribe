import time
import feedparser

with open("index.html", "w", encoding="utf-8") as page:
    page.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
    page.write("<link rel='stylesheet' href='https://unpkg.com/mvp.css@1.12/mvp.css'>\n")
    page.write("<h1>Index of Subscribes</h1>\n")
    with open("subscribes.txt", "r", encoding="utf-8") as sub:
        for url in sub.readlines():
            feed = feedparser.parse(url, agent="Mozilla/5.0 (Android 8.1.0; Mobile; rv:109.0) Gecko/109.0 Firefox/109.0")
            page.write(f"<a href='{feed.feed.title}.html'>{feed.feed.title}</a><br>\n")
            with open(f"{feed.feed.title}.html", "w", encoding="utf-8") as f:
                f.write(f"<h1>{feed.feed.title}</h1>\n")
                for i in feed.entries:
                    f.write(f"<a href='{i.enclosures[0].href}'>{i.title}</a><br>\n")
