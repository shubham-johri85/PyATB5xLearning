class ExcelReader:
    @staticmethod
    def readfromexcel():
        print("Reading from Excel")


class MySQLDBConnection:
    @staticmethod
    def readMYSQLfile():
        print("MySQL")


class TC01:

    def test(self):
        ExcelReader.readfromexcel()
        MySQLDBConnection.readMYSQLfile()


run = TC01()
run.test()
