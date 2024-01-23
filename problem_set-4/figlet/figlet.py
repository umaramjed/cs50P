import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv1 = ["-f", "--font"]


def main():
    if len(sys.argv) < 2: # if there is no commandline argument then get a random font
        font = random.choice(figlet.getFonts())
        figletize("Input: ", font) #random font
    elif len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        sys.exit("Invalid usage")


def figletize(prompt, f):
    x = input(prompt)
    figlet.setFont(font=f)
    print(figlet.renderText(x))


main()



