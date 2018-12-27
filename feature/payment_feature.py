from feature.base_feature import BaseFeature
from feature.credential_feature import CredentialFeature
from feature.homepage_feature import HomepageFeature
from mapper.credential import M_VOUCHER, LOGIN_BATCH


class PaymentFeature(BaseFeature):

    def __init__(self, driver):
        self.credential = CredentialFeature(driver)
        self.homepage = HomepageFeature(driver)

    #M-VOUCHER_HOME
    def check_remaining_balance(self):
        remain_balance = self.driver.get_Element(M_VOUCHER.TEXT_BALANCE_VALUE)
        value = remain_balance.text
        self.checker.assertEqual(value, remain_balance.text)
        print value

    def press_button_topup_voucher(self):
        button_voucher_pulsa = self.driver.get_Element(M_VOUCHER.BUTTON_PREPAID_PROV)
        button_voucher_pulsa.click()

    def press_button_prepaid_electricity(self):
        button_pre_elec = self.driver.get_Element(M_VOUCHER.BUTTON_PREPAID_ELEC)
        button_pre_elec.click()

    def press_button_back(self):
        button_back = self.driver.get_Element(M_VOUCHER.BUTTON_BACK)
        button_back.click()

    #M-VOUCHER_TRX
    def press_operator_option(self):
        button_operator = self.driver.get_Element(M_VOUCHER.BUTTON_OPERATOR_VOUCHER)
        button_operator.click()

    def input_phone_number(self, custphone):
        input_phone = self.driver.get_Element(M_VOUCHER.INPUT_PHONE)
        input_phone.click()
        input_phone.send_keys(custphone)

    def press_nominal_option(self):
        button_nominal = self.driver.get_Element(M_VOUCHER.BUTTON_NOMINAL)
        button_nominal.click()

    def press_button_next(self):
        button_next = self.driver.get_Element(LOGIN_BATCH.BUTTON_SUBMIT)
        button_next.click()

    def select_option_tsel(self):
        opt_tsel = self.driver.get_Element(M_VOUCHER.LIST_ITEM_TSEL)
        opt_tsel.click()

    def select_option_xl(self):
        opt_xl = self.driver.get_Element(M_VOUCHER.LIST_ITEM_XL)
        opt_xl.click()

    def select_option_indosat(self):
        opt_indosat = self.driver.get_Element(M_VOUCHER.LIST_ITEM_INDOSAT)
        opt_indosat.click()

    def select_option_smartfren(self):
        opt_smartfren = self.driver.get_Element(M_VOUCHER.LIST_ITEM_SMARTFREN)
        opt_smartfren.click()

    def select_option_axis(self):
        opt_axis = self.driver.get_Element(M_VOUCHER.LIST_ITEM_AXIS)
        opt_axis.click()

    def select_option_three(self):
        opt_three = self.driver.get_Element(M_VOUCHER.LIST_ITEM_THREE)
        opt_three.click()

    def press_button_nominal(self):
        button_nominal = self.driver.get_Element(M_VOUCHER.BUTTON_NOMINAL)
        button_nominal.click()

    def select_price_seventh(self):
        button_seventh = self.driver.get_Element(M_VOUCHER.LIST_PRICE_SEVENTH)
        button_seventh.click()

    #step
    def do_select_operator_indosat(self, custphone):
        self.press_button_topup_voucher()
        self.press_operator_option()
        self.select_option_indosat()
        self.input_phone_number(custphone)

    def do_select_nominal(self):
        self.press_nominal_option()
        self.select_price_seventh()

    def do_transaction_prepaid_mdeals_indosat(self, phone, pin, otp, custphone):
        self.credential.do_confirmation_login(phone, pin, otp)
        self.do_select_operator_indosat(custphone)
        self.do_select_nominal()
        self.credential.press_button_submit()
