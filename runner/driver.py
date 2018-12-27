import time
from appium.webdriver.webdriver import WebDriver
import resource.res_android
from mapper.basemapper import ID, ACCESS_ID, NAME_ID, XPATH, CLASS_ID


class Driver(WebDriver):

    @staticmethod
    def set_driver():
        desired_caps = resource.res_android.get_desired_capabilities('mbayar.apk')
        driver = Driver('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(4)
        return driver

    def get_Id(self, data):
        return self.find_element_by_id(data)

    def acc_Id(self, data):
        return self.find_element_by_accessibility_id(data)

    def name_Id(self, data):
        return self.find_element_by_name(data)

    def class_Id(self, data):
        return self.find_element_by_class_name(data)

    def xpath(self, data):
        return self.find_element_by_xpath(data)

    def get_Element(self, data):
        if data[0] == ID:
            return self.find_element_by_id(data[1])
        elif data[0] == ACCESS_ID:
            return self.find_element_by_accessibility_id(data[1])
        elif data[0] == NAME_ID:
            return self.find_element_by_name(data[1])
        elif data[0] == CLASS_ID:
            return self.find_element_by_class_name([1])
        elif data[0] == XPATH:
            return self.find_element_by_xpath(data[1])
        else:
            raise NotImplementedError()
