import os, sys
from datetime import date, timedelta

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from show import Show

class ShowLeTribunal(Show):
  def __init__(self):
    super().__init__()
    self.soup = ""

  def read(self, soup):
    self.soup = soup
    self.location = "Le Tribunal"
    self.read_title()
    self.read_image()
    self.read_link()
    self.read_dates()

  def read_title(self):
    self.title = self.soup.get('title').replace("Jeremy Charbonnel", "Jeremy Charbonnel – ").split(' – ')[0]

  def read_image(self):
    img = self.soup.find("img")
    self.img = img.get('src')

  def read_link(self):
    self.link = self.soup.get('href')

  def read_dates(self):
    MONTHS = ["janvier", "février", "mars", "avril", "mai", ""]
    dates_text = self.soup.get('title').replace("Jeremy Charbonnel", "Jeremy Charbonnel – ").replace("du ", "").split(' – ')[1].strip()
    
    self.dates = []
    if "&" not in dates_text and "au" not in dates_text:
      year = 2024
      month = MONTHS.index(dates_text.split(" ")[1]) + 1
      day = int(dates_text.split(" ")[0])
      self.dates.append(date(year, month, day))
    elif "&" in dates_text:
      year = 2024
      month = MONTHS.index(dates_text.split(" ")[-1]) + 1
      day = int(dates_text.split(" ")[0])
      self.dates.append(date(year, month, day))
      day = int(dates_text.split(" ")[2])
      self.dates.append(date(year, month, day))
    elif "/" in dates_text:
      year = 2024
      month = int(dates_text.split(" au ")[0].split("/")[1])
      day = int(dates_text.split(" au ")[0].split("/")[0])
      date1 = date(year, month, day)
      month = int(dates_text.split(" au ")[1].split("/")[1])
      day = int(dates_text.split(" au ")[1].split("/")[0])
      date2 = date(year, month, day)
      delta = date2 - date1
      for i in range(delta.days + 1):
        self.dates.append(date1 + timedelta(days=i))
    else:
      year = 2024
      month = MONTHS.index(dates_text.split(" au ")[1].split(" ")[1]) + 1
      day = int(dates_text.split(" au ")[1].split(" ")[0])
      date2 = date(year, month, day)
      if " " in dates_text.split(" au ")[0]:
        month = MONTHS.index(dates_text.split(" au ")[0].split(" ")[1]) + 1
      day = int(dates_text.split(" au ")[0].split(" ")[0])
      date1 = date(year, month, day)
      delta = date2 - date1
      for i in range(delta.days + 1):
        self.dates.append(date1 + timedelta(days=i))
