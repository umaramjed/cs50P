#n a file called emojize.py,
#implement a program that prompts the user for a str in English
#and then outputs the “emojized” version of that str,
#converting any codes (or aliases) therein to their corresponding emoji.
#:thumbs_up:

import emoji

c = input() # get user input
d = emoji.emojize(c, language="alias")
print(f"Output: {d}")
