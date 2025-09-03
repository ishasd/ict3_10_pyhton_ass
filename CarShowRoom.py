class Cars:
    def __init__(self, car_id, brand, model, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Id: {self.car_id} | {self.brand} {self.model} - Rs.{self.price}"

car_inventory = []

# crud operations ------------------

def createCar():
    car_id = int(input("enter car id:"))
    brand = input("Enter brand:")
    model = input("enter model:")
    price = int(input("enter price:"))
    car = Cars(car_id, brand, model, price)
    car_inventory.append(car)
    print("car added")


def viewCars():
    if not car_inventory:
        print("no cars available")
    else:
        for car in car_inventory:
            print(car.display_info())


def updateCar():
    car_id = int(input("enter car id you want to update: "))
    for car in car_inventory:
        if car.car_id == car_id:
            print("leave blank if you don't want to update")
            new_brand = input(f"enter new brand: (current: {car.brand}): ") or car.brand
            new_model = input(f"enter new model: (current: {car.model}): ") or car.model
            new_price = input(f"enter new price: (current: {car.price}): ") or car.price

            car.brand = new_brand
            car.model = new_model
            car.price = int(new_price)

            print("car updated")
            return 
    print("car not found")


def deleteCar():
    car_id = int(input("enter car id you want to delete: "))
    for car in car_inventory:
        if car.car_id == car_id:
            car_inventory.remove(car)
            print("car deleted")
    print("car not found")




def operations():
    while True:
        print("\ncar showroom crud operations")
        print("1. Add new car")
        print("2. view cars")
        print("3. update car")
        print("4. remove car")
        print("5. Exit")

        choice = int(input("enter you choice (1-5):"))

        if choice == 1:
            createCar()
        elif choice == 2:
            viewCars()
        elif choice == 3 :
            updateCar()
        elif choice == 4:
            deleteCar()
        elif choice == 5 :
            print("Exit")
            break
        else:
            print("invalid choice. try again")





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
        
        operations()
        # print(f"\n Hello {name}, available cars list:\n")

        # cars = [
        #     LuxuryCars("Mercedes", "S-class", 1500000, "Massage seats"),
        #     LuxuryCars("BMW", "7 series", 1400000, "Panaromic Sunroof"),                SportCars("Ferrari", "488-GTB", 3000000, 330),
        #     SportCars("Lamborghini", "Huracan", 3200000, 325)
        # ]

        # for car in cars : 
        #     print(car.display_info())

    except IncomeLowException as e:
        print("Access denied:", e)


if __name__ == "__main__":
    showroom()