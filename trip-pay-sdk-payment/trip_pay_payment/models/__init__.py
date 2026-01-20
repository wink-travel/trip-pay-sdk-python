# coding: utf-8

# flake8: noqa
"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None  

    The version of the OpenAPI document: 30.31.0
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

# import models into model package
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.account_status_entry import AccountStatusEntry
from trip_pay_payment.models.account_status_response import AccountStatusResponse
from trip_pay_payment.models.acquirer_credentials import AcquirerCredentials
from trip_pay_payment.models.affiliate_details_request import AffiliateDetailsRequest
from trip_pay_payment.models.affiliate_information import AffiliateInformation
from trip_pay_payment.models.aggregate_booking_contract_cancellation_state import AggregateBookingContractCancellationState
from trip_pay_payment.models.aggregate_booking_contract_capture_currencies_by_account_response import AggregateBookingContractCaptureCurrenciesByAccountResponse
from trip_pay_payment.models.aggregate_descriptor_payment import AggregateDescriptorPayment
from trip_pay_payment.models.application import Application
from trip_pay_payment.models.authenticated_user import AuthenticatedUser
from trip_pay_payment.models.available_funds import AvailableFunds
from trip_pay_payment.models.bank_account import BankAccount
from trip_pay_payment.models.beneficiary import Beneficiary
from trip_pay_payment.models.beneficiary_aggregate_data import BeneficiaryAggregateData
from trip_pay_payment.models.beneficiary_charge import BeneficiaryCharge
from trip_pay_payment.models.booking_contract import BookingContract
from trip_pay_payment.models.booking_contract_cancellable_response import BookingContractCancellableResponse
from trip_pay_payment.models.booking_contract_grid_response import BookingContractGridResponse
from trip_pay_payment.models.booking_contract_item import BookingContractItem
from trip_pay_payment.models.booking_contract_item_cancellable_response import BookingContractItemCancellableResponse
from trip_pay_payment.models.booking_contract_payment_details import BookingContractPaymentDetails
from trip_pay_payment.models.cancel_booking_contract_request import CancelBookingContractRequest
from trip_pay_payment.models.change_managing_entity_name_request_authenticated_entity import ChangeManagingEntityNameRequestAuthenticatedEntity
from trip_pay_payment.models.composite_filter_descriptor_payment import CompositeFilterDescriptorPayment
from trip_pay_payment.models.contact import Contact
from trip_pay_payment.models.count_response import CountResponse
from trip_pay_payment.models.count_response_authenticated_entity import CountResponseAuthenticatedEntity
from trip_pay_payment.models.country_lightweight import CountryLightweight
from trip_pay_payment.models.create_agent_sale_request import CreateAgentSaleRequest
from trip_pay_payment.models.create_application_response import CreateApplicationResponse
from trip_pay_payment.models.create_mapping_request import CreateMappingRequest
from trip_pay_payment.models.custom_monetary_amount import CustomMonetaryAmount
from trip_pay_payment.models.daily_rate import DailyRate
from trip_pay_payment.models.external_booking_contract import ExternalBookingContract
from trip_pay_payment.models.fee import Fee
from trip_pay_payment.models.filter_descriptor_payment import FilterDescriptorPayment
from trip_pay_payment.models.geo_json_point import GeoJsonPoint
from trip_pay_payment.models.geo_name_lightweight import GeoNameLightweight
from trip_pay_payment.models.geo_name_lightweight_payment import GeoNameLightweightPayment
from trip_pay_payment.models.group_descriptor_payment import GroupDescriptorPayment
from trip_pay_payment.models.guest_user import GuestUser
from trip_pay_payment.models.immediate_refund_request import ImmediateRefundRequest
from trip_pay_payment.models.integrator import Integrator
from trip_pay_payment.models.invite_manager_request_affiliate import InviteManagerRequestAffiliate
from trip_pay_payment.models.key_value_pair import KeyValuePair
from trip_pay_payment.models.key_value_pair_authenticated_entity import KeyValuePairAuthenticatedEntity
from trip_pay_payment.models.managed_by_entity import ManagedByEntity
from trip_pay_payment.models.managed_by_entity_rules import ManagedByEntityRules
from trip_pay_payment.models.managed_by_entity_rules_affiliate import ManagedByEntityRulesAffiliate
from trip_pay_payment.models.manager_invite_affiliate import ManagerInviteAffiliate
from trip_pay_payment.models.managing_entity_affiliate import ManagingEntityAffiliate
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
from trip_pay_payment.models.managing_entity_manager import ManagingEntityManager
from trip_pay_payment.models.managing_entity_manager_payment import ManagingEntityManagerPayment
from trip_pay_payment.models.managing_entity_payment import ManagingEntityPayment
from trip_pay_payment.models.managing_entity_provision_payment import ManagingEntityProvisionPayment
from trip_pay_payment.models.managing_entity_supplier import ManagingEntitySupplier
from trip_pay_payment.models.mapping import Mapping
from trip_pay_payment.models.media_author_attribution import MediaAuthorAttribution
from trip_pay_payment.models.multi_booking_contract_response import MultiBookingContractResponse
from trip_pay_payment.models.notification import Notification
from trip_pay_payment.models.notification_authenticated_entity import NotificationAuthenticatedEntity
from trip_pay_payment.models.page_account import PageAccount
from trip_pay_payment.models.page_booking_contract import PageBookingContract
from trip_pay_payment.models.page_managing_entity_payment import PageManagingEntityPayment
from trip_pay_payment.models.page_mapping import PageMapping
from trip_pay_payment.models.pageable_object_payment import PageableObjectPayment
from trip_pay_payment.models.payable_contract import PayableContract
from trip_pay_payment.models.payable_contract_request import PayableContractRequest
from trip_pay_payment.models.payable_contract_response import PayableContractResponse
from trip_pay_payment.models.payable_contract_supplier import PayableContractSupplier
from trip_pay_payment.models.payable_contract_supplier_item import PayableContractSupplierItem
from trip_pay_payment.models.payable_contract_supplier_item_beneficiary import PayableContractSupplierItemBeneficiary
from trip_pay_payment.models.payout import Payout
from trip_pay_payment.models.payout_fee import PayoutFee
from trip_pay_payment.models.pending_refund import PendingRefund
from trip_pay_payment.models.personal import Personal
from trip_pay_payment.models.pet_info_lightweight import PetInfoLightweight
from trip_pay_payment.models.preferences import Preferences
from trip_pay_payment.models.priced_supplier_contract_item_with_acquirer import PricedSupplierContractItemWithAcquirer
from trip_pay_payment.models.priced_supplier_contract_with_acquirer import PricedSupplierContractWithAcquirer
from trip_pay_payment.models.profile_lightweight import ProfileLightweight
from trip_pay_payment.models.profile_user import ProfileUser
from trip_pay_payment.models.quote_lightweight import QuoteLightweight
from trip_pay_payment.models.raw_daily_rate import RawDailyRate
from trip_pay_payment.models.refund import Refund
from trip_pay_payment.models.refund_request import RefundRequest
from trip_pay_payment.models.remove_entry_response import RemoveEntryResponse
from trip_pay_payment.models.revoke_client_id_response import RevokeClientIdResponse
from trip_pay_payment.models.set_tax_identifier_request import SetTaxIdentifierRequest
from trip_pay_payment.models.simple_address import SimpleAddress
from trip_pay_payment.models.simple_address_authenticated_entity import SimpleAddressAuthenticatedEntity
from trip_pay_payment.models.simple_date_time_itinerary import SimpleDateTimeItinerary
from trip_pay_payment.models.simple_description import SimpleDescription
from trip_pay_payment.models.simple_multimedia import SimpleMultimedia
from trip_pay_payment.models.simple_multimedia_authenticated_entity import SimpleMultimediaAuthenticatedEntity
from trip_pay_payment.models.simple_multimedia_payment import SimpleMultimediaPayment
from trip_pay_payment.models.sort_descriptor_payment import SortDescriptorPayment
from trip_pay_payment.models.sort_object_payment import SortObjectPayment
from trip_pay_payment.models.state import State
from trip_pay_payment.models.state_payment import StatePayment
from trip_pay_payment.models.sub_country_lightweight import SubCountryLightweight
from trip_pay_payment.models.sub_sub_country_lightweight import SubSubCountryLightweight
from trip_pay_payment.models.supplier_contract_item_policy import SupplierContractItemPolicy
from trip_pay_payment.models.total_aggregate_funds import TotalAggregateFunds
from trip_pay_payment.models.unique_request_authenticated_entity import UniqueRequestAuthenticatedEntity
from trip_pay_payment.models.unique_result import UniqueResult
from trip_pay_payment.models.unique_result_authenticated_entity import UniqueResultAuthenticatedEntity
from trip_pay_payment.models.unique_result_payment import UniqueResultPayment
from trip_pay_payment.models.update_account_representative_request_authenticated_entity import UpdateAccountRepresentativeRequestAuthenticatedEntity
from trip_pay_payment.models.update_application_response import UpdateApplicationResponse
from trip_pay_payment.models.update_managed_by_agency_request_affiliate import UpdateManagedByAgencyRequestAffiliate
from trip_pay_payment.models.update_managing_entity_information_request_authenticated_entity import UpdateManagingEntityInformationRequestAuthenticatedEntity
from trip_pay_payment.models.update_mapping_request import UpdateMappingRequest
from trip_pay_payment.models.upsert_account_mapping_request import UpsertAccountMappingRequest
from trip_pay_payment.models.upsert_account_request import UpsertAccountRequest
from trip_pay_payment.models.upsert_application_request import UpsertApplicationRequest
from trip_pay_payment.models.upsert_bank_account_request import UpsertBankAccountRequest
from trip_pay_payment.models.upsert_image_request_authenticated_entity import UpsertImageRequestAuthenticatedEntity
from trip_pay_payment.models.upsert_webhook_managing_entity_request import UpsertWebhookManagingEntityRequest
from trip_pay_payment.models.upsert_webhook_request import UpsertWebhookRequest
from trip_pay_payment.models.verify_account_request import VerifyAccountRequest
from trip_pay_payment.models.webhook import Webhook

