from mapper.basemapper import ID, XPATH, CLASS_ID, ACCESS_ID


class test:
    TEXT_USERNAME = (ID, 'com.tabunganku.debug.tabunganku:id/et_username')
    TEXT_PASSWORD = (ID, 'com.tabunganku.debug.tabunganku:id/et_password')
    BUTTON_SUBMIT = (ID, 'com.tabunganku.debug.tabunganku:id/btn_submit')
    TEXT_WELCOME = (ID, 'com.tabunganku.debug.tabunganku:id/tv_welcome')

class LOGIN_BATCH:
    TEXT_TITLE_PHONE = (ID, 'com.mbayar:id/tv_title')
    TEXT_DESC_PHONE = (ID, '')
    INPUT_PHONE = (ID, 'com.mbayar:id/input_id')
    BUTTON_SUBMIT = (ID, 'com.mbayar:id/btn_next')
    TL_HELP = (ID, 'com.mbayar:id/tv_help')
    INPUT_PIN = (ID, 'com.mbayar:id/input_pin1_et')
    TL_FORGOT_PIN = (ID, 'com.mbayar:id/tv_lupa_pin')

class FORGOT_PIN:
    TEXT_FORGOTPIN_INFO = (ID, 'com.mbayar:id/tv_title')
    INPUT_FIRST = (ID, 'com.mbayar:id/et_input1')
    INPUT_SECOND = (ID, 'com.mbayar:id/et_input2')
    BUTTON_DATE = (ID, 'com.mbayar:id/input_register4')
    TEXT_DESC_INFO = (ID, '')
    BUTTON_SUBMIT = (ID, 'com.mbayar:id/btn1')
    TEXT_DESC_INFO2 = (ID, 'com.mbayar:id/tv_title')
    INPUT_THIRD = (ID, 'com.mbayar:id/et_input3')
    TL_RESEND_OTP = (ID, 'com.mbayar:id/tv_resend')
    BUTTON_CONFIRM = (ID, 'com.mbayar:id/btn_reset_pin_confirm')

class DATE_PICKER:
    BUTTON_YEAR = (ID, 'android:id/date_picker_header_year')
    BUTTON_MONTH_NEXT = (ID, 'android:id/next')
    BUTTON_MONTH_PREV = (ID, 'android:id/prev')
    BUTTON_DATE = (ACCESS_ID, '12 Januari 1994')
    BUTTON_PICK_YEAR = (XPATH, "//android.widget.TextView[@text='1994']")
    BUTTON_SUBMIT = (ID, 'android:id/button1')

class REGISTER_BATCH:
    TARGET = (ID, 'com.mbayar:id/tv_tnc')
    INPUT_PHONE = (ID, 'com.mbayar:id/input_register1')
    INPUT_FULL_NAME = (ID, 'com.mbayar:id/input_register2')
    BUTTON_GENDER_MALE = (ID, 'com.mbayar:id/tv_gender_1')
    BUTTON_GENDER_FEMALE = (ID, 'com.mbayar:id/tv_gender_2')
    INPUT_BIRTH_PLACE = (ID, 'com.mbayar:id/et_register_bplace')
    BUTTON_DATE = (ID, 'com.mbayar:id/input_register4')
    INPUT_EMAIL = (ID, 'com.mbayar:id/input_register5')
    INPUT_PIN = (ID, 'com.mbayar:id/input_register6')
    INPUT_CONFIRM_PIN = (ID, 'com.mbayar:id/input_register7')
    CHECKBOX_AGREEMENT = (ID, 'com.mbayar:id/input_register8')
    BUTTON_SUBMIT = (ID, 'com.mbayar:id/btn_register')
    TEXT_SUCCESS_REGISTER = (ID, 'com.mbayar:id/tv_register1')
    TEXT_REGISTER_DESC = (ID, 'com.mbayar:id/tv_register2')
    BUTTON_SUBMIT_SECOND = (ID, 'com.mbayar:id/btn_register')
    SCROLL_DOWN = (CLASS_ID, 'android.widget.ScrollView')

class VERIFICATION_BATCH:
    TEXT_VERIFY_INFO = (ID, 'com.mbayar:id/tv_register1')
    TEXT_OTP_CODE = (ID, 'com.mbayar:id/tv_register_input1')
    INPUT_CODE = (ID, 'com.mbayar:id/et_register_input1')
    BUTTON_SUBMIT = (ID, 'com.mbayar:id/btn_done')
    TL_RESEND_OTP = (ID, 'com.mbayar:id/tv_register3')
    BUTTON_MIDDLE_CONFIRM = (ID, 'com.mbayar:id/dlg_btn_mid')
    TEXT_MESSAGE_POPUP = (ID, 'com.mbayar:id/dlg_msg_tv')
    TEXT_TITLE_POPUP = (ID, 'com.mbayar:id/dlg_title_tv')

