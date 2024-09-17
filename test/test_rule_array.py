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

from firefly_client.models.rule_array import RuleArray

class TestRuleArray(unittest.TestCase):
    """RuleArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleArray:
        """Test RuleArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleArray`
        """
        model = RuleArray()
        if include_optional:
            return RuleArray(
                data = [
                    firefly_client.models.rule_read.RuleRead(
                        type = 'rules', 
                        id = '2', 
                        attributes = firefly_client.models.rule.Rule(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            title = 'First rule title.', 
                            description = 'First rule description', 
                            rule_group_id = '81', 
                            rule_group_title = 'New rule group', 
                            order = 5, 
                            trigger = 'store-journal', 
                            active = True, 
                            strict = True, 
                            stop_processing = False, 
                            triggers = [
                                firefly_client.models.rule_trigger.RuleTrigger(
                                    id = '2', 
                                    created_at = '2018-09-17T12:46:47+01:00', 
                                    updated_at = '2018-09-17T12:46:47+01:00', 
                                    type = 'user_action', 
                                    value = 'tag1', 
                                    prohibited = False, 
                                    order = 5, 
                                    active = True, 
                                    stop_processing = False, )
                                ], 
                            actions = [
                                firefly_client.models.rule_action.RuleAction(
                                    id = '2', 
                                    created_at = '2018-09-17T12:46:47+01:00', 
                                    updated_at = '2018-09-17T12:46:47+01:00', 
                                    type = 'set_category', 
                                    value = 'Daily groceries', 
                                    order = 5, 
                                    active = True, 
                                    stop_processing = False, )
                                ], ), 
                        links = firefly_client.models.object_link.ObjectLink(
                            0 = firefly_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), 
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), )
                    ],
                meta = firefly_client.models.meta.Meta(
                    pagination = firefly_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), ),
                links = firefly_client.models.page_link.PageLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=4', 
                    first = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=1', 
                    next = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=3', 
                    prev = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=2', 
                    last = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=12', )
            )
        else:
            return RuleArray(
                data = [
                    firefly_client.models.rule_read.RuleRead(
                        type = 'rules', 
                        id = '2', 
                        attributes = firefly_client.models.rule.Rule(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            title = 'First rule title.', 
                            description = 'First rule description', 
                            rule_group_id = '81', 
                            rule_group_title = 'New rule group', 
                            order = 5, 
                            trigger = 'store-journal', 
                            active = True, 
                            strict = True, 
                            stop_processing = False, 
                            triggers = [
                                firefly_client.models.rule_trigger.RuleTrigger(
                                    id = '2', 
                                    created_at = '2018-09-17T12:46:47+01:00', 
                                    updated_at = '2018-09-17T12:46:47+01:00', 
                                    type = 'user_action', 
                                    value = 'tag1', 
                                    prohibited = False, 
                                    order = 5, 
                                    active = True, 
                                    stop_processing = False, )
                                ], 
                            actions = [
                                firefly_client.models.rule_action.RuleAction(
                                    id = '2', 
                                    created_at = '2018-09-17T12:46:47+01:00', 
                                    updated_at = '2018-09-17T12:46:47+01:00', 
                                    type = 'set_category', 
                                    value = 'Daily groceries', 
                                    order = 5, 
                                    active = True, 
                                    stop_processing = False, )
                                ], ), 
                        links = firefly_client.models.object_link.ObjectLink(
                            0 = firefly_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), 
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), )
                    ],
                meta = firefly_client.models.meta.Meta(
                    pagination = firefly_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), ),
                links = firefly_client.models.page_link.PageLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=4', 
                    first = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=1', 
                    next = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=3', 
                    prev = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=2', 
                    last = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=12', ),
        )
        """

    def testRuleArray(self):
        """Test RuleArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
