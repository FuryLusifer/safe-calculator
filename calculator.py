class Calculator:

    def show_welcome_message(self):
        print(f"\n{'-'*15} Calculator App {'-'*15}\n")

    def show_menu(self):
        print("Press 1 to add.")
        print("Press 2 to subtract.")
        print("Press 3 to multiply.")
        print("Press 4 to divide.")
        print("Press 5 to find out the remainder.")
        print("Press 6 to find out the power.")
        print("Press 7 to find out the root.")

    def take_user_input(self):
        user_input_list = []
        print("keep entering numbers to perform your operation (q to quit): ")
        while True:
            user_input = input("-> ")
            if user_input in ['', 'q', 'Q']:
                return user_input_list
            user_input_list.append(float(user_input))

    def add(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.")
            return
        total = numbers[0]
        for num in numbers[1:]:
            total += num
        expression  = " + ".join(str(num) for num in numbers)
        print(f"{expression} = {total}\n")

    def subtract(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.")
            return
        total = numbers[0]
        for num in numbers[1:]:
            total -= num

        expression  = " - ".join(str(num) for num in numbers)
        print(f"{expression} = {total}\n")

    def multiply(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.")
            return
        total = numbers[0]
        for num in numbers[1:]:
            total *= num
        expression  = " * ".join(str(num) for num in numbers)
        print(f"{expression} = {total:.2f}\n")

    def divide(self):
        numbers = self.take_user_input()
        if not numbers:
            print("No numbers entered.")
            return
        total = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Cannot divide by zero.")
                return
            total /= num
        expression = " / ".join(str(num) for num in numbers)
        print(f"{expression} = {total}\n")

    def modulo(self):
        pass

    def power(self):
        pass

    def root(self):
        pass

    def run(self):
        self.show_welcome_message()
        while True:
            self.show_menu()
            user_choice = input("Your Choice: ")

            if user_choice == '1':
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