class HOMEPAGE:
    IMG_HOME_LOGO = (ID, 'com.mbayar:id/toolbar_icon')
    BUTTON_SETTING = (ID, 'com.mbayar:id/action_setting')
    TEXT_CUSTOMER_NAME = (ID, 'com.mbayar:id/tv_customer_name')
    TEXT_ACCOUNT_TYPE = (ID, 'com.mbayar:id/tv_account_type')
    TEXT_CUSTOMER_ID = (ID, 'com.mbayar:id/tv_customer_id')
    TEXT_BALANCE_REMAINING = (ID, 'com.mbayar:id/tv_saldo')
    BUTTON_REFRESH = (ID, 'com.mbayar:id/ll_refresh')
    BUTTON_TOPUP = (ID, 'com.mbayar:id/ll_topup')
    BUTTON_HISTORY = (ID, 'com.mbayar:id/ll_riwayat')
    BUTTON_VOUCHER = (ID, 'com.mbayar:id/ll_menu1')
    BUTTON_BILLS = (ID, 'com.mbayar:id/ll_menu2')
    BUTTON_SHOP = (ID, 'com.mbayar:id/ll_menu3')
    BUTTON_TRANSFER = (ID, 'com.mbayar:id/ll_menu4')
    BUTTON_DONATION = (ID, 'com.mbayar:id/ll_menu5')
    BUTTON_PROMO = (ID, 'com.mbayar:id/ll_menu6')
    BUTTON_EDUCATION = (ID, 'com.mbayar:id/ll_menu7')
    BUTTON_SERVICES = (ID, 'com.mbayar:id/ll_menu8')

class SETTING:
    BUTTON_PROFILE = (XPATH, "//android.widget.TextView[@text='Profil Akun']")
    BUTTON_CHANGE_PROFILE = (XPATH, "//android.widget.TextView[@text='Ubah Profil']")
    BUTTON_CHANGE_PIN = (XPATH, "//android.widget.TextView[@text='Ubah PIN']")
    BUTTON_CHANGE_PHONE = (XPATH, "//android.widget.TextView[@text='Ubah Nomor Seluler']")
    BUTTON_CHANGE_EMAIL = (XPATH, "//android.widget.TextView[@text='Ubah Alamat Email']")
    BUTTON_TERMS_CONDITION = (XPATH, "//android.widget.TextView[@text='Syarat dan Ketentuan']")
    BUTTON_SERVICE_PROFILE = (XPATH, "//android.widget.TextView[@text='Profil Layanan']")
    BUTTON_FAQ = (XPATH, "//android.widget.TextView[@text='FAQ']")
    BUTTON_PRIVACY_POLICY = (XPATH, "//android.widget.TextView[@text='Kebijakan Privacy']")
    BUTTON_CUST_CALL = (XPATH, "//android.widget.TextView[@text='Hubungi Kami']")
    BUTTON_RESEND_EMAIL = (XPATH, "//android.widget.TextView[@text='Verifikasi Ulang Email']")
    BUTTON_DEACTIVED_ACCOUNT = (XPATH, "//android.widget.TextView[@text='Tutup Akun']")
    BUTTON_SIGN_OUT = (XPATH, "//android.widget.TextView[@text='Keluar']")

class PROFILE:
    BUTTON_RETURN_PROFILE = (ID, 'com.mbayar:id/my_toolbar')
    TEXT_USER_PHONE = (ID, 'com.mbayar:id/tv_nohp')
    TEXT_USERNAME = (ID, 'com.mbayar:id/tv_nama')
    TEXT_STATUS = (ID, 'com.mbayar:id/tv_status')

class EDIT_PIN:
    INPUT_OLD_PIN = (ID, 'com.mbayar:id/et_oldpin')
    INPUT_NEW_PIN = (ID, 'com.mbayar:id/et_newpin')
    INPUT_CONFIRM_PIN = (ID, 'com.mbayar:id/et_newpin_confirmation')
    BUTTON_SUBMIT = (ID, 'com.mbayar:id/btn_save')
    TEXT_EMAIL = (XPATH, '')

class DELETE_ACCOUNT:
    TEXT_TITLE = (ID, 'com.mbayar:id/dlg_title_tv')
    TEXT_DESC = (ID, 'com.mbayar:id/dlg_msg_tv')
    BUTTON_CONFIRM = (ID, 'com.mbayar:id/dlg_btn_mid')

