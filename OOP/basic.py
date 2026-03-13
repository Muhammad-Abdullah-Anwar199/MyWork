class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
    #this is only for returing string that why it named (str)
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
    #function = decorator(function)
    @property
    def brand(self):
        return self.__brand


if __name__ == "__main__":
    c1 = Car("Toyota", "Corolla", 2022)
    print(c1.brand)