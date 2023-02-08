import sys
import requests
from bs4 import BeautifulSoup

url = "https://dmhy.b168.net/topics/rss/team_id/650/rss.xml"
text = requests.get(url).text
soup = BeautifulSoup(text, "xml")

with open(f"650.html", "w", encoding="utf-8") as f:
    f.write("<div style='font-size: 75%'>\n")
    f.write(f"<h1>{soup.title.string}</h1>\n")
    for i in soup.select("item"):
        f.write(f"<code>{i.pubDate.string}</code>&emsp;\n")
        f.write(f"<a href='{i.enclosure['url']}'>{i.title.string}</a><br>\n")
    f.write("</div>")