class SIGN_OUT:
    BUTTON_CONFIRM = (ID, 'com.mbayar:id/dlg_btn_right')
    BUTTON_CANCEL = (ID, 'com.mbayar:id/dlg_btn_left')

class M_VOUCHER:
    TEXT_BALANCE_VALUE = (ID, 'com.mbayar:id/tv_saldo')
    BUTTON_BACK = (CLASS_ID, 'android.widget.ImageButton')
    BUTTON_PREPAID_PROV = (ID, 'com.mbayar:id/tv_payment_pulsa')
    BUTTON_PREPAID_ELEC = (XPATH, "//android.widget.TextView[@text='PLN Prepaid']")
    BUTTON_OPERATOR_VOUCHER = (ID, 'com.mbayar:id/rl_purchase1')
    BUTTON_NOMINAL = (ID, 'com.mbayar:id/rl_purchase3')
    INPUT_PHONE = (ID, 'com.mbayar:id/et_purchase_pulsa2')

    #OPERATOR_NAME
    LIST_ITEM_TSEL = (XPATH, "//android.widget.TextView[@text='Telkomsel']")
    LIST_ITEM_XL = (XPATH, "//android.widget.TextView[@text='XL']")
    LIST_ITEM_INDOSAT = (XPATH, "//android.widget.TextView[@text='Indosat']")
    LIST_ITEM_SMARTFREN = (XPATH, "//android.widget.TextView[@text='Smartfren']")
    LIST_ITEM_AXIS = (XPATH, "//android.widget.TextView[@text='AXIS']")
    LIST_ITEM_THREE = (XPATH, "//android.widget.TextView[@text='Three']")

    #NOMINAL_PAID
    LIST_PRICE_FIRST = (XPATH, "//android.widget.TextView[@text='Rp 1,000']")
    LIST_PRICE_SECOND = (XPATH, "//android.widget.TextView[@text='Rp 2,000']")
    LIST_PRICE_THIRD = (XPATH, "//android.widget.TextView[@text='Rp 5,000']")
    LIST_PRICE_FOURTH = (XPATH, "//android.widget.TextView[@text='Rp 10,000']")
    LIST_PRICE_FIFTH = (XPATH, "//android.widget.TextView[@text='Rp 20,000']")
    LIST_PRICE_SIXTH = (XPATH, "//android.widget.TextView[@text='Rp 25,000']")
    LIST_PRICE_SEVENTH = (XPATH, "//android.widget.TextView[@text='Rp 50,000']")
    LIST_PRICE_EIGHTH = (XPATH, "//android.widget.TextView[@text='Rp 100,000']")
    LIST_PRICE_NINTH = (XPATH, "//android.widget.TextView[@text='Rp 150,000']")
    LIST_PRICE_TENTH = (XPATH, "//android.widget.TextView[@text='Rp 200,000']")
    LIST_PRICE_ELEVENTH = (XPATH, "//android.widget.TextView[@text='Rp 300,000']")
    LIST_PRICE_TWELFTH = (XPATH, "//android.widget.TextView[@text='Rp 500,000']")
    LIST_PRICE_THIRTEENTH = (XPATH, "//android.widget.TextView[@text='Rp 1,000,000']")
    LIST_PRICE_FOURTEENTH = (XPATH, "//android.widget.TextView[@text='Rp 5,500']")
    LIST_PRICE_FIFTEENTH = (XPATH, "//android.widget.TextView[@text='Rp 30,000']")
    LIST_PRICE_SIXTEENTH = (XPATH, "//android.widget.TextView[@text='Rp 250,000']")
    LIST_PRICE_SEVENTEENTH = (XPATH, "//android.widget.TextView[@text='Rp 60,000']")
    LIST_PRICE_EIGHTEENTH = (XPATH, "")

class POSTPAID_TRANSACTION:
    BUTTON_POSTPAID_PROV = (ID, '')
    BUTTON_POSTPAID_ELEC = (ID, '')

class MERCHANT_TRANSACTION:
    BUTTON_MERCHANT = (ID, '')

class TRANSFER_TRANSACTION:
    BUTTON_TRANSFER = (ID, '')

class DONATION_TRANSACTION:
    BUTTON_ZAKAT = (ID, '')
    BUTTON_DONATION = (ID, '')
    BUTTON_MEMBER_DUES = (ID, '')
    BUTTON_ENDOWMENT = (ID, '')

class PROMO_TRANSACTION:
    BUTTON_PROMO = (ID, '')

class EDUCATION_TRANSACTION:
    BUTTON_EDUCATION = (ID, '')

class SERVICES_TRANSACTION:
    BUTTON_SERVICES = (ID, '')
