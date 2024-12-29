# trip_pay_payment.AffiliateApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_affiliate_details**](AffiliateApi.md#show_affiliate_details) | **POST** /api/contract/affiliate/details | Show Affiliate Details


# **show_affiliate_details**
> AffiliateInformation show_affiliate_details(affiliate_details_request, wink_version=wink_version)

Show Affiliate Details

Returns basic affiliate details.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.affiliate_details_request import AffiliateDetailsRequest
from trip_pay_payment.models.affiliate_information import AffiliateInformation
from trip_pay_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trippay.io
# See configuration.py for a list of all supported configuration parameters.
configuration = trip_pay_payment.Configuration(
    host = "https://api.trippay.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with trip_pay_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trip_pay_payment.AffiliateApi(api_client)
    affiliate_details_request = trip_pay_payment.AffiliateDetailsRequest() # AffiliateDetailsRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Affiliate Details
        api_response = api_instance.show_affiliate_details(affiliate_details_request, wink_version=wink_version)
        print("The response of AffiliateApi->show_affiliate_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AffiliateApi->show_affiliate_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affiliate_details_request** | [**AffiliateDetailsRequest**](AffiliateDetailsRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**AffiliateInformation**](AffiliateInformation.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

