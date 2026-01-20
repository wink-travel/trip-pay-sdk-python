# trip_pay_payment.NotificationApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_notification**](NotificationApi.md#remove_notification) | **DELETE** /api/message/{messageIdentifier} | Delete Notification
[**remove_notification1**](NotificationApi.md#remove_notification1) | **DELETE** /api/managing-entity/{managingEntityIdentifier}/message/{messageIdentifier} | Delete Notification
[**show_all_notifications**](NotificationApi.md#show_all_notifications) | **GET** /api/message/list | Show Notifications
[**show_notification**](NotificationApi.md#show_notification) | **GET** /api/message/{messageIdentifier} | Show Notification
[**show_notification1**](NotificationApi.md#show_notification1) | **GET** /api/managing-entity/{managingEntityIdentifier}/message/{messageIdentifier} | Show Notification
[**show_notifications**](NotificationApi.md#show_notifications) | **GET** /api/managing-entity/{managingEntityIdentifier}/message/list | Show Notifications
[**show_unread_message_count**](NotificationApi.md#show_unread_message_count) | **GET** /api/message/count | Show Unread Count
[**show_unread_message_count1**](NotificationApi.md#show_unread_message_count1) | **GET** /api/managing-entity/{managingEntityIdentifier}/message/count | Show Unread Count


# **remove_notification**
> NotificationAuthenticatedEntity remove_notification(message_identifier, wink_version=wink_version, accept=accept)

Delete Notification

Remove announcement specified by its identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.notification_authenticated_entity import NotificationAuthenticatedEntity
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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    message_identifier = 'message-1' # str | Message identifier to be removed
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Notification
        api_response = api_instance.remove_notification(message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->remove_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->remove_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_identifier** | **str**| Message identifier to be removed | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**NotificationAuthenticatedEntity**](NotificationAuthenticatedEntity.md)

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

# **remove_notification1**
> Notification remove_notification1(managing_entity_identifier, message_identifier, wink_version=wink_version, accept=accept)

Delete Notification

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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    managing_entity_identifier = 'company-1' # str | Remove a message that belongs to this company identifier
    message_identifier = 'message-1' # str | Message identifier to be removed
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Notification
        api_response = api_instance.remove_notification1(managing_entity_identifier, message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->remove_notification1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->remove_notification1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Remove a message that belongs to this company identifier | 
 **message_identifier** | **str**| Message identifier to be removed | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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

# **show_all_notifications**
> List[NotificationAuthenticatedEntity] show_all_notifications(wink_version=wink_version, accept=accept)

Show Notifications

Retrieve all the messages for this company

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.notification_authenticated_entity import NotificationAuthenticatedEntity
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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Notifications
        api_response = api_instance.show_all_notifications(wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_all_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_all_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[NotificationAuthenticatedEntity]**](NotificationAuthenticatedEntity.md)

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
> NotificationAuthenticatedEntity show_notification(message_identifier, wink_version=wink_version, accept=accept)

Show Notification

Retrieve messages for a specific company by ID

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.notification_authenticated_entity import NotificationAuthenticatedEntity
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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    message_identifier = 'message-1' # str | Message identifier to be retrieved
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Notification
        api_response = api_instance.show_notification(message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_identifier** | **str**| Message identifier to be retrieved | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**NotificationAuthenticatedEntity**](NotificationAuthenticatedEntity.md)

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

# **show_notification1**
> Notification show_notification1(managing_entity_identifier, message_identifier, wink_version=wink_version, accept=accept)

Show Notification

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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    managing_entity_identifier = 'company-1' # str | Retrieve a message for this company identifier
    message_identifier = 'message-1' # str | Message identifier to be retrieved
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Notification
        api_response = api_instance.show_notification1(managing_entity_identifier, message_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_notification1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_notification1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Retrieve a message for this company identifier | 
 **message_identifier** | **str**| Message identifier to be retrieved | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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
> List[Notification] show_notifications(managing_entity_identifier, wink_version=wink_version, accept=accept)

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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    managing_entity_identifier = 'managing_entity_identifier_example' # str | ID of entity to retrieve stream for
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Notifications
        api_response = api_instance.show_notifications(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| ID of entity to retrieve stream for | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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
> CountResponseAuthenticatedEntity show_unread_message_count(wink_version=wink_version, accept=accept)

Show Unread Count

Retrieve count of unread messages

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.count_response_authenticated_entity import CountResponseAuthenticatedEntity
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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Unread Count
        api_response = api_instance.show_unread_message_count(wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_unread_message_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_unread_message_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**CountResponseAuthenticatedEntity**](CountResponseAuthenticatedEntity.md)

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

# **show_unread_message_count1**
> CountResponse show_unread_message_count1(managing_entity_identifier, wink_version=wink_version, accept=accept)

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
    api_instance = trip_pay_payment.NotificationApi(api_client)
    managing_entity_identifier = 'company-1' # str | Show unread message count for this company identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Unread Count
        api_response = api_instance.show_unread_message_count1(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of NotificationApi->show_unread_message_count1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->show_unread_message_count1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Show unread message count for this company identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
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

