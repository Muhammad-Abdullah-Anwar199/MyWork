'''for x in iter(lambda: int(input("What's x? ")) , 1):
    try:
        print("You Typed " , x)
    except ValueError:
        print("x is not an interger!")'''

def get_x():
    try:
        return int(input("What's x? "))
    except ValueError:
        print("x is not an integer!")
        return 0   # return something that's NOT 1

for x in iter(get_x, 1):
    print("You Typed", x)
