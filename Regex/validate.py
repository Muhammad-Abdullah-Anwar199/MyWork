email = input("What's your email? ").strip()

username , domain = email.split("@")
print(username,domain)
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")