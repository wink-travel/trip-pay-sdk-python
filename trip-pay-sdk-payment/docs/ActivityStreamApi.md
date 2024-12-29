# trip_pay_payment.ActivityStreamApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity**](ActivityStreamApi.md#create_activity) | **POST** /api/activity-stream | Create Activity Stream
[**show_stream**](ActivityStreamApi.md#show_stream) | **GET** /api/activity-stream/{entityIdentifier}/list | Show Activity Stream


# **create_activity**
> ActivityStream create_activity(upsert_activity_stream_request, wink_version=wink_version)

Create Activity Stream

Add a new activity stream entry.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.activity_stream import ActivityStream
from trip_pay_payment.models.upsert_activity_stream_request import UpsertActivityStreamRequest
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
    api_instance = trip_pay_payment.ActivityStreamApi(api_client)
    upsert_activity_stream_request = trip_pay_payment.UpsertActivityStreamRequest() # UpsertActivityStreamRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Activity Stream
        api_response = api_instance.create_activity(upsert_activity_stream_request, wink_version=wink_version)
        print("The response of ActivityStreamApi->create_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStreamApi->create_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_activity_stream_request** | [**UpsertActivityStreamRequest**](UpsertActivityStreamRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**ActivityStream**](ActivityStream.md)

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

# **show_stream**
> List[ActivityStream] show_stream(entity_identifier, wink_version=wink_version, accept=accept)

Show Activity Stream

Displays activity stream for specified entity ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.activity_stream import ActivityStream
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
    api_instance = trip_pay_payment.ActivityStreamApi(api_client)
    entity_identifier = 'entity_identifier_example' # str | ID of entity to retrieve stream for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Activity Stream
        api_response = api_instance.show_stream(entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ActivityStreamApi->show_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStreamApi->show_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_identifier** | **str**| ID of entity to retrieve stream for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[ActivityStream]**](ActivityStream.md)

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

