import re
emails = open("emails.txt", "r").read().split("\n")
pattern = '^\w+@(gmail.com|mail.ru|icloud.com)$'
for i in emails:
    name, email = i.split()
    email = re.sub("<|>", "", email)
    if re.search(pattern, email): print(name, email)