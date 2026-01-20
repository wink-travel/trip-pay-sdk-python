# coding: utf-8

"""
    Wink API

     # Introduction  Welcome to the Wink API - A programmer-friendly way to manage, sell and book travel inventory on the Wink platform. The API gives you all the tools you need to ready your properties and inventory for sale across 1000s of our native sales channels.  Integrators, affiliates, travel agents and content creators have the ability search for your travel inventory and promote / sell it in a wide variety of ways.   # Integrations  We have already integrated with the most well-known channel managers so you don't have to. To see our current integrations, please go to https://extranet.wink.travel and scroll to Connectivity section. Once your properties are set up, you can finish the setup by mapping your property to Wink using your channel manager partner portal. If your properties don't have a channel manager, you can easily manage rates and availability with this API.   # Intended Audience  Programmers are [most likely] a requirement to start integrating with Wink. Companies and organizations that would most benefit from integrating with us are new and existing travel companies that have relationships with suppliers and that need an advanced system from which to manage their travel inventory and get that same inventory out to as many eyeballs as possible at the lowest price possible.  - Hotel chains  - Hotel brands  - Travel tech companies  - Destination sites  - Integrators  - Aggregators  - Destination management companies  - Travel agencies  - OTAs   ## APIs  Not every integrator needs every API. For that reason, we have separated APIs into context.  ### Common APIs  - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Channel manager](/channel-manager): The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties. - [Managing Entity](/managing-entity): Endpoints that quickly show you which entities you have access to. - [Notifications](/notifications): The Notifications API is a way for us to stay in touch with your user, property or affiliate account. - [Payment](/payment): All APIs related to TripPay account management, booking, mapping and integration features. - [Ping](/ping): The Ping API is a quick test endpoint to verify that your credentials work. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [User Settings](/user-settings): The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink.  ### Consumer APIs  Consume endpoints are for developers who want to find existing travel inventory and either book it or use it to advertise through one of their Wink affiliate accounts.   - [Configuration](/customization-client): A single endpoint to retrieve whitelabel + customization information for the booking customization.  - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags.  - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API..  - [Booking](/booking): All APIs related to creating bookings on the platform.  - [Travel Agent](/travel-agent): The Travel Agent API exposes endpoints to manage agent-facilitated bookings.  ### Supplier APIs  Produce endpoints are for developers who want to create and manage travel inventory.  #### Property  - [Property Registration](/extranet/property/register): As a producer, this is, oftentimes, where you start your journey. These endpoints let you create properties on Wink. - [Property](/extranet/property): This collection of property endpoints are mostly management endpoints that let you display, change status and similar for your existing properties. - [Facilities](/extranet/facilities): This collection of endpoints let you manage facilities; such as room types. - [Experiences](/extranet/experiences): This collection of endpoints let you manage experiences, such as activities. - [Monetize](/extranet/monetize): The Monetize API exposes endpoints for managing cancellation polies, rate plans, promotions and more on Wink. - [Distribution](/extranet/distribution): The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. - [Property Booking](/extranet/booking): The Property Booking API exposes endpoints for managing bookings and reviews at the property-level.  #### Affiliate  - [Affiliate](/affiliate): This collection of affiliate endpoints are mostly management endpoints that let you display, change status and similar for your existing accounts. - [Browse](/affiliate/browse): The Browse API exposes endpoints for affiliates to find suppliers and inventory to sell. - [Inventory](/affiliate/inventory): The Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. - [Sales Channel](/affiliate/sales-channel): The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. - [WinkLinks](/affiliate/winklinks): The WinkLinks API exposes endpoints for affiliates to manage their WinkLinks page.  ## SDKs  We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  ### Inventory   - Java SDK [https://github.com/wink-travel/wink-sdk-java](https://github.com/wink-travel/wink-sdk-java)  - Python SDK [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)  ### Payment  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java) - Python SDK [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)  ## Usage  These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic.  ## Versioning  We chose to version our endpoints in a way that we hope affects your integration minimally. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  Current version: `2.0` Prior versions: None  

    The version of the OpenAPI document: 30.31.0
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity

class TestManagingEntityAuthenticatedEntity(unittest.TestCase):
    """ManagingEntityAuthenticatedEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagingEntityAuthenticatedEntity:
        """Test ManagingEntityAuthenticatedEntity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagingEntityAuthenticatedEntity`
        """
        model = ManagingEntityAuthenticatedEntity()
        if include_optional:
            return ManagingEntityAuthenticatedEntity(
                id = 'doc-1',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version = 12,
                user_identifier = 'user-1',
                owner_identifier = 'wink-1',
                managers = [
                    trip_pay_payment.models.managing_entity_manager.ManagingEntityManager(
                        email = 'manager@me.com', 
                        status = 'ACCEPTED', 
                        user_identifier = '', 
                        first_name = 'John', 
                        last_name = 'Smith', 
                        secondary_email = 'johnsmith2@email.com', 
                        phone_number = '+12125551212', 
                        profile_picture = null, 
                        owner = True, 
                        roles = [
                            ''
                            ], 
                        name = '', )
                    ],
                managed_by = trip_pay_payment.models.managed_by_entity.ManagedByEntity(
                    identifier = 'agency-1', 
                    name = 'Agency X', 
                    commission_in_percent = 0.01, 
                    rules = null, 
                    valid = True, ),
                owner_type = 'INDIVIDUAL',
                type = 'APPLICATION',
                name = 'The Getaway Resort',
                description = 'My AffiliateAccount is the best company ever.',
                legal_name = 'Legal AffiliateAccount 1',
                url_name = 'the-getaway-resort-ubud-indonesia',
                unique_id = 'abc123',
                account_email = 'company@acme.com',
                account_phone_number = '+1 212 555 1212',
                url = 'https://trippay.io',
                currency_code = 'GBP',
                status = 'PENDING_APPROVAL',
                city = trip_pay_payment.models.geo_name_lightweight_payment.GeoNameLightweight_Payment(
                    geo_name_id = '5128581', 
                    type = 'CITY', 
                    name = 'New York City', 
                    url_name = 'new-york-city-united-states', 
                    ascii_name = 'New York City', 
                    location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                    feature_code = '', 
                    country_code = '', 
                    timezone = 'America/New_York', 
                    country = null, 
                    sub_country = null, 
                    sub_sub_country = null, ),
                address = trip_pay_payment.models.simple_address.SimpleAddress(
                    address1 = '234', 
                    address2 = 'Pebble #5001', 
                    state = 'CA', 
                    postal_code = '90210', 
                    county = 'Alameda county', 
                    city = '', 
                    country_code = '', 
                    country = 'United States', 
                    full_address = '11', ),
                plan = trip_pay_payment.models.managing_entity_provision_payment.ManagingEntityProvision_Payment(
                    subscription_id = 'sub_1234', 
                    invoice_id = 'inv_1234', 
                    customer_id = 'cust_1234', 
                    customer_email = 'avid@travelman.com', 
                    customer_phone = '+1 212 555 1212', 
                    price_lookup_key = 'STARTER_MONTHLY', 
                    status = 'ACTIVE', 
                    invoice_status = 'PAID', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    canceled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    trial_expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    metadata = {
                        'key' : ''
                        }, 
                    active = True, ),
                profile_picture = trip_pay_payment.models.simple_multimedia.SimpleMultimedia(
                    multimedia_identifier = 'image-1', 
                    identifier = 'cloudinary-image-1', 
                    type = 'IMAGE', 
                    source = 'CLOUDINARY', 
                    sort = 10, 
                    angle = '-90', 
                    width = 2560, 
                    height = 1600, 
                    published = True, 
                    category = '1', 
                    descriptions = [
                        trip_pay_payment.models.simple_description.SimpleDescription(
                            name = 'An example title', 
                            description = 'This is a longer description in the specified language.', 
                            language = 'en', 
                            creator = 'USER', 
                            md5_content_hash = '', 
                            hash_mismatch = True, )
                        ], 
                    lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                    attribution = [
                        trip_pay_payment.models.media_author_attribution.MediaAuthorAttribution(
                            url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                            name = 'Samuel Adams', )
                        ], 
                    is_landscape = True, ),
                logo = trip_pay_payment.models.simple_multimedia.SimpleMultimedia(
                    multimedia_identifier = 'image-1', 
                    identifier = 'cloudinary-image-1', 
                    type = 'IMAGE', 
                    source = 'CLOUDINARY', 
                    sort = 10, 
                    angle = '-90', 
                    width = 2560, 
                    height = 1600, 
                    published = True, 
                    category = '1', 
                    descriptions = [
                        trip_pay_payment.models.simple_description.SimpleDescription(
                            name = 'An example title', 
                            description = 'This is a longer description in the specified language.', 
                            language = 'en', 
                            creator = 'USER', 
                            md5_content_hash = '', 
                            hash_mismatch = True, )
                        ], 
                    lifestyle_type = 'LIFESTYLE_HEALTH_FITNESS', 
                    attribution = [
                        trip_pay_payment.models.media_author_attribution.MediaAuthorAttribution(
                            url = 'https://maps.google.com/maps/contrib/111628493169070103594', 
                            name = 'Samuel Adams', )
                        ], 
                    is_landscape = True, ),
                marketing_optin_allowed = True,
                place_id = 'place-1'
            )
        else:
            return ManagingEntityAuthenticatedEntity(
                user_identifier = 'user-1',
                owner_identifier = 'wink-1',
                managers = [
                    trip_pay_payment.models.managing_entity_manager.ManagingEntityManager(
                        email = 'manager@me.com', 
                        status = 'ACCEPTED', 
                        user_identifier = '', 
                        first_name = 'John', 
                        last_name = 'Smith', 
                        secondary_email = 'johnsmith2@email.com', 
                        phone_number = '+12125551212', 
                        profile_picture = null, 
                        owner = True, 
                        roles = [
                            ''
                            ], 
                        name = '', )
                    ],
                owner_type = 'INDIVIDUAL',
                type = 'APPLICATION',
                name = 'The Getaway Resort',
                description = 'My AffiliateAccount is the best company ever.',
                legal_name = 'Legal AffiliateAccount 1',
                url_name = 'the-getaway-resort-ubud-indonesia',
                unique_id = 'abc123',
                account_email = 'company@acme.com',
                account_phone_number = '+1 212 555 1212',
                url = 'https://trippay.io',
                currency_code = 'GBP',
                status = 'PENDING_APPROVAL',
                city = trip_pay_payment.models.geo_name_lightweight_payment.GeoNameLightweight_Payment(
                    geo_name_id = '5128581', 
                    type = 'CITY', 
                    name = 'New York City', 
                    url_name = 'new-york-city-united-states', 
                    ascii_name = 'New York City', 
                    location = {type=POINT, coordinates=[100.5581533, 13.7370197]}, 
                    feature_code = '', 
                    country_code = '', 
                    timezone = 'America/New_York', 
                    country = null, 
                    sub_country = null, 
                    sub_sub_country = null, ),
        )
        """

    def testManagingEntityAuthenticatedEntity(self):
        """Test ManagingEntityAuthenticatedEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
