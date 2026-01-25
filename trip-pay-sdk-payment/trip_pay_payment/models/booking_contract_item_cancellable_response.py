# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None  

    The version of the OpenAPI document: 30.31.5
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from trip_pay_payment.models.custom_monetary_amount import CustomMonetaryAmount
from trip_pay_payment.models.supplier_contract_item_policy import SupplierContractItemPolicy
from typing import Optional, Set
from typing_extensions import Self

class BookingContractItemCancellableResponse(BaseModel):
    """
    Contract item cancellable object
    """ # noqa: E501
    supplier_item_booking_code: Optional[StrictStr] = Field(default=None, description="Booking code identifying the supplier line item.", alias="supplierItemBookingCode")
    name_in_english: Optional[StrictStr] = Field(default=None, description="Name of item in English included in booking.", alias="nameInEnglish")
    policy: Optional[SupplierContractItemPolicy] = None
    type: Optional[StrictStr] = Field(default=None, description="Type of item this is.")
    source_price: Optional[CustomMonetaryAmount] = Field(default=None, description="The sourcePrice of this item.", alias="sourcePrice")
    supplier_price: Optional[CustomMonetaryAmount] = Field(default=None, description="The supplierPrice of this item.", alias="supplierPrice")
    display_price: Optional[CustomMonetaryAmount] = Field(default=None, description="The displayPrice of this item.", alias="displayPrice")
    internal_price: Optional[CustomMonetaryAmount] = Field(default=None, description="The internalPrice of this item.", alias="internalPrice")
    capture_price: Optional[CustomMonetaryAmount] = Field(default=None, description="The capturePrice of this item.", alias="capturePrice")
    cancellable_by_traveler: Optional[StrictBool] = Field(default=None, description="Whether this item can be cancelled by traveler either fully or partially.", alias="cancellableByTraveler")
    cancellable_by_supplier: Optional[StrictBool] = Field(default=None, description="Whether this item can be cancelled by supplier either fully or partially.", alias="cancellableBySupplier")
    cancellable_with_charges: Optional[StrictBool] = Field(default=None, description="Whether this item can be cancelled by supplier either fully or partially.", alias="cancellableWithCharges")
    source_price_after_refund: Optional[CustomMonetaryAmount] = Field(default=None, description="The source amount still due after a cancellation occurs.", alias="sourcePriceAfterRefund")
    supplier_price_after_refund: Optional[CustomMonetaryAmount] = Field(default=None, description="The supplier amount still due after a cancellation occurs.", alias="supplierPriceAfterRefund")
    display_price_after_refund: Optional[CustomMonetaryAmount] = Field(default=None, description="The display amount still due after a cancellation occurs.", alias="displayPriceAfterRefund")
    internal_price_after_refund: Optional[CustomMonetaryAmount] = Field(default=None, description="The internal amount still due after a cancellation occurs.", alias="internalPriceAfterRefund")
    capture_price_after_refund: Optional[CustomMonetaryAmount] = Field(default=None, description="The capture amount still due after a cancellation occurs.", alias="capturePriceAfterRefund")
    __properties: ClassVar[List[str]] = ["supplierItemBookingCode", "nameInEnglish", "policy", "type", "sourcePrice", "supplierPrice", "displayPrice", "internalPrice", "capturePrice", "cancellableByTraveler", "cancellableBySupplier", "cancellableWithCharges", "sourcePriceAfterRefund", "supplierPriceAfterRefund", "displayPriceAfterRefund", "internalPriceAfterRefund", "capturePriceAfterRefund"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LODGING', 'RAIL', 'AIR', 'CAR', 'CRUISE', 'PACKAGE', 'ADD_ON', 'RENTAL', 'EXPERIENCE', 'ANCILLARY_BOOKING', 'ANCILLARY_FEE']):
            raise ValueError("must be one of enum values ('LODGING', 'RAIL', 'AIR', 'CAR', 'CRUISE', 'PACKAGE', 'ADD_ON', 'RENTAL', 'EXPERIENCE', 'ANCILLARY_BOOKING', 'ANCILLARY_FEE')")
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
        """Create an instance of BookingContractItemCancellableResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_price
        if self.source_price:
            _dict['sourcePrice'] = self.source_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supplier_price
        if self.supplier_price:
            _dict['supplierPrice'] = self.supplier_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display_price
        if self.display_price:
            _dict['displayPrice'] = self.display_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of internal_price
        if self.internal_price:
            _dict['internalPrice'] = self.internal_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of capture_price
        if self.capture_price:
            _dict['capturePrice'] = self.capture_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_price_after_refund
        if self.source_price_after_refund:
            _dict['sourcePriceAfterRefund'] = self.source_price_after_refund.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supplier_price_after_refund
        if self.supplier_price_after_refund:
            _dict['supplierPriceAfterRefund'] = self.supplier_price_after_refund.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display_price_after_refund
        if self.display_price_after_refund:
            _dict['displayPriceAfterRefund'] = self.display_price_after_refund.to_dict()
        # override the default output from pydantic by calling `to_dict()` of internal_price_after_refund
        if self.internal_price_after_refund:
            _dict['internalPriceAfterRefund'] = self.internal_price_after_refund.to_dict()
        # override the default output from pydantic by calling `to_dict()` of capture_price_after_refund
        if self.capture_price_after_refund:
            _dict['capturePriceAfterRefund'] = self.capture_price_after_refund.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BookingContractItemCancellableResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "supplierItemBookingCode": obj.get("supplierItemBookingCode"),
            "nameInEnglish": obj.get("nameInEnglish"),
            "policy": SupplierContractItemPolicy.from_dict(obj["policy"]) if obj.get("policy") is not None else None,
            "type": obj.get("type"),
            "sourcePrice": CustomMonetaryAmount.from_dict(obj["sourcePrice"]) if obj.get("sourcePrice") is not None else None,
            "supplierPrice": CustomMonetaryAmount.from_dict(obj["supplierPrice"]) if obj.get("supplierPrice") is not None else None,
            "displayPrice": CustomMonetaryAmount.from_dict(obj["displayPrice"]) if obj.get("displayPrice") is not None else None,
            "internalPrice": CustomMonetaryAmount.from_dict(obj["internalPrice"]) if obj.get("internalPrice") is not None else None,
            "capturePrice": CustomMonetaryAmount.from_dict(obj["capturePrice"]) if obj.get("capturePrice") is not None else None,
            "cancellableByTraveler": obj.get("cancellableByTraveler"),
            "cancellableBySupplier": obj.get("cancellableBySupplier"),
            "cancellableWithCharges": obj.get("cancellableWithCharges"),
            "sourcePriceAfterRefund": CustomMonetaryAmount.from_dict(obj["sourcePriceAfterRefund"]) if obj.get("sourcePriceAfterRefund") is not None else None,
            "supplierPriceAfterRefund": CustomMonetaryAmount.from_dict(obj["supplierPriceAfterRefund"]) if obj.get("supplierPriceAfterRefund") is not None else None,
            "displayPriceAfterRefund": CustomMonetaryAmount.from_dict(obj["displayPriceAfterRefund"]) if obj.get("displayPriceAfterRefund") is not None else None,
            "internalPriceAfterRefund": CustomMonetaryAmount.from_dict(obj["internalPriceAfterRefund"]) if obj.get("internalPriceAfterRefund") is not None else None,
            "capturePriceAfterRefund": CustomMonetaryAmount.from_dict(obj["capturePriceAfterRefund"]) if obj.get("capturePriceAfterRefund") is not None else None
        })
        return _obj


