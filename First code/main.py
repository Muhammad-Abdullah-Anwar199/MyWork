'''from pkgutil import resolve_name

def main():
    name = input("What's your name? ")
    match name:
        case "Abdullah":
            print("199")
        case _:
            print("Who?")


def main():
    iop= 1
    while iop <= 3:
        print("meow")
        iop = iop + 1

def main():
    for _ in range(3):
        print("Meow" , _)


n = int(input("What's n?"))
print("Meow\n" * n , end="")

students = ["Abdullah" , "Rafay" ,"Raheem" , 6]
for i in students:
    print("[",i, sep="," ,end="" )
print()
for i in [1,4,6]:
    print(i)


def main():
    family = {
        "Abdullah" : "Shami House" ,
        "ALi " : "Goraya's House"
}
    for i in family:
        print(i , family[i] , sep="->")


students = [
{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
{"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
{"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"] , student["house"] , student["patronus"])


print("#" * 3 , end="")

def main():
    col = print_column(0)
    rows = print_rows(0)

    print(rows)
    print(col)

    print("*" * 0)
    print("*" * 0)

    print_square(3)

def print_column(width):
    return "*" * width

def print_rows(height):
    return "*" * height

def print_square(size):
    #for each row in square.
    for _ in range(size):
        #for each brick in rows
        for _ in range(size):
            #print bricks
            print("#" , end="")
        print() #this is for simple line switch



def pattern(size):
    for _ in range(size):
        print("#" * size)



def pyramids(n):
    #No of rows
    for i in range(1, n+1):
        #spaces
        for j in range(n-i):
            print(" " , end="")
        #stars
        for k in range(2*i-1):
            print("*" , end="")
        print()
'''

'''def hollowSquare(n):
    #for rows
    for i in range(1,n+1):
    #for stars
        for j in range(1,n+1):
            if i == 1 or i == n or j == 1 or j == n:
                print("#" , end="")
            else:
                print(" ",end="")
        print()
hollowSquare(7)'''

try:
    int("cat")
except ValueError:
    print("Logging error...")
    raise
