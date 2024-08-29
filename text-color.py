import colors
blackcolor=colors.blackcolor
def colorinput(text="", color=blackcolor):
  if color == "black":
    input(text)
  elif color == "red":
    input(f"\033[31m{text}")
  else:
    return False
