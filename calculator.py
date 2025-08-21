import sys
class Calculator:

    def show_welcome_message(self):
        print(f"\n{'-'*15} Calculator App {'-'*15}\n")

    def show_menu(self):
        print("Press 0 to exit.")
        print("Press 1 to add.")
        print("Press 2 to subtract.")
        print("Press 3 to multiply.")
        print("Press 4 to divide.")
        print("Press 5 to find out the remainder (modulo).")
        print("Press 6 to find out the power.")
        print("Press 7 to find out the root.")

    def take_user_input(self):
        user_input_list = []
        print("Keep entering numbers to perform your operation (q to stop): ")
        while True:
            user_input = input("-> ")
            if user_input in ['', 'q', 'Q']:
                return user_input_list
            try:
                user_input_list.append(float(user_input))
            except ValueError:
                print("Invalid number, try again.")

    def add(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.\n")
            return
        total = numbers[0]
        for num in numbers[1:]:
            total += num
        expression = " + ".join(str(num) for num in numbers)
        print(f"{expression} = {total:.2f}\n")

    def subtract(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.\n")
            return
        total = numbers[0]
        for num in numbers[1:]:
            total -= num
        expression = " - ".join(str(num) for num in numbers)
        print(f"{expression} = {total:.2f}\n")

    def multiply(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.\n")
            return
        total = numbers[0]
        for num in numbers[1:]:
            total *= num
        expression = " * ".join(str(num) for num in numbers)
        print(f"{expression} = {total:.2f}\n")

    def divide(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.\n")
            return
        total = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Cannot divide by zero.\n")
                return
            total /= num
        expression = " / ".join(str(num) for num in numbers)
        print(f"{expression} = {total:.2f}\n")

    def modulo(self):
        numbers = self.take_user_input()
        if len(numbers) < 2:
            print("Please enter at least two numbers.\n")
            return
        total = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Cannot take modulo with zero.\n")
                return
            total %= num
        expression = " % ".join(str(num) for num in numbers)
        print(f"{expression} = {total:.2f}\n")

    def power(self):
        numbers = self.take_user_input()
        if len(numbers) < 2:
            print("Please enter at least two numbers.\n")
            return
        total = numbers[0]
        for num in numbers[1:]:
            total **= num
        expression = " ** ".join(str(num) for num in numbers)
        print(f"{expression} = {total:.2f}\n")

    def root(self):
        numbers = self.take_user_input()
        if len(numbers) < 2:
            print("Please enter a number and the root value (e.g., 27 and 3).\n")
            return
        num = numbers[0]
        root_value = numbers[1]
        if root_value == 0:
            print("Root value cannot be zero.\n")
            return
        result = num ** (1 / root_value)
        print(f"{num} root {root_value} = {result:.4f}\n")

    def exit_app(self):
        print("Exiting Calculator. Goodbye!!!\n")
        sys.exit()

    def run(self):
        self.show_welcome_message()
        while True:
            self.show_menu()
            user_choice = input("Your Choice: ")

            if user_choice == '0':
                self.exit_app()
            elif user_choice == '1':
                self.add()
            elif user_choice == '2':
                self.subtract()
            elif user_choice == '3':
                self.multiply()
            elif user_choice == '4':
                self.divide()
            elif user_choice == "5":
                self.modulo()
            elif user_choice == "6":
                self.power()
            elif user_choice == "7":
                self.root()
            else:
                print("Wrong input! Try Again !!!\n")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
