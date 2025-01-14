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

from firefly_client.models.tag_single import TagSingle

class TestTagSingle(unittest.TestCase):
    """TagSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagSingle:
        """Test TagSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagSingle`
        """
        model = TagSingle()
        if include_optional:
            return TagSingle(
                data = firefly_client.models.tag_read.TagRead(
                    type = 'tags', 
                    id = '2', 
                    attributes = firefly_client.models.a_single_tag_(c).A single tag (C)(
                        created_at = '2018-09-17T12:46:47+01:00', 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        tag = 'expensive', 
                        date = 'Mon Sep 17 00:00:00 UTC 2018', 
                        description = 'Tag for expensive stuff', 
                        latitude = 51.983333, 
                        longitude = 5.916667, 
                        zoom_level = 6, ), 
                    links = firefly_client.models.object_link.ObjectLink(
                        0 = firefly_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), )
            )
        else:
            return TagSingle(
                data = firefly_client.models.tag_read.TagRead(
                    type = 'tags', 
                    id = '2', 
                    attributes = firefly_client.models.a_single_tag_(c).A single tag (C)(
                        created_at = '2018-09-17T12:46:47+01:00', 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        tag = 'expensive', 
                        date = 'Mon Sep 17 00:00:00 UTC 2018', 
                        description = 'Tag for expensive stuff', 
                        latitude = 51.983333, 
                        longitude = 5.916667, 
                        zoom_level = 6, ), 
                    links = firefly_client.models.object_link.ObjectLink(
                        0 = firefly_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), ),
        )
        """

    def testTagSingle(self):
        """Test TagSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
