import re

url = input("what's your twitter URL? ").strip()
url_pattern = r'https:\/\/twitter\.com\/(\w+)' #url string "https://twitter.com/umaramjed"

username = re.sub(url_pattern, r'\1', url)
print (f"your username is, {username}")

