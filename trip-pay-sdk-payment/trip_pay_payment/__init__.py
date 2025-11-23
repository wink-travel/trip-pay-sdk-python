# coding: utf-8

# flake8: noqa

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None  

    The version of the OpenAPI document: 30.30.3
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.47"

# Define package exports
__all__ = [
    "AccountApi",
    "AccountMappingsApi",
    "AffiliateApi",
    "AgentApi",
    "ApplicationApi",
    "ContractApi",
    "ManagingEntityApi",
    "MappingApi",
    "NotificationApi",
    "PingApi",
    "WebhookApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "Account",
    "AccountStatusResponse",
    "AcquirerCredentials",
    "Address",
    "AffiliateDetailsRequest",
    "AffiliateInformation",
    "AggregateBookingContractCancellationState",
    "AggregateBookingContractCaptureCurrenciesByAccountResponse",
    "AggregateDescriptor",
    "Application",
    "AuthenticatedUser",
    "AvailableFunds",
    "BankAccount",
    "Beneficiary",
    "BeneficiaryAggregateData",
    "BeneficiaryCharge",
    "BookingContract",
    "BookingContractCancellableResponse",
    "BookingContractGridResponse",
    "BookingContractItem",
    "BookingContractPaymentDetails",
    "CancelBookingContractRequest",
    "CompositeFilterDescriptor",
    "Contact",
    "CountResponse",
    "CountryLightweight",
    "CreateAccountRequest",
    "CreateAgentSaleRequest",
    "CreateApplicationResponse",
    "CreateMappingRequest",
    "CustomMonetaryAmount",
    "ExternalBookingContract",
    "FilterDescriptor",
    "GeoJsonPoint",
    "GeoNameLightweight",
    "GroupDescriptor",
    "GuestUser",
    "ImmediateRefundRequest",
    "Integrator",
    "KeyValuePair",
    "ManagingEntity",
    "Mapping",
    "MultiBookingContractResponse",
    "Notification",
    "PageAccount",
    "PageBookingContract",
    "PageMapping",
    "PageableObject",
    "PayableContract",
    "PayableContractRequest",
    "PayableContractResponse",
    "PayableContractSupplier",
    "PayableContractSupplierItem",
    "PayableContractSupplierItemBeneficiary",
    "Personal",
    "Preferences",
    "PricedSupplierContractWithAcquirer",
    "ProfileLightweight",
    "ProfileUser",
    "QuoteLightweight",
    "RefundRequest",
    "RemoveEntryResponse",
    "RevokeClientIdResponse",
    "SetTaxIdentifierRequest",
    "SimpleDateTimeItinerary",
    "SortDescriptor",
    "SortObject",
    "State",
    "SubCountryLightweight",
    "SubSubCountryLightweight",
    "SupplierContractItemPolicy",
    "TotalAggregateFunds",
    "UniqueResult",
    "UpdateApplicationResponse",
    "UpdateMappingRequest",
    "UpsertAccountMappingRequest",
    "UpsertAccountRequest",
    "UpsertAddressRequest",
    "UpsertApplicationRequest",
    "UpsertBankAccountRequest",
    "UpsertCityOnlyAddressRequest",
    "UpsertWebhookRequest",
    "VerifyAccountRequest",
    "Webhook",
]

# import apis into sdk package
from trip_pay_payment.api.account_api import AccountApi as AccountApi
from trip_pay_payment.api.account_mappings_api import AccountMappingsApi as AccountMappingsApi
from trip_pay_payment.api.affiliate_api import AffiliateApi as AffiliateApi
from trip_pay_payment.api.agent_api import AgentApi as AgentApi
from trip_pay_payment.api.application_api import ApplicationApi as ApplicationApi
from trip_pay_payment.api.contract_api import ContractApi as ContractApi
from trip_pay_payment.api.managing_entity_api import ManagingEntityApi as ManagingEntityApi
from trip_pay_payment.api.mapping_api import MappingApi as MappingApi
from trip_pay_payment.api.notification_api import NotificationApi as NotificationApi
from trip_pay_payment.api.ping_api import PingApi as PingApi
from trip_pay_payment.api.webhook_api import WebhookApi as WebhookApi

