import time


class Page(object):
    def __init__(self, driver=None):
        self.driver = driver

    def wait(self, seconds=2):
        time.sleep(seconds)

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)
