import os, sys
from datetime import date

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from show import Show

class ShowSharks(Show):
  def __init__(self):
    super().__init__()
    self.soup = ""

  def read(self, soup):
    self.soup = soup
    self.location = "Sharks"
    self.read_title()
    self.read_image()
    self.read_link()
    self.read_dates()

  def read_title(self):
    self.title = "Antibes - " + self.soup.find_all("div", {"class": "md:text-xl"})[2].text

  def read_image(self):
    self.img = "https://www.sharks-antibes.com/logos/sharks-logo-2022.svg"

  def read_link(self):
    self.link = "https://www.sharks-antibes.com/calendrier"

  def read_dates(self):
    MONTHS = ["janvier", "février", "mars", "avril", "mai"]
    dates_text = self.soup.find("div", {"class": "whitespace-no-wrap"}).text
    year = 2024
    month = MONTHS.index(dates_text.split(" ")[2]) + 1
    day = int(dates_text.split(" ")[1])
    self.dates = [date(year, month, day)]
