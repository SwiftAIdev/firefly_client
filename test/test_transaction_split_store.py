# coding: utf-8

"""
    Firefly III API v2.1.0

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2024-09-10T05:07:57+00:00  Please keep in mind that the demo site does not accept requests from curl, colly, wget, etc. You must use a browser or a tool like Postman to make requests. Too many script kiddies out there, sorry about that. 

    The version of the OpenAPI document: 2.1.0
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_client.models.transaction_split_store import TransactionSplitStore

class TestTransactionSplitStore(unittest.TestCase):
    """TransactionSplitStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSplitStore:
        """Test TransactionSplitStore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionSplitStore`
        """
        model = TransactionSplitStore()
        if include_optional:
            return TransactionSplitStore(
                type = 'withdrawal',
                var_date = '2018-09-17T12:46:47+01:00',
                amount = '123.45',
                description = 'Vegetables',
                order = 0,
                currency_id = '12',
                currency_code = 'EUR',
                foreign_amount = '123.45',
                foreign_currency_id = '17',
                foreign_currency_code = 'USD',
                budget_id = '4',
                budget_name = 'Groceries',
                category_id = '43',
                category_name = 'Groceries',
                source_id = '2',
                source_name = 'Checking account',
                destination_id = '2',
                destination_name = 'Buy and Large',
                reconciled = False,
                piggy_bank_id = 56,
                piggy_bank_name = '',
                bill_id = '112',
                bill_name = 'Monthly rent',
                tags = [
                    'Barbecue preparation'
                    ],
                notes = 'Some example notes',
                internal_reference = '',
                external_id = '',
                external_url = '',
                bunq_payment_id = '',
                sepa_cc = '',
                sepa_ct_op = '',
                sepa_ct_id = '',
                sepa_db = '',
                sepa_country = '',
                sepa_ep = '',
                sepa_ci = '',
                sepa_batch_id = '',
                interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return TransactionSplitStore(
                type = 'withdrawal',
                var_date = '2018-09-17T12:46:47+01:00',
                amount = '123.45',
                description = 'Vegetables',
        )
        """

    def testTransactionSplitStore(self):
        """Test TransactionSplitStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
