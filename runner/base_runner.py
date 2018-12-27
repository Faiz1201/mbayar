import os
import unittest
from random import randint

from runner.driver import Driver


class BaseRunner(unittest.TestCase):

    def setUp(self):
        self.driver = Driver.set_driver()

    def tearDown(self):
        directory = '%s/' % os.getcwd()
        file_name = 'e2pay' + str(self.rand_num(3)) + '.png'
        self.driver.save_screenshot(directory + file_name)
        self.driver.quit()

    def rand_num(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)
