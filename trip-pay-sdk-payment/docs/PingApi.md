# trip_pay_payment.PingApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](PingApi.md#ping) | **GET** /api/hello | Hello World
[**ping_error**](PingApi.md#ping_error) | **GET** /api/hello/error | Hello World Error


# **ping**
> str ping(accept=accept)

Hello World

Test the connection.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
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
    api_instance = trip_pay_payment.PingApi(api_client)
    accept = 'accept_example' # str |  (optional)

    try:
        # Hello World
        api_response = api_instance.ping(accept=accept)
        print("The response of PingApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PingApi->ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_error**
> str ping_error(accept=accept)

Hello World Error

Test the connection by sending an error message in return.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
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
    api_instance = trip_pay_payment.PingApi(api_client)
    accept = 'accept_example' # str |  (optional)

    try:
        # Hello World Error
        api_response = api_instance.ping_error(accept=accept)
        print("The response of PingApi->ping_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PingApi->ping_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

