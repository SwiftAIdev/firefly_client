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
from firefly_client.models.auto_budget_period import AutoBudgetPeriod
from firefly_client.models.auto_budget_type import AutoBudgetType
from typing import Optional, Set
from typing_extensions import Self

class BudgetUpdate(BaseModel):
    """
    BudgetUpdate
    """ # noqa: E501
    name: StrictStr
    active: Optional[StrictBool] = None
    order: Optional[StrictInt] = None
    notes: Optional[StrictStr] = None
    auto_budget_type: Optional[AutoBudgetType] = None
    auto_budget_currency_id: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    auto_budget_currency_code: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    auto_budget_amount: Optional[StrictStr] = None
    auto_budget_period: Optional[AutoBudgetPeriod] = None
    __properties: ClassVar[List[str]] = ["name", "active", "order", "notes", "auto_budget_type", "auto_budget_currency_id", "auto_budget_currency_code", "auto_budget_amount", "auto_budget_period"]

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
        """Create an instance of BudgetUpdate from a JSON string"""
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
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if auto_budget_type (nullable) is None
        # and model_fields_set contains the field
        if self.auto_budget_type is None and "auto_budget_type" in self.model_fields_set:
            _dict['auto_budget_type'] = None

        # set to None if auto_budget_currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.auto_budget_currency_id is None and "auto_budget_currency_id" in self.model_fields_set:
            _dict['auto_budget_currency_id'] = None

        # set to None if auto_budget_currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.auto_budget_currency_code is None and "auto_budget_currency_code" in self.model_fields_set:
            _dict['auto_budget_currency_code'] = None

        # set to None if auto_budget_amount (nullable) is None
        # and model_fields_set contains the field
        if self.auto_budget_amount is None and "auto_budget_amount" in self.model_fields_set:
            _dict['auto_budget_amount'] = None

        # set to None if auto_budget_period (nullable) is None
        # and model_fields_set contains the field
        if self.auto_budget_period is None and "auto_budget_period" in self.model_fields_set:
            _dict['auto_budget_period'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BudgetUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "active": obj.get("active"),
            "order": obj.get("order"),
            "notes": obj.get("notes"),
            "auto_budget_type": obj.get("auto_budget_type"),
            "auto_budget_currency_id": obj.get("auto_budget_currency_id"),
            "auto_budget_currency_code": obj.get("auto_budget_currency_code"),
            "auto_budget_amount": obj.get("auto_budget_amount"),
            "auto_budget_period": obj.get("auto_budget_period")
        })
        return _obj


