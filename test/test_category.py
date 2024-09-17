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

from firefly_client.models.category import Category

class TestCategory(unittest.TestCase):
    """Category unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Category:
        """Test Category
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Category`
        """
        model = Category()
        if include_optional:
            return Category(
                created_at = '2018-09-17T12:46:47+01:00',
                updated_at = '2018-09-17T12:46:47+01:00',
                name = 'Lunch',
                notes = 'Some example notes',
                spent = [
                    firefly_client.models.category_spent.CategorySpent(
                        currency_id = '5', 
                        currency_code = 'USD', 
                        currency_symbol = '$', 
                        currency_decimal_places = 2, 
                        sum = '-12423.45', )
                    ],
                earned = [
                    firefly_client.models.category_earned.CategoryEarned(
                        currency_id = '5', 
                        currency_code = 'USD', 
                        currency_symbol = '$', 
                        currency_decimal_places = 2, 
                        sum = '123.45', )
                    ]
            )
        else:
            return Category(
                name = 'Lunch',
        )
        """

    def testCategory(self):
        """Test Category"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
