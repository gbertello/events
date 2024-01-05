import os, sys, re
from datetime import date

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from show import Show

class ShowAntibea(Show):
  def __init__(self):
    super().__init__()
    self.soup = ""

  def read(self, soup):
    self.soup = soup
    self.location = "Antibea"
    self.read_title()
    self.read_image()
    self.read_link()
    self.read_dates()

  def read_title(self):
    self.title = self.soup.find("a", {"class": "tribe-event-url"}).text.strip().lower().capitalize()

  def read_image(self):
    self.img = re.findall(r'url\(.*\)', self.soup.find("div", {"class": "block-image"}).get('style'))[0][4:-1]

  def read_link(self):
    self.link = self.soup.find("a", {"class": "tribe-event-url"}).get('href')

  def read_dates(self):
    MONTHS = ["JAN", "FÉV", "MARS", "AVR", "MAI", "JUIN", "JUI", "AOÛT"]
    dates_text = self.soup.find("span").text.replace("MARS 21", "MAR. 21").replace("MARS 05", "MAR. 05").replace("31 MAR.", "31 MARS.").replace("MAI 01", "MAI. 01")
    if dates_text.endswith("."): dates_text = dates_text[0:-1]
    for dates_text_month in dates_text.split(". "):
      year = 2024
      month = MONTHS.index(dates_text_month.split(" ")[-1]) + 1
      for dates_text_day in " ".join(dates_text_month.split(" ")[0:-1]).split("|"):
        day = int(dates_text_day)
        self.dates.append(date(year, month, day))
