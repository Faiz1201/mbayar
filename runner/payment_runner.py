from feature.payment_feature import PaymentFeature
from runner.base_runner import BaseRunner


class TransactionRunner(BaseRunner):

    def setUp(self):
        BaseRunner.setUp(self)
        self.transaction = PaymentFeature(self.driver)

    def test_valid_prepaid_indosat(self):
        self.transaction.do_prepaid_mdeals_indosat('087784292693', '150194')