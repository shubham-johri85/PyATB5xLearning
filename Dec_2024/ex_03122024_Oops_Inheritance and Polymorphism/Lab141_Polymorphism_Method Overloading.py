#Method Overloading
"""
Python doesn't support method overloading in the traditional sense,
like some other languages such as Java or C++. However, 
you can achieve similar functionality using default arguments or variable-length arguments. 
Here's a simple example:
"""

class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(a,b)
        elif a is not None:
            print(a)
        else:
            print("No arguments")

obj = Example()
obj.display()
obj.display(10)
obj.display(10, 20)