# import ApiClient
from trip_pay_payment.api_response import ApiResponse as ApiResponse
from trip_pay_payment.api_client import ApiClient as ApiClient
from trip_pay_payment.configuration import Configuration as Configuration
from trip_pay_payment.exceptions import OpenApiException as OpenApiException
from trip_pay_payment.exceptions import ApiTypeError as ApiTypeError
from trip_pay_payment.exceptions import ApiValueError as ApiValueError
from trip_pay_payment.exceptions import ApiKeyError as ApiKeyError
from trip_pay_payment.exceptions import ApiAttributeError as ApiAttributeError
from trip_pay_payment.exceptions import ApiException as ApiException

# import models into sdk package
from trip_pay_payment.models.account import Account as Account
from trip_pay_payment.models.account_status_response import AccountStatusResponse as AccountStatusResponse
from trip_pay_payment.models.acquirer_credentials import AcquirerCredentials as AcquirerCredentials
from trip_pay_payment.models.address import Address as Address
from trip_pay_payment.models.affiliate_details_request import AffiliateDetailsRequest as AffiliateDetailsRequest
from trip_pay_payment.models.affiliate_information import AffiliateInformation as AffiliateInformation
from trip_pay_payment.models.aggregate_booking_contract_cancellation_state import AggregateBookingContractCancellationState as AggregateBookingContractCancellationState
from trip_pay_payment.models.aggregate_booking_contract_capture_currencies_by_account_response import AggregateBookingContractCaptureCurrenciesByAccountResponse as AggregateBookingContractCaptureCurrenciesByAccountResponse
from trip_pay_payment.models.aggregate_descriptor import AggregateDescriptor as AggregateDescriptor
from trip_pay_payment.models.application import Application as Application
from trip_pay_payment.models.authenticated_user import AuthenticatedUser as AuthenticatedUser
from trip_pay_payment.models.available_funds import AvailableFunds as AvailableFunds
from trip_pay_payment.models.bank_account import BankAccount as BankAccount
from trip_pay_payment.models.beneficiary import Beneficiary as Beneficiary
from trip_pay_payment.models.beneficiary_aggregate_data import BeneficiaryAggregateData as BeneficiaryAggregateData
from trip_pay_payment.models.beneficiary_charge import BeneficiaryCharge as BeneficiaryCharge
from trip_pay_payment.models.booking_contract import BookingContract as BookingContract
from trip_pay_payment.models.booking_contract_cancellable_response import BookingContractCancellableResponse as BookingContractCancellableResponse
from trip_pay_payment.models.booking_contract_grid_response import BookingContractGridResponse as BookingContractGridResponse
from trip_pay_payment.models.booking_contract_item import BookingContractItem as BookingContractItem
from trip_pay_payment.models.booking_contract_payment_details import BookingContractPaymentDetails as BookingContractPaymentDetails
from trip_pay_payment.models.cancel_booking_contract_request import CancelBookingContractRequest as CancelBookingContractRequest
from trip_pay_payment.models.composite_filter_descriptor import CompositeFilterDescriptor as CompositeFilterDescriptor
from trip_pay_payment.models.contact import Contact as Contact
from trip_pay_payment.models.count_response import CountResponse as CountResponse
from trip_pay_payment.models.country_lightweight import CountryLightweight as CountryLightweight
from trip_pay_payment.models.create_account_request import CreateAccountRequest as CreateAccountRequest
from trip_pay_payment.models.create_agent_sale_request import CreateAgentSaleRequest as CreateAgentSaleRequest
from trip_pay_payment.models.create_application_response import CreateApplicationResponse as CreateApplicationResponse
from trip_pay_payment.models.create_mapping_request import CreateMappingRequest as CreateMappingRequest
from trip_pay_payment.models.custom_monetary_amount import CustomMonetaryAmount as CustomMonetaryAmount
from trip_pay_payment.models.external_booking_contract import ExternalBookingContract as ExternalBookingContract
from trip_pay_payment.models.filter_descriptor import FilterDescriptor as FilterDescriptor
from trip_pay_payment.models.geo_json_point import GeoJsonPoint as GeoJsonPoint
from trip_pay_payment.models.geo_name_lightweight import GeoNameLightweight as GeoNameLightweight
from trip_pay_payment.models.group_descriptor import GroupDescriptor as GroupDescriptor
from trip_pay_payment.models.guest_user import GuestUser as GuestUser
from trip_pay_payment.models.immediate_refund_request import ImmediateRefundRequest as ImmediateRefundRequest
from trip_pay_payment.models.integrator import Integrator as Integrator
from trip_pay_payment.models.key_value_pair import KeyValuePair as KeyValuePair
from trip_pay_payment.models.managing_entity import ManagingEntity as ManagingEntity
from trip_pay_payment.models.mapping import Mapping as Mapping
from trip_pay_payment.models.multi_booking_contract_response import MultiBookingContractResponse as MultiBookingContractResponse
from trip_pay_payment.models.notification import Notification as Notification
from trip_pay_payment.models.page_account import PageAccount as PageAccount
from trip_pay_payment.models.page_booking_contract import PageBookingContract as PageBookingContract
from trip_pay_payment.models.page_mapping import PageMapping as PageMapping
from trip_pay_payment.models.pageable_object import PageableObject as PageableObject
from trip_pay_payment.models.payable_contract import PayableContract as PayableContract
from trip_pay_payment.models.payable_contract_request import PayableContractRequest as PayableContractRequest
from trip_pay_payment.models.payable_contract_response import PayableContractResponse as PayableContractResponse
from trip_pay_payment.models.payable_contract_supplier import PayableContractSupplier as PayableContractSupplier
from trip_pay_payment.models.payable_contract_supplier_item import PayableContractSupplierItem as PayableContractSupplierItem
from trip_pay_payment.models.payable_contract_supplier_item_beneficiary import PayableContractSupplierItemBeneficiary as PayableContractSupplierItemBeneficiary
from trip_pay_payment.models.personal import Personal as Personal
from trip_pay_payment.models.preferences import Preferences as Preferences
from trip_pay_payment.models.priced_supplier_contract_with_acquirer import PricedSupplierContractWithAcquirer as PricedSupplierContractWithAcquirer
from trip_pay_payment.models.profile_lightweight import ProfileLightweight as ProfileLightweight
from trip_pay_payment.models.profile_user import ProfileUser as ProfileUser
from trip_pay_payment.models.quote_lightweight import QuoteLightweight as QuoteLightweight
from trip_pay_payment.models.refund_request import RefundRequest as RefundRequest
from trip_pay_payment.models.remove_entry_response import RemoveEntryResponse as RemoveEntryResponse
from trip_pay_payment.models.revoke_client_id_response import RevokeClientIdResponse as RevokeClientIdResponse
from trip_pay_payment.models.set_tax_identifier_request import SetTaxIdentifierRequest as SetTaxIdentifierRequest
from trip_pay_payment.models.simple_date_time_itinerary import SimpleDateTimeItinerary as SimpleDateTimeItinerary
from trip_pay_payment.models.sort_descriptor import SortDescriptor as SortDescriptor
from trip_pay_payment.models.sort_object import SortObject as SortObject
from trip_pay_payment.models.state import State as State
from trip_pay_payment.models.sub_country_lightweight import SubCountryLightweight as SubCountryLightweight
from trip_pay_payment.models.sub_sub_country_lightweight import SubSubCountryLightweight as SubSubCountryLightweight
from trip_pay_payment.models.supplier_contract_item_policy import SupplierContractItemPolicy as SupplierContractItemPolicy
from trip_pay_payment.models.total_aggregate_funds import TotalAggregateFunds as TotalAggregateFunds
from trip_pay_payment.models.unique_result import UniqueResult as UniqueResult
from trip_pay_payment.models.update_application_response import UpdateApplicationResponse as UpdateApplicationResponse
from trip_pay_payment.models.update_mapping_request import UpdateMappingRequest as UpdateMappingRequest
from trip_pay_payment.models.upsert_account_mapping_request import UpsertAccountMappingRequest as UpsertAccountMappingRequest
from trip_pay_payment.models.upsert_account_request import UpsertAccountRequest as UpsertAccountRequest
from trip_pay_payment.models.upsert_address_request import UpsertAddressRequest as UpsertAddressRequest
from trip_pay_payment.models.upsert_application_request import UpsertApplicationRequest as UpsertApplicationRequest
from trip_pay_payment.models.upsert_bank_account_request import UpsertBankAccountRequest as UpsertBankAccountRequest
from trip_pay_payment.models.upsert_city_only_address_request import UpsertCityOnlyAddressRequest as UpsertCityOnlyAddressRequest
from trip_pay_payment.models.upsert_webhook_request import UpsertWebhookRequest as UpsertWebhookRequest
from trip_pay_payment.models.verify_account_request import VerifyAccountRequest as VerifyAccountRequest
from trip_pay_payment.models.webhook import Webhook as Webhook

