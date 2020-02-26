
"""https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem"""

# obvious one using regex
import re
def fun(s):       
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

""" or 

def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True

n = int(input())
emails = [input() for email in range(n)]

valid = list(filter(check_valid, emails))
print(sorted(valid))

"""