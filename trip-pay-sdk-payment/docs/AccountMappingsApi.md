# trip_pay_payment.AccountMappingsApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_mapping**](AccountMappingsApi.md#create_account_mapping) | **POST** /api/account/{accountIdentifier}/mapping | Create Account Mapping
[**find_account_mapping**](AccountMappingsApi.md#find_account_mapping) | **GET** /api/account/{accountIdentifier}/mapping/{id} | Show Account Mapping
[**remove_account_mapping**](AccountMappingsApi.md#remove_account_mapping) | **DELETE** /api/account/{accountIdentifier}/mapping/{id} | Delete Account Mapping
[**show_account_mapping_grid**](AccountMappingsApi.md#show_account_mapping_grid) | **POST** /api/account/{accountIdentifier}/mapping/grid | Show Account Mappings
[**update_account_mapping**](AccountMappingsApi.md#update_account_mapping) | **PUT** /api/account/{accountIdentifier}/mapping/{id} | Update Account Mapping


# **create_account_mapping**
> Mapping create_account_mapping(account_identifier, upsert_account_mapping_request, wink_version=wink_version)

Create Account Mapping

Create a mapping between a local account and a remote account.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.mapping import Mapping
from trip_pay_payment.models.upsert_account_mapping_request import UpsertAccountMappingRequest
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
    api_instance = trip_pay_payment.AccountMappingsApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    upsert_account_mapping_request = trip_pay_payment.UpsertAccountMappingRequest() # UpsertAccountMappingRequest | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Create Account Mapping
        api_response = api_instance.create_account_mapping(account_identifier, upsert_account_mapping_request, wink_version=wink_version)
        print("The response of AccountMappingsApi->create_account_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMappingsApi->create_account_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **upsert_account_mapping_request** | [**UpsertAccountMappingRequest**](UpsertAccountMappingRequest.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**Mapping**](Mapping.md)

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

# **find_account_mapping**
> Mapping find_account_mapping(account_identifier, id, wink_version=wink_version, accept=accept)

Show Account Mapping

Show a specific mapping by account and mapping identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.mapping import Mapping
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
    api_instance = trip_pay_payment.AccountMappingsApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    id = 'id_example' # str | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Account Mapping
        api_response = api_instance.find_account_mapping(account_identifier, id, wink_version=wink_version, accept=accept)
        print("The response of AccountMappingsApi->find_account_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMappingsApi->find_account_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**Mapping**](Mapping.md)

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

# **remove_account_mapping**
> RemoveEntryResponse remove_account_mapping(account_identifier, id, wink_version=wink_version, accept=accept)

Delete Account Mapping

Delete a specific mapping owned by account identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.remove_entry_response import RemoveEntryResponse
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
    api_instance = trip_pay_payment.AccountMappingsApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    id = 'id_example' # str | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Account Mapping
        api_response = api_instance.remove_account_mapping(account_identifier, id, wink_version=wink_version, accept=accept)
        print("The response of AccountMappingsApi->remove_account_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMappingsApi->remove_account_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**RemoveEntryResponse**](RemoveEntryResponse.md)

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

# **show_account_mapping_grid**
> PageMapping show_account_mapping_grid(account_identifier, state, wink_version=wink_version)

Show Account Mappings

List all mappings belonging to a specific account.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.page_mapping import PageMapping
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
    api_instance = trip_pay_payment.AccountMappingsApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    state = trip_pay_payment.State() # State | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Show Account Mappings
        api_response = api_instance.show_account_mapping_grid(account_identifier, state, wink_version=wink_version)
        print("The response of AccountMappingsApi->show_account_mapping_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMappingsApi->show_account_mapping_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **state** | [**State**](State.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PageMapping**](PageMapping.md)

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

# **update_account_mapping**
> Mapping update_account_mapping(account_identifier, id, upsert_account_mapping_request, wink_version=wink_version)

Update Account Mapping

Update an existing mapping owned by account identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.mapping import Mapping
from trip_pay_payment.models.upsert_account_mapping_request import UpsertAccountMappingRequest
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
    api_instance = trip_pay_payment.AccountMappingsApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    id = 'id_example' # str | 
    upsert_account_mapping_request = trip_pay_payment.UpsertAccountMappingRequest() # UpsertAccountMappingRequest | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Account Mapping
        api_response = api_instance.update_account_mapping(account_identifier, id, upsert_account_mapping_request, wink_version=wink_version)
        print("The response of AccountMappingsApi->update_account_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMappingsApi->update_account_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **id** | **str**|  | 
 **upsert_account_mapping_request** | [**UpsertAccountMappingRequest**](UpsertAccountMappingRequest.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**Mapping**](Mapping.md)

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

