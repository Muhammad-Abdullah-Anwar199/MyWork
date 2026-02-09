def main():
    number = int(input("Enter a number: "))
    print(square(number))
    nu = int(input("Enter a number: "))
    print(add(nu))
def square(nu):
    return nu + nu

def add(n):
    return n - n

if __name__ == "__main__":
    main()