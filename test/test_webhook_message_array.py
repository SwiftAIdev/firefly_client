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

from firefly_client.models.webhook_message_array import WebhookMessageArray

class TestWebhookMessageArray(unittest.TestCase):
    """WebhookMessageArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookMessageArray:
        """Test WebhookMessageArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookMessageArray`
        """
        model = WebhookMessageArray()
        if include_optional:
            return WebhookMessageArray(
                data = [
                    firefly_client.models.webhook_message_read.WebhookMessageRead(
                        type = 'webhook_messages', 
                        id = '2', 
                        attributes = firefly_client.models.webhook_message.WebhookMessage(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            sent = False, 
                            errored = False, 
                            webhook_id = '5', 
                            uuid = '7a344c02-5b52-46b1-90e6-a437431dcf07', 
                            message = '{some:message}', ), )
                    ],
                meta = firefly_client.models.meta.Meta(
                    pagination = firefly_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), )
            )
        else:
            return WebhookMessageArray(
                data = [
                    firefly_client.models.webhook_message_read.WebhookMessageRead(
                        type = 'webhook_messages', 
                        id = '2', 
                        attributes = firefly_client.models.webhook_message.WebhookMessage(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            sent = False, 
                            errored = False, 
                            webhook_id = '5', 
                            uuid = '7a344c02-5b52-46b1-90e6-a437431dcf07', 
                            message = '{some:message}', ), )
                    ],
                meta = firefly_client.models.meta.Meta(
                    pagination = firefly_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), ),
        )
        """

    def testWebhookMessageArray(self):
        """Test WebhookMessageArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
