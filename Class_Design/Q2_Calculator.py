

ADD = '+'
SUBTRACT = '-'
EVALUATE = '='
CLEAR = 'c'


class Calculator:
    def __init__(self) -> None:
        self.num_before_operation = None
        self.operation = None
        self.num_after_operation = None

    def evaluate_result(self):
        can_evaluate_result = self.num_before_operation is not None and self.operation is not None and self.num_after_operation is not None

        if not can_evaluate_result: return None

        if self.operation == '+':
            return self.num_before_operation + self.num_after_operation

        elif self.operation == '-':
            return self.num_before_operation - self.num_after_operation

    def update_num(self, key):
        if self.num_before_operation is not None and self.operation is not None:
            self.num_after_operation = int(key)
            return

        self.num_before_operation = int(key)

    
    def keyPress(self, key):

        if key == CLEAR:
            self.num_before_operation = None
            self.operation = None
            self.num_after_operation = None

        elif key == ADD:
            self.operation = ADD

        elif key == SUBTRACT:
            self.operation = SUBTRACT

        elif key == EVALUATE:
            evaluation_result = self.evaluate_result()

            if evaluation_result is None:
                return None

            self.num_before_operation = evaluation_result
            self.operation = None
            self.num_after_operation = None

            return evaluation_result

        else:
            if type(key) is not int and not key.isdigit():
                print('Error: invalid input, you must enter 0-9, +, -, c, =')
                return
            
            self.update_num(key)

            return key


if __name__ == "__main__":
    calc = Calculator()

    # Test 1
    calc.keyPress('5')
    calc.keyPress('+')
    calc.keyPress('7')
    result = calc.keyPress('=')
    print(f"Expected: {12} Your code's output: {result}")

    calc.keyPress('c')

    # Test 2
    calc.keyPress('7')
    calc.keyPress('-')
    calc.keyPress('5')
    result = calc.keyPress('=')
    print(f"Expected: {2} Your code's output: {result}")
    calc.keyPress('c')

    # Test 3
    calc.keyPress('15')
    calc.keyPress('+')
    calc.keyPress('3')
    result = calc.keyPress('=')
    print(f"Expected: {18} Your code's output: {result}")
    calc.keyPress('-')
    calc.keyPress('7')
    result = calc.keyPress('=')
    print(f"Expected: {11} Your code's output: {result}")
    calc.keyPress('c')

    # Test 4
    calc.keyPress(15)
    calc.keyPress('+')
    calc.keyPress(3)
    result = calc.keyPress('=')
    print(f"Expected: {18} Your code's output: {result}")
    calc.keyPress('-')
    calc.keyPress(7)
    result = calc.keyPress('=')
    print(f"Expected: {11} Your code's output: {result}")
    calc.keyPress('c')

    # Test 5
    calc.keyPress('15a')
    calc.keyPress('+')
    calc.keyPress('5')
    result = calc.keyPress('=')
    print(f"Expected: {None} Your code's output: {result}")

            

