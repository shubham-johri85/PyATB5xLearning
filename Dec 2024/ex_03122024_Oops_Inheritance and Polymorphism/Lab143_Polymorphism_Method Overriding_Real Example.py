class OldBrowser:

    def start_browser(self):
        print("start IE")

    def stop_browser(self):
        print("Stop IE")


class Browser(OldBrowser):
    def start_browser(self):  # ---> Method Overriding
        super().start_browser() # ---> Here we call start_browser method from parent so o/p will add start IE also
        print("start Chrome")

    def stop_browser(self):  # ---> Method Overriding
        print("Stop Chrome")


IE = Browser()
IE.start_browser()
IE.stop_browser()
