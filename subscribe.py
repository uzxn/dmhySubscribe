import time
import feedparser

with open("index.html", "w", encoding="utf-8") as page:
    page.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n"
               "<link rel='stylesheet' href='https://unpkg.com/mvp.css@1.12/mvp.css'>\n"
               "<main>\n"
               "<h1>Index of Subscribes</h1>\n"
               "<table>\n")
    with open("subscribes.txt", "r", encoding="utf-8") as sub:
        url = sub.readline()
            while url:
                feed = feedparser.parse(url)
                page.write(f"<tr>\n"
                           "<th>{time.strftime('%Y-%m-%d %H:%M:%S', feed.feed.published_parsed)}</th>\n"
                           "<th><a href='{feed.feed.title}.html'>{feed.feed.title}</a></th>\n"
                           "</tr>\n")
                with open(f"{feed.feed.title}.html", "w", encoding="utf-8") as f:
                    f.write(f"<meta name='viewport' content='width=device-width initial-scale=1'>\n"
                            "<link rel='stylesheet' href='https://unpkg.com/mvp.css@1.12/mvp.css'>\n"
                            "<main>\n"
                            "<h1>{feed.feed.title}</h1>\n"
                            "<table>\n")
                    for i in feed.entries:
                        f.write(f"<tr>\n"
                                "<th>{time.strftime('%Y-%m-%d %H:%M:%S', i.published_parsed)}</th>\n"
                                "<th>{i.enclosures[0].href}</th>\n"
                                "</tr>\n")
                    f.write("</trable>\n</main>")
    page.write("</trable>\n</main>")
    url = sub.readline()
