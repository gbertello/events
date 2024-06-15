#!/usr/bin/env python3
import os

out = "{};{};{};{};{}\n".format("Location", "Title", "Date", "Image", "Link")

for dir in os.listdir('.'): 
  if "." not in dir and "_" not in dir:
    with open(dir + "/out.csv", "r") as f:
      out += f.read()

with open("out.csv", "w") as f:
  f.write(out)
