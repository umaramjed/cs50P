import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Define a regex pattern to match YouTube URLs in different formats
    pattern = r'https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)'

    match = re.search(pattern, s)

    if match:
        video_id = match.group(1)
        youtu_be_url = f'https://youtu.be/{video_id}'
        return youtu_be_url
    else:
        return None

if __name__ == "__main__":
    main()
