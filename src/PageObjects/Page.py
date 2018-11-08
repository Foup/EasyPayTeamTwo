from selenium import webdriver
import time


class Page():

    def __init__(self, driver):
        self.driver = driver

    def wait(self, seconds=2):
        time.sleep(seconds)