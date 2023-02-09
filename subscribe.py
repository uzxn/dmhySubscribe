import time
import feedparser

with open("index.html", "w", encoding="utf-8") as page:
    page.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
    page.write("<link rel='stylesheet' href='https://unpkg.com/mvp.css@1.12/mvp.css'>\n")
    page.write("<h1>Index of Subscribes</h1>\n")
    page.write("<ul>\n")
    with open("subscribes.txt", "r", encoding="utf-8") as sub:
        j = 0
        for url in sub.readlines():
            j += 1
            feed = feedparser.parse(url, agent="Mozilla/5.0 (Android 8.1.0; Mobile; rv:109.0) Gecko/109.0 Firefox/109.0")
            page.write(f"<li><a href='{j}.txt'>{feed.feed.title}</a></li>\n")
            with open(f"{j}.txt", "w", encoding="utf-8") as f:
                f.write(f"{feed.feed.title}\n\n")
                for i in feed.entries:
                    f.write(f"{i.title}\n    {i.enclosures[0].href}'>\n")
        page.write("</ul>")
