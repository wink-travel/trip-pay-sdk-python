# coding: utf-8

"""
    Wink Payment API

    A programmatic way to create bookings, receive reactive and disburse funds globally.  ## APIs Not every integrator needs every APIs. For that reason, we have separated APIs into context.  - [Affiliate](/affiliate): All APIs related to selling travel inventory as an affiliate. - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Booking](/booking): All APIs related to creating platform bookings. - [Channel Manager](/channel-manager): All APIs related to channel managers who want to integrate with our platform. - [Extranet](/extranet): All APIs related to managing travel inventory and suppliers. - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API.. - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.  ## SDKs We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java)  # Usage These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic. We will link to SDKs for the most popular programming languages on this page as they become available.  ## Versioning We chose to version our endpoints in a way that we hope affects your integration with us the least. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  ## Release history - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md 

    The version of the OpenAPI document: 30.17.14
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from trip_pay_payment.models.personal import Personal
from trip_pay_payment.models.preferences import Preferences
from trip_pay_payment.models.profile_user import ProfileUser
from typing import Optional, Set
from typing_extensions import Self

class ProfileLightweight(BaseModel):
    """
    ProfileLightweight
    """ # noqa: E501
    profile_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Profile identifier", alias="profileIdentifier")
    user_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="User identifier", alias="userIdentifier")
    share: StrictBool = Field(description="Indicates whether the user wants to share this profile of themselves with hotel(s)")
    user: ProfileUser = Field(description="User details")
    personal: Personal = Field(description="Detailed customer information for this profile")
    preferences: Preferences = Field(description="Customer preferences")
    __properties: ClassVar[List[str]] = ["profileIdentifier", "userIdentifier", "share", "user", "personal", "preferences"]

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
        """Create an instance of ProfileLightweight from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of personal
        if self.personal:
            _dict['personal'] = self.personal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preferences
        if self.preferences:
            _dict['preferences'] = self.preferences.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileLightweight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "profileIdentifier": obj.get("profileIdentifier"),
            "userIdentifier": obj.get("userIdentifier"),
            "share": obj.get("share"),
            "user": ProfileUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "personal": Personal.from_dict(obj["personal"]) if obj.get("personal") is not None else None,
            "preferences": Preferences.from_dict(obj["preferences"]) if obj.get("preferences") is not None else None
        })
        return _obj


