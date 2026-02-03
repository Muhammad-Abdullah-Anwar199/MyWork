def main():
    while True:
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("0. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            print("Goodbye!")
            break
        
        # Map choice to operation
        operations = {1: "+", 2: "-", 3: "*", 4: "/"}
        
        if choice in operations:
            x = int(input("Enter x: "))
            z = int(input("Enter z: "))
            op = operations[choice]  # get the operation symbol
            calculator(x, op, z)
        else:
            print("Invalid choice. Try again.")

def calculator(x, y, z):
    match y:
        case '+':
            print(f"{x} + {z} = {x+z}")
        case '-':
            print(f"{x} - {z} = {x-z}")
        case '*':
            print(f"{x} * {z} = {x*z}")
        case '/':
            if z == 0:
                print("Cannot divide by zero!")
            else:
                print(f"{x} / {z} = {x/z}")
        case _:
            print("Unknown operation")
main()


text = "hello"
print("he" in text)  # True
print("hi" in text)  # False

list = [1,2,4,5,2,4,5,3,4,53,453]
print(7 in list)
#mini excercise
x = print("Hello")
print(x)
