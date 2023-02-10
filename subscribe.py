import time
import feedparser

with open("index.html", "w") as page:
    page.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
    page.write("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/@ajusa/lit@latest/dist/lit.css'>\n")
    page.write("<div class='c'><h1>Index of Subscribes</h1>\n")
    with open("subscribes.txt", "r") as sub:
        j = 0
        for url in sub.readlines():
            j += 1
            feed = feedparser.parse(url, agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
            page.write(f"<a href={j}.html>{feed.feed.title}</a>&emsp;\n")
            with open(f"{j}.html", "w") as f:
                f.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
                f.write("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/@ajusa/lit@latest/dist/lit.css'>\n")
                f.write(f"<div class='c'><h1>{feed.feed.title}</h1>\n")
                for i in feed.entries:
                    f.write(f"<pre><code><a href='{i.enclosures[0].href}'>{i.title}</a>\n")
                    f.write(f"{i.enclosures[0].href}</code></pre>\n")
                f.write("</div>")
    page.write("</div>")
