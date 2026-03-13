import re

email = input("What's your email? ").strip()
# ^ means match from the start of the string
# . means match any single character
# + means 1 or more
# * means 0 or more
# $ means at the end of the string
# [] means, we can check for the combinition of the words like [^@] any character expect "@"
# \. matches exact character

if re.search(r"^[^@].+@[^@]+\.edu$" , email):
    print("Valid")
else:
    print("Invalid")