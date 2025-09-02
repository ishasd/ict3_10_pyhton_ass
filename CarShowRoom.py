class Cars:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"{self.brand} {self.model} - Rs.{self.price}"


class LuxuryCars(Cars):
    def __init__(self, brand, model, price, feature):
        super().__init__(brand, model, price)
        self.feature = feature

    def display_info(self):
        return f"[Luxury] {super().display_info()} | Feature: {self.feature}"

class SportCars(Cars):
    def __init__(self, brand, model, price, topSpeed):
        super().__init__(brand, model, price)
        self.topSpeed = topSpeed

    def display_info(self):
        return f"[Sports] {super().display_info()} | top Speed: {self.topSpeed} km/h"


class IncomeLowException(Exception):
    """Custom exception when client's income is low"""
    pass


def showroom():
    print("Welcome to the car showroom..")
    name = input("enter your name:")
    age = int(input("enter your age:"))
    income = int(input("enter your annual income:"))

    try:
        if income<100000:
            raise IncomeLowException("Income is less than eligibility amount")

        print(f"\n Hello {name}, available cars list:\n")

        cars = [
            LuxuryCars("Mercedes", "S-class", 1500000, "Massage seats"),
            LuxuryCars("BMW", "7 series", 1400000, "Panaromic Sunroof"),                SportCars("Ferrari", "488-GTB", 3000000, 330),
            SportCars("Lamborghini", "Huracan", 3200000, 325)
        ]

        for car in cars : 
            print(car.display_info())

    except IncomeLowException as e:
        print("Access denied:", e)


if __name__ == "__main__":
    showroom()