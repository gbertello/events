#!/usr/bin/env python3

from bs4 import BeautifulSoup
from showLeTribunal import ShowLeTribunal

with open("in.html", "r") as f:
  html = f.read()

shows = []

soup = BeautifulSoup(html, "html.parser")
shows_soup = soup.find("div", {"class": "filter_gallery_2527"})
for show_soup in shows_soup.find_all("a"):
  show = ShowLeTribunal()
  show.read(show_soup)
  shows.append(show)

with open("out.csv", "w") as f:
  for show in shows:
    f.write(show.to_str() + "\n")
