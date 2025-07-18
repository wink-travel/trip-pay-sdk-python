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

from trip_pay_payment.models.profile_user import ProfileUser

class TestProfileUser(unittest.TestCase):
    """ProfileUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProfileUser:
        """Test ProfileUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProfileUser`
        """
        model = ProfileUser()
        if include_optional:
            return ProfileUser(
                first_name = 'Avid',
                last_name = 'Travelman',
                email = 'avid@travelman.com',
                phone = '0123456789',
                profile_picture_url = '',
                full_name = 'John Smith'
            )
        else:
            return ProfileUser(
        )
        """

    def testProfileUser(self):
        """Test ProfileUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
