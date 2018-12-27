from feature.base_feature import BaseFeature
from mapper.credential import HOMEPAGE


class HomepageFeature(BaseFeature):

    def check_logo_mbayar(self):
        img_mbayar = self.driver.get_Element(HOMEPAGE.IMG_HOME_LOGO)
        self.checker.assertIsNotNone(img_mbayar, 'LOGO Available')

    def check_customer_name(self):
        desc_username = self.driver.get_Element(HOMEPAGE.TEXT_CUSTOMER_NAME)
        username = desc_username.text
        self.checker.assertEqual(username, desc_username.text)
        print username

    def check_account_type(self):
        desc_type = self.driver.get_Element(HOMEPAGE.TEXT_ACCOUNT_TYPE)
        acc_type = desc_type.text
        self.checker.assertEqual(acc_type, desc_type.text)
        print acc_type

    def check_user_phone(self):
        user_phone = self.driver.get_Element(HOMEPAGE.TEXT_CUSTOMER_ID)
        phone_number = user_phone.text
        self.checker.assertEqual(phone_number, user_phone.text)
        print phone_number

    def check_remaining_balance(self):
        remain_balance = self.driver.get_Element(HOMEPAGE.TEXT_BALANCE_REMAINING)
        value = remain_balance.text
        self.checker.assertEqual(value, remain_balance.text)
        print value

    def press_button_refresh_saldo(self):
        refresh_value = self.driver.get_Element(HOMEPAGE.BUTTON_REFRESH)
        refresh_value.click()

    def press_button_top_up_saldo(self):
        topup_value = self.driver.get_Element(HOMEPAGE.BUTTON_TOPUP)
        topup_value.click()

    def press_button_history_transaction(self):
        history_trx = self.driver.get_Element(HOMEPAGE.BUTTON_HISTORY)
        history_trx.click()

    def press_button_mVoucher(self):
        button_menu1 = self.driver.get_Element(HOMEPAGE.BUTTON_VOUCHER)
        button_menu1.click()

    def press_button_mBills(self):
        button_menu2 = self.driver.get_Element(HOMEPAGE.BUTTON_BILLS)
        button_menu2.click()

    def press_button_mShop(self):
        button_menu3 = self.driver.get_Element(HOMEPAGE.BUTTON_SHOP)
        button_menu3.click()

    def press_button_mTransfer(self):
        button_menu4 = self.driver.get_Element(HOMEPAGE.BUTTON_TRANSFER)
        button_menu4.click()

    def press_button_mDonation(self):
        button_menu5 = self.driver.get_Element(HOMEPAGE.BUTTON_DONATION)
        button_menu5.click()

    def press_button_mPromo(self):
        button_menu6 = self.driver.get_Element(HOMEPAGE.BUTTON_PROMO)
        button_menu6.click()

    def press_button_mEdu(self):
        button_menu7 = self.driver.get_Element(HOMEPAGE.BUTTON_EDUCATION)
        button_menu7.click()

    def press_button_mServices(self):
        button_menu8 = self.driver.get_Element(HOMEPAGE.BUTTON_SERVICES)
        button_menu8.click()
