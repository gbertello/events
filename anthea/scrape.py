#!/usr/bin/env python3

from urllib.request import urlopen

url = "https://www.anthea-antibes.fr/fr/calendrier"
html = urlopen(url).read().decode("utf-8")
with open("anthea.html", "w") as f:
  f.write(html)
