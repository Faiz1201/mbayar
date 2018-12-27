from feature.credential_feature import CredentialFeature
from runner.base_runner import BaseRunner
from runner.value import long_name, long_address, long_email


class CredentialRunner(BaseRunner):

    def setUp(self):
        BaseRunner.setUp(self)
        self.credential = CredentialFeature(self.driver)

    #Register-Valid
    def test_valid_register(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    #Register-Empty
    def test_invalid_register_empty_phone_mandatory(self):
        self.credential.do_register('088813131414', '', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_empty_name_mandatory(self):
        self.credential.do_register('087787878787', '087787878787', '', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_empty_address_mandatory(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', '', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_empty_email_mandatory(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994', '',
                                    '150194', '150194')

    def test_invalid_register_empty_pin_mandatory(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator,com', '', '150194')

    def test_invalid_register_empty_confirm_pin_mandatory(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '')

    #Register-MaxLength
    def test_invalid_register_max_phone_length(self):
        self.credential.do_register('087787878787', '08778787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_max_fullname_length(self):
        self.credential.do_register('087787878787', '087787878787', long_name, 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_max_address_length(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', long_address, '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_max_email_length(self):
        self.credential.do_register('087878787878', '087878787878', 'Faizal Akbar', 'Jakarta', long_email,
                                    '12 Januari 1994', '150194', '150194')

    def test_invalid_register_max_pin_length(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '1501944', '150194')

    def test_invalid_register_max_repin_length(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '1501944')

    #Registered-Data
    def test_invalid_register_use_registered_phone(self):
        self.credential.do_register('087787878787', '087784292693', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_use_registered_email(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'isal@mailinator.com', '150194', '150194')

    #Invalid-Data
    def test_invalid_register_use_invalid_phone(self):
        self.credential.do_register('087787878787', '454545454545', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '150194')

    def test_invalid_register_use_invalid_email(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'e2pay', '150194', '150194')

    def test_invalid_register_combination_pin(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '123456', '123456')

    def test_invalid_register_false_combination_pin(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '120195')

    #Less-Data
    def test_invalid_register_less_pin(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '12019', '150194')

    def test_invalid_register_less_confirmpin(self):
        self.credential.do_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta', '12 Januari 1994',
                                    'faizal@mailinator.com', '150194', '12019')

    #Invalid-VerificationRegister
    def test_invalid_blank_verification(self):
        self.credential.do_confirmation_register('087787878787', '087787878787', 'Faizal Akbar', '12 Januari 1994',
                                                 'Jakarta', 'faizal@mailinator.com', '150194', '150194', '')

    def test_invalid_false_verification(self):
        self.credential.do_confirmation_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta',
                                                 '12 Januari 1994', 'faizal@mailinator.com', '150194', '150194', '1234')

    def test_invalid_false_verification_three_times(self):
        self.credential.do_confirmation_multiple('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta',
                                                 '12 Januari 1994', 'faizal@mailinator.com', '150194', '150194', '1234')

    def test_invalid_false_verification_less_value(self):
        self.credential.do_confirmation_register('087787878787', '087787878787', 'Faizal Akbar', 'Jakarta',
                                                 '12 Januari 1994', 'faizal@mailinator.com', '150194', '150194', '123')

    #Valid-Login
    def test_valid_login(self):
        self.credential.do_confirmation_login('087776076912', '496351', '1357')

    #Invalid-Login
    def test_invalid_phone_number_login(self):
        self.credential.do_login_batch('712326720821')

    def test_invalid_empty_number_login(self):
        self.credential.do_login_batch('')

    def test_invalid_max_length_phone_login(self):
        self.credential.do_login_batch('08123456789012')

    def test_invalid_pin_login(self):
        self.credential.do_login('087784292693', '121314')

    def test_invalid_pin_login_twice(self):
        self.credential.do_input_pin_twice('087784292693', '121314')

    def test_invalid_pin_login_multiple(self):
        self.credential.do_input_pin_multiple('087784292693', '121314')

    def test_invalid_less_pin_login(self):
        self.credential.do_login('087784292693', '12019')

    def test_invalid_verification_login(self):
        self.credential.do_confirmation_login('087784292693', '150194', '1234')

    def test_invalid_verification_login_twice(self):
        self.credential.do_confirmation_login_twice('087784292693', '150194', '1234')

    def test_invalid_verification_login_three_times(self):
        self.credential.do_confirmation_login_multiple('087784292693', '150194', '1234')

    def test_invalid_less_verification_login(self):
        self.credential.do_confirmation_login('087784292693', '150194', '123')

    #ValidForgot-PIN
    def test_valid_forgot_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '150194', '1234')

    #Max-Length
    def test_invalid_forgot_pin_max_length_phone(self):
        self.credential.do_forgot_pin_continue('08778429269333', 'Jakarta', '12 Januari 1994', '150194', '150194', '1234')

    def test_invalid_forgot_pin_max_length_address(self):
        self.credential.do_forgot_pin_continue('087784292693', long_address, '12 Januari 1994', '150194', '150194', '1234')

    def test_invalid_forgot_pin_max_length_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '1501944', '150194', '1234')

    def test_invalid_forgot_pin_max_length_confirm_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '1501944', '1234')

    def test_invalid_forgot_pin_max_length_verification_code(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '150194', '12345')

    #Empty-Data
    def test_invalid_forgot_pin_empty_mandatory_phone(self):
        self.credential.do_forgot_pin_continue('', 'Jakarta', '12 Januari 1994', '150194', '150194', '1234')

    def test_invalid_forgot_pin_empty_mandatory_address(self):
        self.credential.do_forgot_pin_continue('087784292693', '', '12 Januari 1994', '150194', '150194', '1234')

    def test_invalid_forgot_pin_empty_mandatory_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '', '150194', '1234')

    def test_invalid_forgot_pin_empty_mandatory_confirm_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '150194', '1234')

    #Invalid-Data
    def test_invalid_forgot_pin_combination_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '112233', '112233', '1234')

    def test_invalid_forgot_pin_false_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '150195', '1234')

    def test_invalid_forgot_pin_false_phone_number(self):
        self.credential.do_login_batch('081210109898')

    def test_invalid_forgot_pin_false_date_birth(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '13 Januari 1994', '150194', '150194', '1234')

    def test_invalid_forgot_pin_false_address(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Bekasi', '12 Januari 1994', '150194', '150194', '1234')

    def test_invalid_forgot_pin_false_otp(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '150194', '0000')

    def test_invalid_forgot_pin_false_three_times(self):
        self.credential.do_forgot_pin_verification_multiple('087784292693', 'Jakarta', '12 Januari 1994', '150194',
                                                            '150194', '1234', '1244', '1254')

    #Less-Data
    def test_invalid_forgot_pin_less_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '15019', '150194', '1234')

    def test_invalid_forgot_pin_less_confirm_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '15019', '1234')

    def test_invalid_forgot_pin_less_otp(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '150194', '123')

    #Old-Pin
    def test_invalid_forgot_pin_using_old_pin(self):
        self.credential.do_forgot_pin_continue('087784292693', 'Jakarta', '12 Januari 1994', '150194', '150194', '1234')

