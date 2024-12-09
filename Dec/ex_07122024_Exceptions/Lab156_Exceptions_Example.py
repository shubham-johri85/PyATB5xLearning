# Exception handle under class

class ABC:

    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter only integer value of a")
        else:
            print("a")
        finally:
            print("Try again")


Obj_ref = ABC()
Obj_ref.f1()

