from BrowserPackage.OpenBrowser import startbrowser
from BrowserPackage.StopBrowser import closebrowser



class TestCase:
    def tc1(self):
        startbrowser()
        print("Execution")
        closebrowser()

Result1=TestCase()
Result1.tc1()