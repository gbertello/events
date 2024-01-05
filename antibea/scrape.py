#!/usr/bin/env python3

from urllib.request import urlopen

url = "https://www.theatre-antibea.fr/"
html = urlopen(url).read().decode("utf-8")
with open("in.html", "w") as f:
  f.write(html)
