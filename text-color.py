redcolor = "red"
yellowcolor = "yellow"
bluecolor = "blue"
whitecolor = "white"
def colorinput(text="", color=whitecolor):
  if color == "white":
    input(text)
  elif color == "red":
    input(f"\033[31m{text}")
