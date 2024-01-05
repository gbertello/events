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
    show = ShowAnthea()
    show.read(show_soup)
    shows.append(show)

with open("out.csv", "w") as f:
  f.write("{};{};{};{};{}\n".format("Location", "Title", "Date", "Image", "Link"))
  for show in shows:
    f.write(show.to_str() + "\n")
