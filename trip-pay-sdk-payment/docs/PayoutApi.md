# trip_pay_payment.PayoutApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ephemeral_key**](PayoutApi.md#create_ephemeral_key) | **POST** /api/issuing-card/ephemeral | Create Stripe ephemeral key


# **create_ephemeral_key**
> CreateIssuingCardEphemeralKeyResponse create_ephemeral_key(create_issuing_card_ephemeral_key_request, wink_version=wink_version)

Create Stripe ephemeral key

Ephemeral keys are required to do display an issuing card to the user, among other things.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.create_issuing_card_ephemeral_key_request import CreateIssuingCardEphemeralKeyRequest
from trip_pay_payment.models.create_issuing_card_ephemeral_key_response import CreateIssuingCardEphemeralKeyResponse
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
    api_instance = trip_pay_payment.PayoutApi(api_client)
    create_issuing_card_ephemeral_key_request = trip_pay_payment.CreateIssuingCardEphemeralKeyRequest() # CreateIssuingCardEphemeralKeyRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Stripe ephemeral key
        api_response = api_instance.create_ephemeral_key(create_issuing_card_ephemeral_key_request, wink_version=wink_version)
        print("The response of PayoutApi->create_ephemeral_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutApi->create_ephemeral_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_issuing_card_ephemeral_key_request** | [**CreateIssuingCardEphemeralKeyRequest**](CreateIssuingCardEphemeralKeyRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**CreateIssuingCardEphemeralKeyResponse**](CreateIssuingCardEphemeralKeyResponse.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

