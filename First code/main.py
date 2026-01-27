def main():
    name = input("What's your name? ")
    match name:
        case "Abdullah":
            print("199")
        case _:
            print("Who?")
main()

def main():
    i = 1
    while i <= 3:
        print("meow")
        i = i + 1
main()

def main():
    for _ in range(3):
        print("Meow" , _)
main()
n = int(input("What's n?"))
print("Meow\n" * n , end="")

students = ["Abdullah" , "Rafay" ,"Raheem" , 6]
for i in students:
    print("[",i, sep="," ,end="" )
print()
for i in [1,4,6]:
    print(i)