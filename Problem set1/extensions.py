def starts(prefix):
    return prefix[len(prefix):] == prefix

def extensions(prompt):
    if prompt.endswith("gif"):
        print("image/gif")
    elif prompt.endswith("jpg"):
        print("image/jpeg")
    elif prompt.endswith("jpeg"):
        print("image/jpeg")
    elif prompt.endswith("png"):
        print("image/png")
    else:
        print("nothing")
extensions("cat.png")