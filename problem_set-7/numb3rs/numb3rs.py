import re
import sys

def validate(ip):
    ipv4_pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    ipv4_pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    ipv4_pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    ipv4_pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    is_valid = re.search(ipv4_pattern, ip)
    if is_valid:
        return True
    else:
        return False

def main():
    user_input = input("IPv4 Address: ")

    if validate(user_input):
        print("True")
        sys.exit(1)
    else:
        print("False")
        sys.exit(1)

if __name__ == "__main__":
    main()



...


if __name__ == "__main__":
    main()

