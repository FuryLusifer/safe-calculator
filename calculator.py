import os

# -------------------- Custom Exceptions --------------------

class CalculatorError(Exception):
    """Base class for calculator errors"""
    pass

class InputError(CalculatorError):
    """Raised when user input is invalid"""
    pass

class CalculationError(CalculatorError):
    """Raised when a calculation goes wrong (like division by zero)"""
    pass


class Calculator:
    # -------------------- Initialization --------------------
    def __init__(self):
        self.history_file = "history.txt"
        self.history = []
        self.load_history_from_file()

    # -------------------- Messages & Menu --------------------
    def show_welcome_message(self):
        print(f"\n{'-'*15} Calculator App {'-'*15}\n")

    def show_menu(self):
        print("Press 0 to exit.")
        print("Press 1 to add.")
        print("Press 2 to subtract.")
        print("Press 3 to multiply.")
        print("Press 4 to divide.")
        print("Press 5 to find remainder (modulo).")
        print("Press 6 to power (exponent).")
        print("Press 7 to root.")
        print("Press 8 to view history.")
        print("Press 9 to clear history.")

    # -------------------- History Handling --------------------
    def load_history_from_file(self):
        """Load history from file if it exists"""
        try:
            with open(self.history_file, "r") as f:
                self.history = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.history = []

    def save_to_history(self, record):
        """Save a record to memory and file"""
        self.history.append(record)
        with open(self.history_file, "a") as f:
            f.write(record + "\n")

    def view_history(self):
        if not self.history:
            print("No history yet.\n")
        else:
            print("\n--- Calculation History ---")
            for record in self.history:
                print(record)
            print()

    def clear_history(self):
        """Clear history in memory and remove file"""
        self.history = []
        if os.path.exists(self.history_file):
            open(self.history_file, "w").close()  # empty file
        print("History cleared!\n")

    # -------------------- Input Handling --------------------
    def take_user_input(self):
        """Collects multiple numbers from user until q/Enter"""
        user_input_list = []
        print("Keep entering numbers to perform your operation (q to stop): ")
        while True:
            user_input = input("-> ")
            if user_input in ['', 'q', 'Q']:
                return user_input_list
            try:
                user_input_list.append(float(user_input))
            except ValueError:
                raise InputError(f"Invalid number entered: {user_input}")

    # -------------------- Core Operation Helper --------------------
    def perform_operation(self, operator, func, requires_two=False, special_format=False):
        """
        Generic operation handler to reduce repetition.
        operator: str (symbol like '+', '-', '*', '/')
        func: lambda for operation logic
        requires_two: whether at least 2 numbers are required
        special_format: if True, show 4 decimals instead of 2
        """
        numbers = self.take_user_input()
        if not numbers:
            raise InputError("No numbers entered.")
        if requires_two and len(numbers) < 2:
            raise InputError(f"{operator} operation requires at least two numbers.")

        total = numbers[0]
        for num in numbers[1:]:
            total = func(total, num)

        expression = f" {operator} ".join(str(num) for num in numbers)
        decimals = 4 if special_format else 2
        result_str = f"{expression} = {total:.{decimals}f}"
        print(result_str, "\n")
        self.save_to_history(result_str)

    # -------------------- Specific Operations --------------------
    def add(self):
        self.perform_operation("+", lambda x, y: x + y)

    def subtract(self):
        self.perform_operation("-", lambda x, y: x - y)

    def multiply(self):
        self.perform_operation("*", lambda x, y: x * y)

    def divide(self):
        def safe_div(x, y):
            if y == 0:
                raise CalculationError("Division by zero is not allowed.")
            return x / y
        self.perform_operation("/", safe_div)

    def modulo(self):
        def safe_mod(x, y):
            if y == 0:
                raise CalculationError("Modulo by zero is not allowed.")
            return x % y
        self.perform_operation("%", safe_mod, requires_two=True)

    def power(self):
        self.perform_operation("**", lambda x, y: x ** y, requires_two=True)

    def root(self):
        def root_func(x, y):
            if y == 0:
                raise CalculationError("Root value cannot be zero.")
            return x ** (1 / y)
        self.perform_operation("root", root_func, requires_two=True, special_format=True)

    # -------------------- Exit App --------------------
    def exit_app(self):
        print("Exiting Calculator. Goodbye!\n")
        raise SystemExit

    # -------------------- Run Loop --------------------
    def run(self):
        self.show_welcome_message()
        actions = {
            '0': self.exit_app,
            '1': self.add,
            '2': self.subtract,
            '3': self.multiply,
            '4': self.divide,
            '5': self.modulo,
            '6': self.power,
            '7': self.root,
            '8': self.view_history,
            '9': self.clear_history,
        }

        while True:
            self.show_menu()
            user_choice = input("Your Choice: ")

            try:
                action = actions.get(user_choice)
                if action:
                    action()
                else:
                    print("Wrong input! Try Again !!!\n")

            except CalculatorError as e:
                print(f"Error: {e}\n")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()