import os
import unittest
from random import randint

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import TouchActions


class BaseFeature():

    def __init__(self, driver):
        self.driver = driver
        self.checker = unittest.TestCase('__init__')
        self.action = TouchAction(driver)
        self.actions = TouchActions(driver)
        self.driver.implicitly_wait(30)
