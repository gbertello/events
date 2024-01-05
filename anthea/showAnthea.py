import os, sys
from datetime import date

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from show import Show

class ShowAnthea(Show):
  def __init__(self):
    super().__init__()
    self.soup = ""

  def read(self, soup):
    self.soup = soup
    self.read_title()
    self.read_image()
    self.read_link()
    self.read_dates()

  def read_title(self):
    self.title = self.soup.find("h3", {"class": "card__spectacle_title"}).text

  def read_image(self):
    self.img = "https://www.anthea-antibes.fr" + \
               self.soup.find("img").get("src").replace("//", "/")

  def read_link(self):
    self.link = self.soup.find("a", {"class": "card__link"}).get("href")

  def read_dates(self):
    MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin"]
    dates_text = self.soup.find("p", {"class": "card__dates"}).text \
                          .strip() \
                          .replace(" et ", "', ") \
                          .replace("1er", "1") \
                          .replace("'", "") \
                          .replace(",", "")
    self.dates = []
    year = 2024
    for dates_text_by_month in dates_text.split(". "):
      month = MONTHS.index(dates_text_by_month.split(" ")[-1]) + 1

      try:
        days = [int(x) for x in dates_text_by_month.split(" ")[0:-1]]
      except:
        print("Invalid dates: " + dates_text)
        sys.exit(1)

      for day in days:
        self.dates.append(date(year, month, day))

  def to_str(self):
    lines = []
    for d in self.dates:
      lines.append("{};{};{};{}".format(self.title, d, self.img, self.link))
    return "\n".join(lines)
