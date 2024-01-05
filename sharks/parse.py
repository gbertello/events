#!/usr/bin/env python3

from bs4 import BeautifulSoup
from showSharks import ShowSharks

with open("in.html", "r") as f:
  html = f.read()

shows = []

soup = BeautifulSoup(html, "html.parser")
for show_soup in soup.find_all("div", {"class": "bg-indigo-100"}):
  show = ShowSharks()
  show.read(show_soup)
  shows.append(show)

with open("out.csv", "w") as f:
  for show in shows:
    f.write(show.to_str() + "\n")
