#!/usr/bin/env python3

from bs4 import BeautifulSoup
from showAnthea import ShowAnthea

with open("in.html", "r") as f:
  html = f.read()

shows = []

soup = BeautifulSoup(html, "html.parser")
section_soups = soup.find("div", {"class": "spectacles__panel"}) \
                    .find_all("section")

for section_soup in section_soups:
  show_soups = section_soup.find("ul", {"class": "spectacles__list"}) \
                           .find_all("li")

  for show_soup in show_soups:
    if len(show_soup.find_all("h3", {"class": "card__spectacle_title"})) > 0:
      show = ShowAnthea()
      show.read(show_soup)
      shows.append(show)

duplicates = []
for i in range(0, len(shows)):
  for j in range(0, i):
    if shows[i].title == shows[j].title:
      duplicates.append(i)
      break

duplicates.reverse()
for duplicate in duplicates:
  del shows[duplicate]
  
with open("out.csv", "w") as f:
  for show in shows:
    f.write(show.to_str() + "\n")