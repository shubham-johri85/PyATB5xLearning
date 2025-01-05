class father:
    def home(self):
        print("4bhk")


class son(father):
    def home(self):
        print("2BHK")


Ram = son()
Ram.home()
