import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return (re.match(pattern, email) !=None)

email = "gmail@example.com"
print(is_valid_email(email))  # True

