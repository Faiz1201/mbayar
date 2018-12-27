from feature.base_feature import BaseFeature
from mapper.credential import test


class TestFeature(BaseFeature):

    def input_username(self, name):
        username = self.driver.get_Element(test.TEXT_USERNAME)
        username.click()
        username.send_keys(name)

    def input_password(self, password):
        ipassword = self.driver.get_Element(test.TEXT_PASSWORD)
        ipassword.click()
        ipassword.send_keys(password)

    def button_submit(self):
        button_submit = self.driver.get_Element(test.BUTTON_SUBMIT)
        button_submit.click()

    def result_test(self):
        result_test = self.driver.get_Element(test.TEXT_WELCOME)
        self.checker.assertEqual('SELAMAT BELAJAR AUTOMATION QA INFINETWORKS', result_test.text)
        print result_test

    def do_welcome_login(self, name, password):
        self.input_username(name)
        self.input_password(password)
        self.button_submit()
        self.result_test()
