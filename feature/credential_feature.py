from feature.base_feature import BaseFeature
from mapper.credential import LOGIN_BATCH, REGISTER_BATCH, VERIFICATION_BATCH, DATE_PICKER, FORGOT_PIN


class CredentialFeature(BaseFeature):

    def check_title_input_phone(self):
        title_input_phone = self.driver.get_Element(LOGIN_BATCH.TEXT_TITLE_PHONE)
        get_title = title_input_phone.text
        self.checker.assertEqual(get_title, title_input_phone.text)
        print get_title

    def check_desc_input_phone(self):
        desc_input_phone = self.driver.get_Element(LOGIN_BATCH.TEXT_DESC_PHONE)
        get_desc = desc_input_phone.text
        self.checker.assertEqual(get_desc, desc_input_phone.text)
        print get_desc

    def input_phone(self, phone):
        et_phone = self.driver.get_Element(LOGIN_BATCH.INPUT_PHONE)
        et_phone.click()
        et_phone.send_keys(phone)
        phone_number = et_phone.text
        self.checker.assertEqual(phone_number, et_phone.text)

    def input_full_name(self, fullname):
        et_fullname = self.driver.get_Element(REGISTER_BATCH.INPUT_FULL_NAME)
        et_fullname.click()
        et_fullname.send_keys(fullname)
        name = et_fullname.text
        self.checker.assertEqual(name, et_fullname.text)

    def input_pin(self, pin):
        et_pin = self.driver.get_Element(LOGIN_BATCH.INPUT_PIN)
        et_pin.click()
        et_pin.send_keys(pin)

    def press_button_submit(self):
        button_submit = self.driver.get_Element(LOGIN_BATCH.BUTTON_SUBMIT)
        button_submit.click()

    def input_phone_register(self, phonereg):
        input_phone = self.driver.get_Element(REGISTER_BATCH.INPUT_PHONE)
        input_phone.click()
        input_phone.send_keys(phonereg)

    def press_button_gender_male(self):
        button_gender_male = self.driver.get_Element(REGISTER_BATCH.BUTTON_GENDER_MALE)
        button_gender_male.click()

    def press_button_gender_female(self):
        button_gender_female = self.driver.get_Element(REGISTER_BATCH.BUTTON_GENDER_FEMALE)
        button_gender_female.click()

    def input_address(self, address):
        input_address = self.driver.get_Element(REGISTER_BATCH.INPUT_BIRTH_PLACE)
        input_address.click()
        input_address.send_keys(address)

    def input_email(self, email):
        input_email = self.driver.get_Element(REGISTER_BATCH.INPUT_EMAIL)
        input_email.click()
        input_email.send_keys(email)

    def input_register_pin(self, pin):
        input_pin = self.driver.get_Element(REGISTER_BATCH.INPUT_PIN)
        input_pin.click()
        input_pin.send_keys(pin)

    def input_confirm_pin(self, repin):
        input_repin = self.driver.get_Element(REGISTER_BATCH.INPUT_CONFIRM_PIN)
        input_repin.click()
        input_repin.send_keys(repin)

    def switch_terms_condition(self):
        cb_terms = self.driver.get_Element(REGISTER_BATCH.CHECKBOX_AGREEMENT)
        cb_terms.is_selected()
        cb_terms.click()

    def press_button_submit_register(self):
        button_submit_register = self.driver.get_Element(REGISTER_BATCH.BUTTON_SUBMIT_SECOND)
        button_submit_register.click()

    def check_title_Confirmation(self):
        title_verification = self.driver.get_Element(VERIFICATION_BATCH.TEXT_VERIFY_INFO)
        get_title_verify = title_verification.text
        self.checker.assertEqual(get_title_verify, title_verification.text)
        print get_title_verify

    def input_verification(self, otp):
        et_verification = self.driver.get_Element(VERIFICATION_BATCH.INPUT_CODE)
        et_verification.click()
        et_verification.send_keys(otp)

    def press_button_confirmation(self):
        button_confirm = self.driver.get_Element(VERIFICATION_BATCH.BUTTON_SUBMIT)
        button_confirm.click()

    def pick_date(self, date):
        click_calendar = self.driver.get_Element(REGISTER_BATCH.BUTTON_DATE)
        click_calendar.click()
        pick_year = self.driver.get_Element(DATE_PICKER.BUTTON_YEAR)
        pick_year.click()
        select_year = self.driver.get_Element(DATE_PICKER.BUTTON_PICK_YEAR)
        select_year.click()
        pick_date = self.driver.find_element_by_accessibility_id(date)
        pick_date.click()
        button_ok = self.driver.get_Element(DATE_PICKER.BUTTON_SUBMIT)
        button_ok.click()

    def check_title_popup(self):
        title_popup = self.driver.get_Element(VERIFICATION_BATCH.TEXT_TITLE_POPUP)
        get_title_popup = title_popup.text
        self.checker.assertEqual(get_title_popup, title_popup.text)
        print get_title_popup

    def check_desc_popup(self):
        desc_popup = self.driver.get_Element(VERIFICATION_BATCH.TEXT_MESSAGE_POPUP)
        get_desc_popup = desc_popup.text
        self.checker.assertEqual(get_desc_popup, desc_popup.text)
        print get_desc_popup

    def scroll_down_page_action(self):
        scroll_element = self.driver.get_Element(REGISTER_BATCH.SCROLL_DOWN)
        self.checker.assertIsNone(scroll_element, 'scrollView exist')
        for x in range(0, 10):
            self.action.press(scroll_element).move_to(x=0, y=-159).perform()

    def scroll_down_page_driver(self):
        origin_el = self.driver.get_Element(REGISTER_BATCH.SCROLL_DOWN)
        destination_el = self.driver.get_Element(REGISTER_BATCH.TARGET)
        self.checker.assertIsNone(origin_el, 'scrollView exist')
        self.driver.scroll(origin_el, destination_el)

    def press_button_confirm_popup(self):
        button_confirm = self.driver.get_Element(VERIFICATION_BATCH.BUTTON_MIDDLE_CONFIRM)
        button_confirm.click()

    def failure_connection(self):
        self.driver.set_network_connection()

    def press_button_forgot_pin(self):
        tl_forgot_pin = self.driver.get_Element(LOGIN_BATCH.TL_FORGOT_PIN)
        tl_forgot_pin.click()

    def input_phone_renew_pin(self, phone):
        input_phone = self.driver.get_Element(FORGOT_PIN.INPUT_FIRST)
        input_phone.click()
        input_phone.send_keys(phone)

    def input_birth_place(self, address):
        input_address = self.driver.get_Element(FORGOT_PIN.INPUT_SECOND)
        input_address.click()
        input_address.send_keys(address)

    def press_button_submit_repin(self):
        button_submit = self.driver.get_Element(FORGOT_PIN.BUTTON_SUBMIT)
        button_submit.click()

    def input_new_pin(self, pin):
        input_pin = self.driver.get_Element(FORGOT_PIN.INPUT_FIRST)
        input_pin.click()
        input_pin.send_keys(pin)

    def input_reconfirm_pin(self, repin):
        input_confirm_pin = self.driver.get_Element(FORGOT_PIN.INPUT_SECOND)
        input_confirm_pin.click()
        input_confirm_pin.send_keys(repin)

    def input_verification_new_pin(self, otp):
        input_otp = self.driver.get_Element(FORGOT_PIN.INPUT_THIRD)
        input_otp.click()
        input_otp.send_keys(otp)

    def press_button_verify_renewpin(self):
        button_verify = self.driver.get_Element(FORGOT_PIN.BUTTON_CONFIRM)
        button_verify.click()

    #Register
    def do_login_batch(self, phone):
        self.check_title_input_phone()
        self.input_phone(phone)
        self.press_button_submit()

    def do_register(self, phone, phonereg, fullname, address, date, email, pin, repin):
        self.do_login_batch(phone)
        self.input_phone_register(phonereg)
        self.input_full_name(fullname)
        self.press_button_gender_male()
        self.input_address(address)
        self.pick_date(date)
        self.input_email(email)
        self.input_register_pin(pin)
        self.input_confirm_pin(repin)
        self.switch_terms_condition()
        self.press_button_submit_register()

    def do_confirmation_register(self, phone, phonereg, fullname, address, date, email, pin, repin, otp):
        self.do_register(phone, phonereg, fullname, address, date, email, pin, repin)
        self.do_confirmation(otp)

    def do_confirmation_multiple(self, phone, phonereg, fullname, address, date, email, pin, repin, otp):
        self.do_register(phone, phonereg, fullname, address, date, email, pin, repin)
        self.do_confirmation(otp)
        self.press_button_confirm_popup()
        self.do_confirmation(otp)
        self.press_button_confirm_popup()
        self.do_confirmation(otp)
        self.press_button_confirm_popup()

    def do_confirmation(self, otp):
        self.check_title_Confirmation()
        self.input_verification(otp)
        self.press_button_confirmation()

    def do_login(self, phone, pin):
        self.do_login_batch(phone)
        self.input_pin(pin)
        self.press_button_submit()

    def do_input_pin_twice(self, phone, pin):
        self.do_login(phone, pin)
        self.press_button_confirm_popup()
        self.do_login(phone, pin)
        self.press_button_confirm_popup()

    def do_input_pin_multiple(self, phone, pin):
        self.do_input_pin_twice(phone, pin)
        self.do_login(phone, pin)
        self.press_button_confirm_popup()

    def do_confirmation_login(self, phone, pin, otp):
        self.do_login(phone, pin)
        self.do_confirmation(otp)

    def do_confirmation_login_twice(self, phone, pin, otp):
        self.do_login(phone, pin)
        self.do_confirmation(otp)
        self.press_button_confirm_popup()
        self.do_confirmation(otp)
        self.press_button_confirm_popup()

    def do_confirmation_login_multiple(self, phone, pin, otp):
        self.do_confirmation_login_twice(phone, pin, otp)
        self.do_confirmation(otp)
        self.press_button_confirm_popup()

    def do_forgot_pin(self, phone):
        self.do_login_batch(phone)
        self.press_button_forgot_pin()

    def do_renew_pin(self, pin, repin, otp):
        self.input_new_pin(pin)
        self.input_reconfirm_pin(repin)
        self.input_verification_new_pin(otp)
        self.press_button_verify_renewpin()

    def do_forgot_pin_continue(self, phone, address, date, pin, repin, otp):
        self.do_forgot_pin(phone)
        self.input_phone_renew_pin(phone)
        self.input_birth_place(address)
        self.pick_date(date)
        self.press_button_submit_repin()
        self.do_renew_pin(pin, repin, otp)

    def do_forgot_pin_verification_multiple(self, phone, address, date, pin, repin, otp, otpa, otpb):
        self.do_forgot_pin_continue(phone, address, date, pin, repin, otp)
        self.input_verification_new_pin(otpa)
        self.press_button_verify_renewpin()
        self.input_verification_new_pin(otpb)
        self.press_button_verify_renewpin()
