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

from firefly_client.api.about_api import AboutApi


class TestAboutApi(unittest.TestCase):
    """AboutApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AboutApi()

    def tearDown(self) -> None:
        pass

    def test_get_about(self) -> None:
        """Test case for get_about

        System information end point.
        """
        pass

    def test_get_cron(self) -> None:
        """Test case for get_cron

        Cron job endpoint
        """
        pass

    def test_get_current_user(self) -> None:
        """Test case for get_current_user

        Currently authenticated user endpoint.
        """
        pass


if __name__ == '__main__':
    unittest.main()