class Show:
  def __init__(self):
    self.location = ""
    self.title = ""
    self.img = ""
    self.link = ""
    self.dates = []

  def to_str(self):
    lines = []
    for d in self.dates:
      lines.append("{};{};{};{};{}".format(self.location, self.title, d, self.img, self.link))
    return "\n".join(lines)
