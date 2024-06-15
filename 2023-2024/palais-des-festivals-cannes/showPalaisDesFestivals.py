import os, sys
from datetime import date, timedelta

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from show import Show

class ShowPalaisDesFestivals(Show):
  def __init__(self):
    super().__init__()
    self.soup = ""

  def read(self, soup):
    self.soup = soup
    self.location = "Palais des festivals - Cannes"
    self.read_title()
    self.read_image()
    self.read_link()
    self.read_dates()

  def read_title(self):
    self.title = self.soup.find("div", {"class": "item-infos-title"}).text

  def read_image(self):
    self.img = self.soup.find("img").get("src")

  def read_link(self):
    self.link = self.soup.find("a").get("href")

  def read_dates(self):
    MONTHS = ["Janv.", "Févr.", "Mars", "Avr.", "Mai", "Juin", "Juil.", "", "", "Oct."]
    MONTHS2 = ["", "Février", "Avril", "Mai", "", "Juillet", "Août", "Septembre"]
    self.dates = []
    for dates_text in self.soup.find("div", {"class": "item-block-infos-date"}).text.replace("\n", " ").strip().split(","):
      while "   " in dates_text:
        dates_text = dates_text.replace("  ", " ")
      dates_text = dates_text.replace("  ", " ").replace("... ", "").strip()
      if " au " not in dates_text:
        year = 2024
        month = MONTHS.index(dates_text.split(" ")[3]) + 1
        day = int(dates_text.split(" ")[2])
        self.dates.append(date(year, month, day))
      else:
        year = 2024
        month = MONTHS2.index(dates_text.split(" au ")[1].split(" ")[1]) + 1
        day = int(dates_text.split(" au ")[1].split(" ")[0])
        date2 = date(year, month, day)
        if len(dates_text.split(" au ")[0].split(" ")) > 2:
          month = MONTHS2.index(dates_text.split(" au ")[0].split(" ")[2]) + 1
        day = int(dates_text.split(" au ")[0].split(" ")[1])
        date1 = date(year, month, day)
        delta = date2 - date1
        for i in range(delta.days + 1):
          self.dates.append(date1 + timedelta(days=i))
