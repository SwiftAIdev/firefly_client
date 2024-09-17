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

from firefly_client.api.available_budgets_api import AvailableBudgetsApi


class TestAvailableBudgetsApi(unittest.TestCase):
    """AvailableBudgetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AvailableBudgetsApi()

    def tearDown(self) -> None:
        pass

    def test_get_available_budget(self) -> None:
        """Test case for get_available_budget

        Get a single available budget.
        """
        pass

    def test_list_available_budget(self) -> None:
        """Test case for list_available_budget

        List all available budget amounts.
        """
        pass


if __name__ == '__main__':
    unittest.main()