def bank(prompt):
    if prompt.startswith("hello"):
        print("$0")
    elif prompt.startswith('h') and prompt != "hello":
        print("$20")
    else:
        print("$100")

user = input("Greeting: ").strip().lower()
bank(user)