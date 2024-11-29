class calc:
    def __init__(self):
        print("Default Constructor")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


ref_calc = calc()
a = float(input("Enter the value of a-->"))
b = float(input("Enter the value of b-->"))

Sum = ref_calc.sum(a,b)
Sub = ref_calc.sub(a,b)
Mul = ref_calc.mul(a,b)
Div = ref_calc.div(a,b)
print(Sum, Sub, Mul, Div)