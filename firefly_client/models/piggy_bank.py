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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PiggyBank(BaseModel):
    """
    PiggyBank
    """ # noqa: E501
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    account_id: StrictStr = Field(description="The ID of the asset account this piggy bank is connected to.")
    account_name: Optional[StrictStr] = Field(default=None, description="The name of the asset account this piggy bank is connected to.")
    name: StrictStr
    currency_id: Optional[StrictStr] = None
    currency_code: Optional[StrictStr] = None
    currency_symbol: Optional[StrictStr] = None
    currency_decimal_places: Optional[StrictInt] = Field(default=None, description="Number of decimals supported by the currency")
    target_amount: Optional[StrictStr]
    percentage: Optional[Union[StrictFloat, StrictInt]] = None
    current_amount: Optional[StrictStr] = None
    left_to_save: Optional[StrictStr] = None
    save_per_month: Optional[StrictStr] = None
    start_date: Optional[date] = Field(default=None, description="The date you started with this piggy bank.")
    target_date: Optional[date] = Field(default=None, description="The date you intend to finish saving money.")
    order: Optional[StrictInt] = None
    active: Optional[StrictBool] = None
    notes: Optional[StrictStr] = None
    object_group_id: Optional[StrictStr] = Field(default=None, description="The group ID of the group this object is part of. NULL if no group.")
    object_group_order: Optional[StrictInt] = Field(default=None, description="The order of the group. At least 1, for the highest sorting.")
    object_group_title: Optional[StrictStr] = Field(default=None, description="The name of the group. NULL if no group.")
    __properties: ClassVar[List[str]] = ["created_at", "updated_at", "account_id", "account_name", "name", "currency_id", "currency_code", "currency_symbol", "currency_decimal_places", "target_amount", "percentage", "current_amount", "left_to_save", "save_per_month", "start_date", "target_date", "order", "active", "notes", "object_group_id", "object_group_order", "object_group_title"]

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
        """Create an instance of PiggyBank from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
            "account_name",
            "currency_id",
            "currency_code",
            "currency_symbol",
            "currency_decimal_places",
            "percentage",
            "left_to_save",
            "save_per_month",
            "active",
            "object_group_order",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if target_amount (nullable) is None
        # and model_fields_set contains the field
        if self.target_amount is None and "target_amount" in self.model_fields_set:
            _dict['target_amount'] = None

        # set to None if percentage (nullable) is None
        # and model_fields_set contains the field
        if self.percentage is None and "percentage" in self.model_fields_set:
            _dict['percentage'] = None

        # set to None if left_to_save (nullable) is None
        # and model_fields_set contains the field
        if self.left_to_save is None and "left_to_save" in self.model_fields_set:
            _dict['left_to_save'] = None

        # set to None if save_per_month (nullable) is None
        # and model_fields_set contains the field
        if self.save_per_month is None and "save_per_month" in self.model_fields_set:
            _dict['save_per_month'] = None

        # set to None if target_date (nullable) is None
        # and model_fields_set contains the field
        if self.target_date is None and "target_date" in self.model_fields_set:
            _dict['target_date'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if object_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_id is None and "object_group_id" in self.model_fields_set:
            _dict['object_group_id'] = None

        # set to None if object_group_order (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_order is None and "object_group_order" in self.model_fields_set:
            _dict['object_group_order'] = None

        # set to None if object_group_title (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_title is None and "object_group_title" in self.model_fields_set:
            _dict['object_group_title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PiggyBank from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "account_id": obj.get("account_id"),
            "account_name": obj.get("account_name"),
            "name": obj.get("name"),
            "currency_id": obj.get("currency_id"),
            "currency_code": obj.get("currency_code"),
            "currency_symbol": obj.get("currency_symbol"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "target_amount": obj.get("target_amount"),
            "percentage": obj.get("percentage"),
            "current_amount": obj.get("current_amount"),
            "left_to_save": obj.get("left_to_save"),
            "save_per_month": obj.get("save_per_month"),
            "start_date": obj.get("start_date"),
            "target_date": obj.get("target_date"),
            "order": obj.get("order"),
            "active": obj.get("active"),
            "notes": obj.get("notes"),
            "object_group_id": obj.get("object_group_id"),
            "object_group_order": obj.get("object_group_order"),
            "object_group_title": obj.get("object_group_title")
        })
        return _obj

