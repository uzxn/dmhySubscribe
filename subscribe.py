import time
import feedparser

with open("index.html", "w") as page:
    page.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
    page.write("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/@ajusa/lit@latest/dist/lit.css'>\n")
    page.write("<div class='c'><h1>Index of Subscribes</h1>\n")
    with open("subscribes.txt", "r") as sub:
        for line in sub.readlines():
            name, url = line.split(',', 1)
            feed = feedparser.parse(url, agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
            page.write(f"<a href={name}.html>{name}</a><br>\n")
            with open(f"{name}.html", "w") as f:
                f.write("<meta name='viewport' content='width=device-width initial-scale=1'>\n")
                f.write("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/@ajusa/lit@latest/dist/lit.css'>\n")
                f.write(f"<div class='c'><h1>{name}</h1>\n")
                for i in feed.entries:
                    f.write(f"<a href='{i.enclosures[0].href}'>{i.title}</a><br>\n")
                f.write("</div>")
    page.write("</div>")
