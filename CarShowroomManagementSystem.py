class SalaryTooLowException(Exception):
    def __init__(self, message="Access Denied: Salary must be at least Rs. 100000 to view car details."):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, brand, model, price, fuel_type, transmission, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.color = color

    def display_summary(self):
        return f"{self.brand} {self.model} - Rs.{self.price}"

    def display_details(self):
        details = (
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Price: Rs.{self.price}\n"
            f"Fuel Type: {self.fuel_type}\n"
            f"Transmission: {self.transmission}\n"
            f"Color: {self.color}"
        )
        return details

class Showroom:
    def __init__(self):
        self.__inventory = []

    def view_cars(self):
        if not self.__inventory:
            print("\nNo cars available in the showroom.")
        else:
            print("\nAvailable Cars in Showroom:")
            for idx, car in enumerate(self.__inventory, start=1):
                print(f"{idx}. {car.display_summary()}")

    def display_car_details(self, model_name, user_salary):
        if user_salary < 100000:
            raise SalaryTooLowException()

        for car in self.__inventory:
            if car.model.lower() == model_name.lower():
                print("\nCar Details:")
                print(car.display_details())
                return
        print("\nCar model not found.")

    def sell_car(self, model_name):
        for car in self.__inventory:
            if car.model.lower() == model_name.lower():
                self.__inventory.remove(car)
                print(f"\nCar model '{model_name}' sold successfully!")
                return
        print("\nCar model not found in inventory.")

    def buy_car(self, car):
        self.__inventory.append(car)
        print(f"\nCar model '{car.model}' added to inventory successfully.")


def main():
    showroom = Showroom()

    while True:
        print("\n--- Car Showroom Management System ---")
        print("1. View Available Cars")
        print("2. Display Car Details")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            showroom.view_cars()

        elif choice == '2':
            try:
                model_name = input("Enter Car Model Name to view details: ")
                salary = int(input("Enter your salary (Rs.): "))
                showroom.display_car_details(model_name, salary)
            except SalaryTooLowException as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: Invalid salary input.")

        elif choice == '3':
            model_name = input("Enter Car Model Name to sell: ")
            showroom.sell_car(model_name)

        elif choice == '4':
            try:
                brand = input("Enter Car Brand: ")
                model = input("Enter Car Model: ")
                price = int(input("Enter Price (Rs.): "))
                fuel_type = input("Enter Fuel Type (Petrol/Diesel/Electric): ")
                transmission = input("Enter Transmission (Manual/Automatic): ")
                color = input("Enter Color: ")

                new_car = Car(brand, model, price, fuel_type, transmission, color)
                showroom.buy_car(new_car)
            except ValueError:
                print("Error: Invalid input. Price must be a number.")

        elif choice == '5':
            print("Exiting Car Showroom System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
