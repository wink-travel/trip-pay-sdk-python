# trip_pay_payment.ExternalEventApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_external_event**](ExternalEventApi.md#show_external_event) | **GET** /api/administration/external-event/{eventIdentifier} | Show External Event
[**show_external_event_grid**](ExternalEventApi.md#show_external_event_grid) | **POST** /api/administration/external-event/grid | Show External Event Grid
[**show_external_event_list**](ExternalEventApi.md#show_external_event_list) | **GET** /api/administration/external-event/{entityIdentifier}/list | Show External Events


# **show_external_event**
> ExternalEvent show_external_event(event_identifier, wink_version=wink_version, accept=accept)

Show External Event

Displays external event for specified event ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.external_event import ExternalEvent
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
    api_instance = trip_pay_payment.ExternalEventApi(api_client)
    event_identifier = 'event_identifier_example' # str | ID of event to retrieve
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show External Event
        api_response = api_instance.show_external_event(event_identifier, wink_version=wink_version, accept=accept)
        print("The response of ExternalEventApi->show_external_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalEventApi->show_external_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_identifier** | **str**| ID of event to retrieve | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ExternalEvent**](ExternalEvent.md)

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

# **show_external_event_grid**
> PageExternalEvent show_external_event_grid(state, wink_version=wink_version)

Show External Event Grid

Displays external events for specified entity ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.page_external_event import PageExternalEvent
from trip_pay_payment.models.state import State
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
    api_instance = trip_pay_payment.ExternalEventApi(api_client)
    state = trip_pay_payment.State() # State | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show External Event Grid
        api_response = api_instance.show_external_event_grid(state, wink_version=wink_version)
        print("The response of ExternalEventApi->show_external_event_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalEventApi->show_external_event_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**State**](State.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageExternalEvent**](PageExternalEvent.md)

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

# **show_external_event_list**
> List[ExternalEvent] show_external_event_list(entity_identifier, wink_version=wink_version, accept=accept)

Show External Events

Displays external events for specified entity ID.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.external_event import ExternalEvent
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
    api_instance = trip_pay_payment.ExternalEventApi(api_client)
    entity_identifier = 'entity_identifier_example' # str | ID of entity to retrieve stream for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show External Events
        api_response = api_instance.show_external_event_list(entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ExternalEventApi->show_external_event_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalEventApi->show_external_event_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_identifier** | **str**| ID of entity to retrieve stream for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[ExternalEvent]**](ExternalEvent.md)

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

