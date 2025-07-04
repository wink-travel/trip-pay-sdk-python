# coding: utf-8

"""
    Wink Payment API

    A programmatic way to create bookings, receive reactive and disburse funds globally.  ## APIs Not every integrator needs every APIs. For that reason, we have separated APIs into context.  - [Affiliate](/affiliate): All APIs related to selling travel inventory as an affiliate. - [Analytics](/analytics): All APIs related to tracking metrics across a wide variety of data source segments including, more entertaining, leaderboard metrics. - [Booking](/booking): All APIs related to creating platform bookings. - [Channel Manager](/channel-manager): All APIs related to channel managers who want to integrate with our platform. - [Extranet](/extranet): All APIs related to managing travel inventory and suppliers. - [Inventory](/inventory): All APIs related to retrieve known travel inventory as it was found using the Lookup API.. - [Lookup](/lookup): All APIs related to locating inventory by region, locale and property flags. - [Reference](/reference): All APIs related to retrieving platform-supported taxonomies. - [TripPay](/reactive): All APIs related to TripPay account management, booking, mapping and integration features.  ## SDKs We are actively working on supporting the most used languages out there. If you don't see your language here, reach out to us with a request to officially add your language. In the meantime, if you want to roll your own SDK, you can do so by downloading the OpenAPI spec and using one of the many available OpenAPI generators available: [https://openapi-generator.tech/docs/generators](https://openapi-generator.tech/docs/generators).  - Java SDK [https://github.com/wink-travel/trip-pay-sdk-java](https://github.com/wink-travel/trip-pay-sdk-java)  # Usage These features are made available to you via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). This API is language agnostic. We will link to SDKs for the most popular programming languages on this page as they become available.  ## Versioning We chose to version our endpoints in a way that we hope affects your integration with us the least. You request the version of our API you wish to work with via the `Wink-Version` header. When it's time for you to upgrade, you only have to change the version number to get access to our updated endpoints.  ## Release history - Follow updates on Github: https://github.com/wink-travel/wink-sdk-java/blob/master/CHANGELOG.md 

    The version of the OpenAPI document: 30.9.11
    Contact: bjorn@wink.travel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trip_pay_payment.models.page_account import PageAccount

class TestPageAccount(unittest.TestCase):
    """PageAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageAccount:
        """Test PageAccount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageAccount`
        """
        model = PageAccount()
        if include_optional:
            return PageAccount(
                total_elements = 56,
                total_pages = 56,
                size = 56,
                content = [
                    trip_pay_payment.models.account.Account(
                        id = 'doc-1', 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        version = 12, 
                        type = 'MERCHANT', 
                        owner_type = 'COMPANY', 
                        account_owner_identifier = 'account-1', 
                        name = 'My Company', 
                        legal_name = 'Legal Company 1', 
                        user_identifier = 'user-1', 
                        owner = trip_pay_payment.models.contact.Contact(
                            first_name = 'John', 
                            last_name = 'Smith', 
                            email = 'johnsmith@email.com', 
                            secondary_email = 'johnsmith2@email.com', 
                            phone_number = '+12125551212', 
                            full_name = 'John Smith', 
                            summary = 'John Smith (johnsmith@gmail.com / +12125551212)', ), 
                        account_email = 'company@acme.com', 
                        account_phone_number = '+1 212 555 1212', 
                        description = 'My Company is the best company ever.', 
                        url = 'https://trippay.io', 
                        status = 'REGISTERED', 
                        currency_code = 'GBP', 
                        address = trip_pay_payment.models.address.Address(
                            address1 = '234 Near da beach', 
                            address2 = 'Pebble #5001', 
                            state = 'CA', 
                            postal_code = '90210', 
                            county = 'Alameda county', 
                            city = trip_pay_payment.models.geo_name.GeoName(
                                geo_name_id = '5128581', 
                                type = 'CITY', 
                                name = 'New York City', 
                                url_name = 'new-york-city-united-states', 
                                ascii_name = 'New York City', 
                                alternate_names = [
                                    'NYC'
                                    ], 
                                location = {"type":"POINT","coordinates":[100.5581533,13.7370197]}, 
                                feature_class = '', 
                                feature_code = '', 
                                country_code = '', 
                                alternate_country_codes = [
                                    ''
                                    ], 
                                admin1_code = '', 
                                admin2_code = '', 
                                admin3_code = '', 
                                admin4_code = '', 
                                population = 8175133, 
                                elevation = 10, 
                                digital_elevation_model = '', 
                                timezone = 'America/New_York', 
                                modification_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                radius_in_meters = 56, 
                                country = trip_pay_payment.models.country.Country(
                                    iso = 'US', 
                                    iso3 = 'USA', 
                                    iso_numeric = 840, 
                                    fips = 'US', 
                                    name = 'United States', 
                                    capital = 'Washington', 
                                    area = 9629091.0, 
                                    population = 310232863, 
                                    continent = 'NA', 
                                    top_level_domain = '.us', 
                                    currency_code = 'USD', 
                                    currency_name = 'Dollar', 
                                    phone = '1', 
                                    postal_code_format = '#####-####', 
                                    postal_code_reg_ex = '^d{5}(-d{4})?$', 
                                    languages = [
                                        'en-US'
                                        ], 
                                    geo_name_id = '6252001', 
                                    neighbors = [
                                        'CA'
                                        ], ), 
                                sub_country = trip_pay_payment.models.sub_country.SubCountry(
                                    code = 'US.NY', 
                                    country_code = 'US', 
                                    sub_country_code = 'NY', 
                                    name = 'New York', 
                                    ascii_name = 'New York', 
                                    geo_name_id = '5128638', ), 
                                sub_sub_country = trip_pay_payment.models.sub_sub_country.SubSubCountry(
                                    code = '', 
                                    country_code = '', 
                                    sub_country_code = '', 
                                    sub_sub_country_code = '', 
                                    name = '', 
                                    ascii_name = '', 
                                    geo_name_id = '', ), ), 
                            valid = True, 
                            full_address = '11 At home, Suite 3C, New York City, NY 10010, United States', ), 
                        acquirers = [
                            trip_pay_payment.models.acquirer.Acquirer(
                                acquirer_id = 'acquirer-1', 
                                priority = 56, 
                                vendor = 'STRIPE', 
                                type = 'CREDIT_CARD', 
                                currency_code = 'GBP', 
                                credentials = [
                                    trip_pay_payment.models.acquirer_credentials.AcquirerCredentials(
                                        type = 'TOKEN', 
                                        key1 = 'token-1', 
                                        key2 = 'token-2', )
                                    ], 
                                webhook_secret = '', 
                                public_token = '', )
                            ], 
                        bank_accounts = [
                            trip_pay_payment.models.bank_account.BankAccount(
                                identifier = '', 
                                country_code = 'US', 
                                currency_code = 'USD', 
                                account_holder_name = 'Luxury Resorts', 
                                swift_code = 'HHKHD', 
                                routing_number = '12345678', 
                                account_number = '12345678', 
                                primary = True, )
                            ], 
                        owner_type_identifier = '', 
                        dob = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        tasks = [
                            Your EIN is incorrect.
                            ], 
                        preferred_disbursement_type = 'BANK_TRANSFER', )
                    ],
                number = 56,
                sort = [
                    trip_pay_payment.models.sort_object.SortObject(
                        direction = '', 
                        null_handling = '', 
                        ascending = True, 
                        property = '', 
                        ignore_case = True, )
                    ],
                first = True,
                last = True,
                number_of_elements = 56,
                pageable = trip_pay_payment.models.pageable_object.PageableObject(
                    offset = 56, 
                    sort = [
                        trip_pay_payment.models.sort_object.SortObject(
                            direction = '', 
                            null_handling = '', 
                            ascending = True, 
                            property = '', 
                            ignore_case = True, )
                        ], 
                    page_number = 56, 
                    page_size = 56, 
                    paged = True, 
                    unpaged = True, ),
                empty = True
            )
        else:
            return PageAccount(
        )
        """

    def testPageAccount(self):
        """Test PageAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
