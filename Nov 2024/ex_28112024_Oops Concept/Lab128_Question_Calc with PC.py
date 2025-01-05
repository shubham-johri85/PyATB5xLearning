class calc:
    def __init__(self, a, b):
        print("Parameterized Constructor")
        self.a=a
        self.b=b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


ref_calc = calc(9,8)
# Sum=ref_calc.sum()
# Sub=ref_calc.sub()
# Mul=ref_calc.mul()
# Div=ref_calc.div()
print(ref_calc.sum(), ref_calc.sub(), ref_calc.mul(), ref_calc.div())
