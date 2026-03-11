class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


if __name__ == "__main__":
    c1 = Car("Toyota", "Corolla", 2022)
    print(c1._Car__model)