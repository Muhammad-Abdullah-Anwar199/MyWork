'''for x in iter(lambda: int(input("What's x? ")) , 1):
    try:
        print("You Typed " , x)
    except ValueError:
        print("x is not an interger!")'''

'''def get_x():
    try:
        return int(input("What's x? "))
    except ValueError:
        print("x is not an integer!")
        return 0  ''' # return something that's NOT 1

'''for x in iter(get_x, 1):
    print("You Typed", x)

result = lambda a , b : a+b'''

#print(result(5,5))

'''
def main():
    print(get_int())


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()
'''
# important fact about the "Scope" 
# in python only classes and modules or we can say functions have create the scope
# the loops like while loop and other don't have seprate scope

'''try:
    l = 0
    l = int(input("What's x? "))
except ValueError:
    print("x is not an integer!")
print(f"l is {l}")'''

# now in this case there is no scope issue 
#if the l have the the int(input()) when the input function fails it dos'nt assign to l so when we
# trying to print
#this gives us an error

'''def slove():
    a = "3"
    a *=2 # * do string repition so 33
    z = float(a) + 5.00
    print(f"{z:,.1f}")
slove()

def new():
    s = "abc"
    n = ""
    for x in s:
        print(x)
        n = x + n
    print(n)
'''
try:
