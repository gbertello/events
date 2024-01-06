#!/usr/bin/env python3

from urllib.request import urlopen

url = "https://www.palaisdesfestivals.com/agenda/culturel/?listpage="

html = ""
for i in range(1, 6):
  html += urlopen(url + str(i)).read().decode("utf-8") + "\n\n"
  
with open("in.html", "w") as f:
  f.write(html)
