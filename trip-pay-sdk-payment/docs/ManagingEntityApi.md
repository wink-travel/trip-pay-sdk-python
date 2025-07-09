# trip_pay_payment.ManagingEntityApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_managing_entities**](ManagingEntityApi.md#show_managing_entities) | **GET** /api/managing-entity/{managingEntityIdentifier} | Show Managing Entity
[**show_managing_entities1**](ManagingEntityApi.md#show_managing_entities1) | **GET** /api/managing-entity/list | Show Managing Entities


# **show_managing_entities**
> ManagingEntity show_managing_entities(managing_entity_identifier, wink_version=wink_version, accept=accept)

Show Managing Entity

Load single managing entity.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity import ManagingEntity
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
    api_instance = trip_pay_payment.ManagingEntityApi(api_client)
    managing_entity_identifier = 'managing_entity_identifier_example' # str | Managing entity ID
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Managing Entity
        api_response = api_instance.show_managing_entities(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->show_managing_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_managing_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Managing entity ID | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntity**](ManagingEntity.md)

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

# **show_managing_entities1**
> List[ManagingEntity] show_managing_entities1(wink_version=wink_version, accept=accept)

Show Managing Entities

Lists all entities, including user entity, owned by user.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity import ManagingEntity
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
    api_instance = trip_pay_payment.ManagingEntityApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Managing Entities
        api_response = api_instance.show_managing_entities1(wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->show_managing_entities1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_managing_entities1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[ManagingEntity]**](ManagingEntity.md)

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

