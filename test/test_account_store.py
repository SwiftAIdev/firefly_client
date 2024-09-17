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

from firefly_client.models.account_store import AccountStore

class TestAccountStore(unittest.TestCase):
    """AccountStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountStore:
        """Test AccountStore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountStore`
        """
        model = AccountStore()
        if include_optional:
            return AccountStore(
                name = 'My checking account',
                type = 'asset',
                iban = 'GB98MIDL07009312345678',
                bic = 'BOFAUS3N',
                account_number = '7009312345678',
                opening_balance = '-1012.12',
                opening_balance_date = '2018-09-17T12:46:47+01:00',
                virtual_balance = '123.45',
                currency_id = '12',
                currency_code = 'EUR',
                active = False,
                order = 1,
                include_net_worth = True,
                account_role = 'defaultAsset',
                credit_card_type = 'monthlyFull',
                monthly_payment_date = '2018-09-17T12:46:47+01:00',
                liability_type = 'loan',
                liability_direction = 'credit',
                interest = '0',
                interest_period = 'monthly',
                notes = 'Some example notes',
                latitude = 51.983333,
                longitude = 5.916667,
                zoom_level = 6
            )
        else:
            return AccountStore(
                name = 'My checking account',
                type = 'asset',
        )
        """

    def testAccountStore(self):
        """Test AccountStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
