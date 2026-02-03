def main():
    prompt = input("What is the answer to the Great Question of life, universe , and Everthing? ").strip().lower()
    if prompt == "42":
        print("Yes!")
    elif prompt == "forty two":
        print("Yes!")
    elif prompt == "forty-two":
        print("Yes!")
    else:
        print("NO!")
main()