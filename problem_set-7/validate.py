import re

email = input('Whats your email? ').strip()

email_rex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' # regex for email address, 'r' indicates raw string

if re.search(email_rex, email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')





'''username, domain = email.split("@")
print (f"username is {username} and domain is {domain}")'''


'''if "@" in email and "." in email:
    print("Valid Email")
else:
    print("This is not an email address")'''
