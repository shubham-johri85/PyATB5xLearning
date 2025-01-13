"""
It is a special method that belongs to class rather than instance.
We can directly call the method with class name without creating object of it.
@staticmethod decorator is used to define it
"""


class SM:
    @staticmethod
    def sum(a, b):  # - Static Method
        return a + b

    def mul(self, a, b): # -- NonStatic Method
        return a * b


print(SM.sum(4, 2))

NM=SM()
print(NM.mul(4,8))

