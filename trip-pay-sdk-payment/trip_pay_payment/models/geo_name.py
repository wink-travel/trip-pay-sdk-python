# coding: utf-8

"""
    Wink Payment API

    A programmatic way to create bookings, receive reactive and disburse funds globally.  ## APIs Not every integrator needs every APIs. For that reason, we have separated APIs into context.  - [Affiliate](/affiliate): All APIs related to selling travel inventory as an affiliate. - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Booking](/booking): All APIs related to creating platform bookings. - [Channel Manager](/channel-manager): All APIs related to channel managers who want to integrate with our platform. - [Extranet](/extranet): All APIs related to managing travel inventory and suppliers. - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API.. - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.  ## SDKs We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java)  # Usage These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic. We will link to SDKs for the most popular programming languages on this page as they become available.  ## Versioning We chose to version our endpoints in a way that we hope affects your integration with us the least. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  ## Release history - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md 

    The version of the OpenAPI document: 30.16.4
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from trip_pay_payment.models.country import Country
from trip_pay_payment.models.geo_json_point import GeoJsonPoint
from trip_pay_payment.models.sub_country import SubCountry
from trip_pay_payment.models.sub_sub_country import SubSubCountry
from typing import Optional, Set
from typing_extensions import Self

class GeoName(BaseModel):
    """
    GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.
    """ # noqa: E501
    geo_name_id: Optional[StrictStr] = Field(default=None, description="GeoName identifier", alias="geoNameId")
    type: Optional[StrictStr] = Field(default=None, description="GeoName type")
    name: Optional[StrictStr] = Field(default=None, description="Name of city")
    url_name: Optional[StrictStr] = Field(default=None, description="Url name", alias="urlName")
    ascii_name: Optional[StrictStr] = Field(default=None, description="Ascii name of city", alias="asciiName")
    alternate_names: Optional[List[StrictStr]] = Field(default=None, description="Array of alternate name", alias="alternateNames")
    location: Optional[GeoJsonPoint] = None
    feature_class: Optional[StrictStr] = Field(default=None, alias="featureClass")
    feature_code: Optional[StrictStr] = Field(default=None, alias="featureCode")
    country_code: Optional[StrictStr] = Field(default=None, alias="countryCode")
    alternate_country_codes: Optional[List[StrictStr]] = Field(default=None, alias="alternateCountryCodes")
    admin1_code: Optional[StrictStr] = Field(default=None, alias="admin1Code")
    admin2_code: Optional[StrictStr] = Field(default=None, alias="admin2Code")
    admin3_code: Optional[StrictStr] = Field(default=None, alias="admin3Code")
    admin4_code: Optional[StrictStr] = Field(default=None, alias="admin4Code")
    population: Optional[StrictInt] = Field(default=None, description="Population of the city")
    elevation: Optional[StrictInt] = Field(default=None, description="City elevation")
    digital_elevation_model: Optional[StrictStr] = Field(default=None, alias="digitalElevationModel")
    timezone: Optional[StrictStr] = Field(default=None, description="Timezone")
    modification_date: Optional[date] = Field(default=None, alias="modificationDate")
    radius_in_meters: Optional[StrictInt] = Field(default=None, alias="radiusInMeters")
    country: Optional[Country] = None
    sub_country: Optional[SubCountry] = Field(default=None, alias="subCountry")
    sub_sub_country: Optional[SubSubCountry] = Field(default=None, alias="subSubCountry")
    __properties: ClassVar[List[str]] = ["geoNameId", "type", "name", "urlName", "asciiName", "alternateNames", "location", "featureClass", "featureCode", "countryCode", "alternateCountryCodes", "admin1Code", "admin2Code", "admin3Code", "admin4Code", "population", "elevation", "digitalElevationModel", "timezone", "modificationDate", "radiusInMeters", "country", "subCountry", "subSubCountry"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CITY', 'ISLAND', 'OTHER']):
            raise ValueError("must be one of enum values ('CITY', 'ISLAND', 'OTHER')")
        return value

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
        """Create an instance of GeoName from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_country
        if self.sub_country:
            _dict['subCountry'] = self.sub_country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_sub_country
        if self.sub_sub_country:
            _dict['subSubCountry'] = self.sub_sub_country.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GeoName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "geoNameId": obj.get("geoNameId"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "urlName": obj.get("urlName"),
            "asciiName": obj.get("asciiName"),
            "alternateNames": obj.get("alternateNames"),
            "location": GeoJsonPoint.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "featureClass": obj.get("featureClass"),
            "featureCode": obj.get("featureCode"),
            "countryCode": obj.get("countryCode"),
            "alternateCountryCodes": obj.get("alternateCountryCodes"),
            "admin1Code": obj.get("admin1Code"),
            "admin2Code": obj.get("admin2Code"),
            "admin3Code": obj.get("admin3Code"),
            "admin4Code": obj.get("admin4Code"),
            "population": obj.get("population"),
            "elevation": obj.get("elevation"),
            "digitalElevationModel": obj.get("digitalElevationModel"),
            "timezone": obj.get("timezone"),
            "modificationDate": obj.get("modificationDate"),
            "radiusInMeters": obj.get("radiusInMeters"),
            "country": Country.from_dict(obj["country"]) if obj.get("country") is not None else None,
            "subCountry": SubCountry.from_dict(obj["subCountry"]) if obj.get("subCountry") is not None else None,
            "subSubCountry": SubSubCountry.from_dict(obj["subSubCountry"]) if obj.get("subSubCountry") is not None else None
        })
        return _obj


