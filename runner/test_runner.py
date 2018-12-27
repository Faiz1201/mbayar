import unittest
from feature.test_feature import TestFeature
from runner.base_runner import BaseRunner


class TestRunner(BaseRunner):

    def setUp(self):
        BaseRunner.setUp(self)
        self.test = TestFeature(self.driver)

    def test_do_welcome_login(self):
        self.test.do_welcome_login('faizal', 'e2pay')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRunner)
    unittest.TextTestRunner(verbosity=2).run(suite)
