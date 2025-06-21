# trip_pay_payment.NotificationLightweightApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_notification**](NotificationLightweightApi.md#remove_notification) | **DELETE** /api/account/{accountIdentifier}/message/{messageIdentifier} | Delete NotificationLightweight
[**show_notification**](NotificationLightweightApi.md#show_notification) | **GET** /api/account/{accountIdentifier}/message/{messageIdentifier} | Show NotificationLightweight
[**show_notifications**](NotificationLightweightApi.md#show_notifications) | **GET** /api/account/{accountIdentifier}/message/list | Show Notifications
[**show_unread_message_count**](NotificationLightweightApi.md#show_unread_message_count) | **GET** /api/account/{accountIdentifier}/message/count | Show Unread Count


# **remove_notification**
> Notification remove_notification(account_identifier, message_identifier, wink_version=wink_version, accept=accept)

Delete NotificationLightweight

Remove announcement specified by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.notification import Notification
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
    api_instance = trip_pay_payment.NotificationLightweightApi(api_client)
    account_identifier = 'company-1' # str | Remove a message that belongs to this company identifier
    message_identifier = 'message-1' # str | Message identifier to be removed
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete NotificationLightweight
        api_response = api_instance.remove_notification(account_identifier, message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationLightweightApi->remove_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationLightweightApi->remove_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Remove a message that belongs to this company identifier | 
 **message_identifier** | **str**| Message identifier to be removed | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **show_notification**
> Notification show_notification(account_identifier, message_identifier, wink_version=wink_version, accept=accept)

Show NotificationLightweight

Retrieve messages for a specific company by ID

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.notification import Notification
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
    api_instance = trip_pay_payment.NotificationLightweightApi(api_client)
    account_identifier = 'company-1' # str | Retrieve a message for this company identifier
    message_identifier = 'message-1' # str | Message identifier to be retrieved
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show NotificationLightweight
        api_response = api_instance.show_notification(account_identifier, message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationLightweightApi->show_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationLightweightApi->show_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Retrieve a message for this company identifier | 
 **message_identifier** | **str**| Message identifier to be retrieved | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **show_notifications**
> List[Notification] show_notifications(account_identifier, wink_version=wink_version, accept=accept)

Show Notifications

Retrieve all the messages for this account.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.notification import Notification
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
    api_instance = trip_pay_payment.NotificationLightweightApi(api_client)
    account_identifier = 'account_identifier_example' # str | ID of entity to retrieve stream for
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Notifications
        api_response = api_instance.show_notifications(account_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationLightweightApi->show_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationLightweightApi->show_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| ID of entity to retrieve stream for | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Notification]**](Notification.md)

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

# **show_unread_message_count**
> CountResponse show_unread_message_count(account_identifier, wink_version=wink_version, accept=accept)

Show Unread Count

Retrieve count of unread messages

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.count_response import CountResponse
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
    api_instance = trip_pay_payment.NotificationLightweightApi(api_client)
    account_identifier = 'company-1' # str | Show unread message count for this company identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Unread Count
        api_response = api_instance.show_unread_message_count(account_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationLightweightApi->show_unread_message_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationLightweightApi->show_unread_message_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| Show unread message count for this company identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**CountResponse**](CountResponse.md)

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

