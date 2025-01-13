from abc import ABC, abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def readfromexcel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class TC01(Browser):
    def start(self):
        print("open chrome")

    def readfromexcel(self):
        print("fetch the data from excel")

    def stop(self):
        print("close the chrome")

    def execute(self):
        self.start()
        self.readfromexcel()
        self.stop()

test1=TC01()
test1.execute()
