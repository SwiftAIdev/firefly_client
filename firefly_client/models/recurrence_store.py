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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_client.models.recurrence_repetition_store import RecurrenceRepetitionStore
from firefly_client.models.recurrence_transaction_store import RecurrenceTransactionStore
from firefly_client.models.recurrence_transaction_type import RecurrenceTransactionType
from typing import Optional, Set
from typing_extensions import Self

class RecurrenceStore(BaseModel):
    """
    RecurrenceStore
    """ # noqa: E501
    type: RecurrenceTransactionType
    title: StrictStr
    description: Optional[StrictStr] = Field(default=None, description="Not to be confused with the description of the actual transaction(s) being created.")
    first_date: date = Field(description="First time the recurring transaction will fire. Must be after today.")
    repeat_until: Optional[date] = Field(description="Date until the recurring transaction can fire. Use either this field or repetitions.")
    nr_of_repetitions: Optional[StrictInt] = Field(default=None, description="Max number of created transactions. Use either this field or repeat_until.")
    apply_rules: Optional[StrictBool] = Field(default=None, description="Whether or not to fire the rules after the creation of a transaction.")
    active: Optional[StrictBool] = Field(default=None, description="If the recurrence is even active.")
    notes: Optional[StrictStr] = None
    repetitions: List[RecurrenceRepetitionStore]
    transactions: List[RecurrenceTransactionStore]
    __properties: ClassVar[List[str]] = ["type", "title", "description", "first_date", "repeat_until", "nr_of_repetitions", "apply_rules", "active", "notes", "repetitions", "transactions"]

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
        """Create an instance of RecurrenceStore from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in repetitions (list)
        _items = []
        if self.repetitions:
            for _item_repetitions in self.repetitions:
                if _item_repetitions:
                    _items.append(_item_repetitions.to_dict())
            _dict['repetitions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item_transactions in self.transactions:
                if _item_transactions:
                    _items.append(_item_transactions.to_dict())
            _dict['transactions'] = _items
        # set to None if repeat_until (nullable) is None
        # and model_fields_set contains the field
        if self.repeat_until is None and "repeat_until" in self.model_fields_set:
            _dict['repeat_until'] = None

        # set to None if nr_of_repetitions (nullable) is None
        # and model_fields_set contains the field
        if self.nr_of_repetitions is None and "nr_of_repetitions" in self.model_fields_set:
            _dict['nr_of_repetitions'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecurrenceStore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "first_date": obj.get("first_date"),
            "repeat_until": obj.get("repeat_until"),
            "nr_of_repetitions": obj.get("nr_of_repetitions"),
            "apply_rules": obj.get("apply_rules"),
            "active": obj.get("active"),
            "notes": obj.get("notes"),
            "repetitions": [RecurrenceRepetitionStore.from_dict(_item) for _item in obj["repetitions"]] if obj.get("repetitions") is not None else None,
            "transactions": [RecurrenceTransactionStore.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None
        })
        return _obj


