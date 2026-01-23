# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None  

    The version of the OpenAPI document: 30.31.3
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from trip_pay_payment.models.authenticated_user import AuthenticatedUser
from trip_pay_payment.models.custom_monetary_amount import CustomMonetaryAmount
from trip_pay_payment.models.integrator import Integrator
from trip_pay_payment.models.priced_supplier_contract_item_with_acquirer import PricedSupplierContractItemWithAcquirer
from trip_pay_payment.models.quote_lightweight import QuoteLightweight
from typing import Optional, Set
from typing_extensions import Self

class PricedSupplierContractWithAcquirer(BaseModel):
    """
    Details of the booking entries that went in for one particular supplier directly.
    """ # noqa: E501
    federated_organization_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The auth realm owner ID", alias="federatedOrganizationIdentifier")
    federated_organization_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The auth realm owner name", alias="federatedOrganizationName")
    user: AuthenticatedUser = Field(description="The authenticated user that made the payment request")
    ip_address: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Caller's IP address", alias="ipAddress")
    trace_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Way to track which booking contracts were made together", alias="traceId")
    source_url: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Where did the booking occur", alias="sourceUrl")
    identifier: UUID = Field(description="Unique identifier used to track the contract. Create a UUID for this purpose.")
    supplier_identifier: UUID = Field(description="Supplier identifier", alias="supplierIdentifier")
    supplier_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Supplier name", alias="supplierName")
    display_price_quote: QuoteLightweight = Field(description="The quote used to create totalDisplayPrice.", alias="displayPriceQuote")
    supplier_price_quote: QuoteLightweight = Field(description="The quote used to create totalSupplierPrice.", alias="supplierPriceQuote")
    internal_price_quote: QuoteLightweight = Field(description="The quote used to create totalInternalPrice.", alias="internalPriceQuote")
    capture_price_quote: QuoteLightweight = Field(description="The quote used to create totalCapturePrice.", alias="capturePriceQuote")
    item_list: Annotated[List[PricedSupplierContractItemWithAcquirer], Field(min_length=1, max_length=2147483647)] = Field(alias="itemList")
    acquirer: Integrator
    external_supplier_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Track supplier with its external supplier identifier", alias="externalSupplierIdentifier")
    external_supplier_booking_code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="External booking code generated by the affiliate", alias="externalSupplierBookingCode")
    external_transaction_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="External transaction identifier populated when agent responsible for acquiring", alias="externalTransactionIdentifier")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Place to add more data related to the booking contract.")
    total_display_price: Optional[CustomMonetaryAmount] = Field(default=None, alias="totalDisplayPrice")
    total_supplier_price: Optional[CustomMonetaryAmount] = Field(default=None, alias="totalSupplierPrice")
    total_internal_price: Optional[CustomMonetaryAmount] = Field(default=None, alias="totalInternalPrice")
    total_capture_price: Optional[CustomMonetaryAmount] = Field(default=None, alias="totalCapturePrice")
    total_price: Optional[CustomMonetaryAmount] = Field(default=None, alias="totalPrice")
    __properties: ClassVar[List[str]] = ["federatedOrganizationIdentifier", "federatedOrganizationName", "user", "ipAddress", "traceId", "sourceUrl", "identifier", "supplierIdentifier", "supplierName", "displayPriceQuote", "supplierPriceQuote", "internalPriceQuote", "capturePriceQuote", "itemList", "acquirer", "externalSupplierIdentifier", "externalSupplierBookingCode", "externalTransactionIdentifier", "metadata", "totalDisplayPrice", "totalSupplierPrice", "totalInternalPrice", "totalCapturePrice", "totalPrice"]

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
        """Create an instance of PricedSupplierContractWithAcquirer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of display_price_quote
        if self.display_price_quote:
            _dict['displayPriceQuote'] = self.display_price_quote.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supplier_price_quote
        if self.supplier_price_quote:
            _dict['supplierPriceQuote'] = self.supplier_price_quote.to_dict()
        # override the default output from pydantic by calling `to_dict()` of internal_price_quote
        if self.internal_price_quote:
            _dict['internalPriceQuote'] = self.internal_price_quote.to_dict()
        # override the default output from pydantic by calling `to_dict()` of capture_price_quote
        if self.capture_price_quote:
            _dict['capturePriceQuote'] = self.capture_price_quote.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in item_list (list)
        _items = []
        if self.item_list:
            for _item_item_list in self.item_list:
                if _item_item_list:
                    _items.append(_item_item_list.to_dict())
            _dict['itemList'] = _items
        # override the default output from pydantic by calling `to_dict()` of acquirer
        if self.acquirer:
            _dict['acquirer'] = self.acquirer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_display_price
        if self.total_display_price:
            _dict['totalDisplayPrice'] = self.total_display_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_supplier_price
        if self.total_supplier_price:
            _dict['totalSupplierPrice'] = self.total_supplier_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_internal_price
        if self.total_internal_price:
            _dict['totalInternalPrice'] = self.total_internal_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_capture_price
        if self.total_capture_price:
            _dict['totalCapturePrice'] = self.total_capture_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_price
        if self.total_price:
            _dict['totalPrice'] = self.total_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PricedSupplierContractWithAcquirer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "federatedOrganizationIdentifier": obj.get("federatedOrganizationIdentifier"),
            "federatedOrganizationName": obj.get("federatedOrganizationName"),
            "user": AuthenticatedUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "ipAddress": obj.get("ipAddress"),
            "traceId": obj.get("traceId"),
            "sourceUrl": obj.get("sourceUrl"),
            "identifier": obj.get("identifier"),
            "supplierIdentifier": obj.get("supplierIdentifier"),
            "supplierName": obj.get("supplierName"),
            "displayPriceQuote": QuoteLightweight.from_dict(obj["displayPriceQuote"]) if obj.get("displayPriceQuote") is not None else None,
            "supplierPriceQuote": QuoteLightweight.from_dict(obj["supplierPriceQuote"]) if obj.get("supplierPriceQuote") is not None else None,
            "internalPriceQuote": QuoteLightweight.from_dict(obj["internalPriceQuote"]) if obj.get("internalPriceQuote") is not None else None,
            "capturePriceQuote": QuoteLightweight.from_dict(obj["capturePriceQuote"]) if obj.get("capturePriceQuote") is not None else None,
            "itemList": [PricedSupplierContractItemWithAcquirer.from_dict(_item) for _item in obj["itemList"]] if obj.get("itemList") is not None else None,
            "acquirer": Integrator.from_dict(obj["acquirer"]) if obj.get("acquirer") is not None else None,
            "externalSupplierIdentifier": obj.get("externalSupplierIdentifier"),
            "externalSupplierBookingCode": obj.get("externalSupplierBookingCode"),
            "externalTransactionIdentifier": obj.get("externalTransactionIdentifier"),
            "metadata": obj.get("metadata"),
            "totalDisplayPrice": CustomMonetaryAmount.from_dict(obj["totalDisplayPrice"]) if obj.get("totalDisplayPrice") is not None else None,
            "totalSupplierPrice": CustomMonetaryAmount.from_dict(obj["totalSupplierPrice"]) if obj.get("totalSupplierPrice") is not None else None,
            "totalInternalPrice": CustomMonetaryAmount.from_dict(obj["totalInternalPrice"]) if obj.get("totalInternalPrice") is not None else None,
            "totalCapturePrice": CustomMonetaryAmount.from_dict(obj["totalCapturePrice"]) if obj.get("totalCapturePrice") is not None else None,
            "totalPrice": CustomMonetaryAmount.from_dict(obj["totalPrice"]) if obj.get("totalPrice") is not None else None
        })
        return _obj


