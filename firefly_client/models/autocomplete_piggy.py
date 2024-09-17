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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AutocompletePiggy(BaseModel):
    """
    AutocompletePiggy
    """ # noqa: E501
    id: StrictStr
    name: StrictStr = Field(description="Name of the piggy bank found by an auto-complete search.")
    currency_id: Optional[StrictStr] = Field(default=None, description="Currency ID for this piggy bank.")
    currency_code: Optional[StrictStr] = Field(default=None, description="Currency code for this piggy bank.")
    currency_symbol: Optional[StrictStr] = None
    currency_name: Optional[StrictStr] = Field(default=None, description="Currency name for the currency used by this account.")
    currency_decimal_places: Optional[StrictInt] = None
    object_group_id: Optional[StrictStr] = Field(default=None, description="The group ID of the group this object is part of. NULL if no group.")
    object_group_title: Optional[StrictStr] = Field(default=None, description="The name of the group. NULL if no group.")
    __properties: ClassVar[List[str]] = ["id", "name", "currency_id", "currency_code", "currency_symbol", "currency_name", "currency_decimal_places", "object_group_id", "object_group_title"]

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
        """Create an instance of AutocompletePiggy from a JSON string"""
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
        # set to None if object_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_id is None and "object_group_id" in self.model_fields_set:
            _dict['object_group_id'] = None

        # set to None if object_group_title (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_title is None and "object_group_title" in self.model_fields_set:
            _dict['object_group_title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutocompletePiggy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "currency_id": obj.get("currency_id"),
            "currency_code": obj.get("currency_code"),
            "currency_symbol": obj.get("currency_symbol"),
            "currency_name": obj.get("currency_name"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "object_group_id": obj.get("object_group_id"),
            "object_group_title": obj.get("object_group_title")
        })
        return _obj


