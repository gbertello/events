#!/usr/bin/env python3

out = "{};{};{};{};{}\n".format("Location", "Title", "Date", "Image", "Link")

with open("anthea/out.csv", "r") as f:
  out += f.read()

with open("le-tribunal/out.csv", "r") as f:
  out += f.read()

with open("out.csv", "w") as f:
  f.write(out)
