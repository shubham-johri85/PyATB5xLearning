class base_test:
    def open_browser(self):
        print("Starting the browser")

    def close_browser(self):
        print("close the browser")

    def read_from_excel(self):
        print("Read data from excel")


class TestCase1(base_test):
    def test1(self):
        self.open_browser()
        print("Executed TC 1")
        self.read_from_excel()
        self.close_browser()


class TestCase2(base_test):
    def test2(self):
        self.open_browser()
        print("Executed TC 2")
        self.read_from_excel()
        self.close_browser()


TC1 = TestCase1()
TC1.test1()

TC2 = TestCase2()
TC2.test2()
