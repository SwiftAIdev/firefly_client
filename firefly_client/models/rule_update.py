# coding: utf-8

"""
    Firefly III API v2.1.0

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2024-09-10T05:07:57+00:00  Please keep in mind that the demo site does not accept requests from curl, colly, wget, etc. You must use a browser or a tool like Postman to make requests. Too many script kiddies out there, sorry about that. 

    The version of the OpenAPI document: 2.1.0
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_client.models.rule_action_update import RuleActionUpdate
from firefly_client.models.rule_trigger_type import RuleTriggerType
from firefly_client.models.rule_trigger_update import RuleTriggerUpdate
from typing import Optional, Set
from typing_extensions import Self

class RuleUpdate(BaseModel):
    """
    RuleUpdate
    """ # noqa: E501
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    rule_group_id: Optional[StrictStr] = Field(default=None, description="ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory.")
    order: Optional[StrictInt] = None
    trigger: Optional[RuleTriggerType] = None
    active: Optional[StrictBool] = Field(default=True, description="Whether or not the rule is even active. Default is true.")
    strict: Optional[StrictBool] = Field(default=None, description="If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true.")
    stop_processing: Optional[StrictBool] = Field(default=False, description="If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false.")
    triggers: Optional[List[RuleTriggerUpdate]] = None
    actions: Optional[List[RuleActionUpdate]] = None
    __properties: ClassVar[List[str]] = ["title", "description", "rule_group_id", "order", "trigger", "active", "strict", "stop_processing", "triggers", "actions"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RuleUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item_triggers in self.triggers:
                if _item_triggers:
                    _items.append(_item_triggers.to_dict())
            _dict['triggers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "rule_group_id": obj.get("rule_group_id"),
            "order": obj.get("order"),
            "trigger": obj.get("trigger"),
            "active": obj.get("active") if obj.get("active") is not None else True,
            "strict": obj.get("strict"),
            "stop_processing": obj.get("stop_processing") if obj.get("stop_processing") is not None else False,
            "triggers": [RuleTriggerUpdate.from_dict(_item) for _item in obj["triggers"]] if obj.get("triggers") is not None else None,
            "actions": [RuleActionUpdate.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None
        })
        return _obj


