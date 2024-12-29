# trip_pay_payment.MappingApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mapping**](MappingApi.md#create_mapping) | **POST** /api/mapping | Create Mapping
[**load_mapping**](MappingApi.md#load_mapping) | **GET** /api/mapping/{id} | Show Mapping
[**load_mapping_by_external_identifier**](MappingApi.md#load_mapping_by_external_identifier) | **GET** /api/mapping/external/{id} | Show External Mapping
[**load_mappings**](MappingApi.md#load_mappings) | **GET** /api/mapping/list | Show Mappings
[**remove_mapping**](MappingApi.md#remove_mapping) | **DELETE** /api/mapping/{id} | Delete Mapping
[**remove_mapping_by_external_identifier**](MappingApi.md#remove_mapping_by_external_identifier) | **DELETE** /api/mapping/external/{id} | Delete External Mapping
[**update_mapping**](MappingApi.md#update_mapping) | **PATCH** /api/mapping/{id} | Update Mapping
[**update_mapping_by_external_identifier**](MappingApi.md#update_mapping_by_external_identifier) | **PATCH** /api/mapping/external/{id} | Update External Mapping


# **create_mapping**
> Mapping create_mapping(create_mapping_request, wink_version=wink_version)

Create Mapping

Create a mapping between two accounts

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.create_mapping_request import CreateMappingRequest
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
    api_instance = trip_pay_payment.MappingApi(api_client)
    create_mapping_request = trip_pay_payment.CreateMappingRequest() # CreateMappingRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Mapping
        api_response = api_instance.create_mapping(create_mapping_request, wink_version=wink_version)
        print("The response of MappingApi->create_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->create_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mapping_request** | [**CreateMappingRequest**](CreateMappingRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

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

# **load_mapping**
> Mapping load_mapping(id, wink_version=wink_version, accept=accept)

Show Mapping

Show a specific mapping contract

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
    api_instance = trip_pay_payment.MappingApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Mapping
        api_response = api_instance.load_mapping(id, wink_version=wink_version, accept=accept)
        print("The response of MappingApi->load_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->load_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
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

# **load_mapping_by_external_identifier**
> Mapping load_mapping_by_external_identifier(id, wink_version=wink_version, accept=accept)

Show External Mapping

Show a specific mapping contract by external identifier

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
    api_instance = trip_pay_payment.MappingApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show External Mapping
        api_response = api_instance.load_mapping_by_external_identifier(id, wink_version=wink_version, accept=accept)
        print("The response of MappingApi->load_mapping_by_external_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->load_mapping_by_external_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
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

# **load_mappings**
> List[Mapping] load_mappings(wink_version=wink_version, accept=accept)

Show Mappings

List all mappings

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
    api_instance = trip_pay_payment.MappingApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Mappings
        api_response = api_instance.load_mappings(wink_version=wink_version, accept=accept)
        print("The response of MappingApi->load_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->load_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Mapping]**](Mapping.md)

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

# **remove_mapping**
> Mapping remove_mapping(id, wink_version=wink_version, accept=accept)

Delete Mapping

Delete a specific mapping contract

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
    api_instance = trip_pay_payment.MappingApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Mapping
        api_response = api_instance.remove_mapping(id, wink_version=wink_version, accept=accept)
        print("The response of MappingApi->remove_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->remove_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
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

# **remove_mapping_by_external_identifier**
> Mapping remove_mapping_by_external_identifier(id, wink_version=wink_version, accept=accept)

Delete External Mapping

Delete a specific mapping contract based on its external identifier

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
    api_instance = trip_pay_payment.MappingApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete External Mapping
        api_response = api_instance.remove_mapping_by_external_identifier(id, wink_version=wink_version, accept=accept)
        print("The response of MappingApi->remove_mapping_by_external_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->remove_mapping_by_external_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
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

# **update_mapping**
> Mapping update_mapping(id, update_mapping_request, wink_version=wink_version)

Update Mapping

Update a mapping name only

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.mapping import Mapping
from trip_pay_payment.models.update_mapping_request import UpdateMappingRequest
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
    api_instance = trip_pay_payment.MappingApi(api_client)
    id = 'id_example' # str | 
    update_mapping_request = trip_pay_payment.UpdateMappingRequest() # UpdateMappingRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Mapping
        api_response = api_instance.update_mapping(id, update_mapping_request, wink_version=wink_version)
        print("The response of MappingApi->update_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->update_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_mapping_request** | [**UpdateMappingRequest**](UpdateMappingRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

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

# **update_mapping_by_external_identifier**
> Mapping update_mapping_by_external_identifier(id, update_mapping_request, wink_version=wink_version)

Update External Mapping

Update a mapping name only

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.mapping import Mapping
from trip_pay_payment.models.update_mapping_request import UpdateMappingRequest
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
    api_instance = trip_pay_payment.MappingApi(api_client)
    id = 'id_example' # str | 
    update_mapping_request = trip_pay_payment.UpdateMappingRequest() # UpdateMappingRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update External Mapping
        api_response = api_instance.update_mapping_by_external_identifier(id, update_mapping_request, wink_version=wink_version)
        print("The response of MappingApi->update_mapping_by_external_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->update_mapping_by_external_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_mapping_request** | [**UpdateMappingRequest**](UpdateMappingRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

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

