# trip_pay_payment.ManagingEntityApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_name**](ManagingEntityApi.md#change_name) | **PATCH** /api/my-account/change-name | Change Name
[**is_managing_entity_name_unique**](ManagingEntityApi.md#is_managing_entity_name_unique) | **POST** /api/managing-entity-name-check | Verify Managing Entity Name
[**is_name_unique**](ManagingEntityApi.md#is_name_unique) | **GET** /api/managing-entity/name | Name Check
[**is_url_name_unique**](ManagingEntityApi.md#is_url_name_unique) | **POST** /api/managing-entity-url-name-check | Verify Managing Entity Url Name
[**remove_managing_entity**](ManagingEntityApi.md#remove_managing_entity) | **DELETE** /api/managing-entity/{managingEntityIdentifier} | Delete Managing Entity
[**remove_my_account**](ManagingEntityApi.md#remove_my_account) | **DELETE** /api/my-account | Delete My Account
[**show_accessible_managing_entities**](ManagingEntityApi.md#show_accessible_managing_entities) | **GET** /api/managing-entity/list | List Managing Entities
[**show_accessible_managing_entities_by_state**](ManagingEntityApi.md#show_accessible_managing_entities_by_state) | **POST** /api/managing-entity/grid | Search Managing Entities
[**show_managing_entities**](ManagingEntityApi.md#show_managing_entities) | **GET** /api/managing-entity/list/all | Show All Managing Entities
[**show_managing_entity**](ManagingEntityApi.md#show_managing_entity) | **GET** /api/managing-entity/{managingEntityIdentifier} | Show Managing Entity
[**show_my_account**](ManagingEntityApi.md#show_my_account) | **GET** /api/my-account | Show My Account
[**show_sales_channels**](ManagingEntityApi.md#show_sales_channels) | **GET** /api/sales-channel/search | Search Sales Channel by Name
[**update_managing_entity_account_representative**](ManagingEntityApi.md#update_managing_entity_account_representative) | **PATCH** /api/my-account/account-representative | Update Account Representative
[**update_my_account_address**](ManagingEntityApi.md#update_my_account_address) | **PATCH** /api/my-account/address | Update Address
[**update_my_account_logo**](ManagingEntityApi.md#update_my_account_logo) | **PATCH** /api/my-account/logo | Update Logo
[**update_profile**](ManagingEntityApi.md#update_profile) | **PATCH** /api/managing-entity/{managingEntityIdentifier}/profile | Update Profile
[**update_profile_picture**](ManagingEntityApi.md#update_profile_picture) | **PATCH** /api/my-account/profile-picture | Update Profile Picture


# **change_name**
> ManagingEntityAuthenticatedEntity change_name(change_managing_entity_name_request_authenticated_entity, wink_version=wink_version)

Change Name

Gives owners a way to change the name of their account.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.change_managing_entity_name_request_authenticated_entity import ChangeManagingEntityNameRequestAuthenticatedEntity
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
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
    change_managing_entity_name_request_authenticated_entity = trip_pay_payment.ChangeManagingEntityNameRequestAuthenticatedEntity() # ChangeManagingEntityNameRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Change Name
        api_response = api_instance.change_name(change_managing_entity_name_request_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->change_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->change_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_managing_entity_name_request_authenticated_entity** | [**ChangeManagingEntityNameRequestAuthenticatedEntity**](ChangeManagingEntityNameRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **is_managing_entity_name_unique**
> UniqueResultAuthenticatedEntity is_managing_entity_name_unique(unique_request_authenticated_entity, wink_version=wink_version)

Verify Managing Entity Name

Check if managing entity name is unique

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.unique_request_authenticated_entity import UniqueRequestAuthenticatedEntity
from trip_pay_payment.models.unique_result_authenticated_entity import UniqueResultAuthenticatedEntity
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
    unique_request_authenticated_entity = trip_pay_payment.UniqueRequestAuthenticatedEntity() # UniqueRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Verify Managing Entity Name
        api_response = api_instance.is_managing_entity_name_unique(unique_request_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->is_managing_entity_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->is_managing_entity_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_request_authenticated_entity** | [**UniqueRequestAuthenticatedEntity**](UniqueRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**UniqueResultAuthenticatedEntity**](UniqueResultAuthenticatedEntity.md)

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

# **is_name_unique**
> UniqueResultPayment is_name_unique(name, geo_name_id=geo_name_id, managing_entity_identifier=managing_entity_identifier, wink_version=wink_version, accept=accept)

Name Check

Verifies that the name is unique.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.unique_result_payment import UniqueResultPayment
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
    name = 'Blue Orchid' # str | Search for uniqueness for this hotel name.
    geo_name_id = '12345678' # str | Search for uniqueness in relationship to a city. (optional)
    managing_entity_identifier = 'hotel-123' # str | Optional, existing hotel identifier (optional)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Name Check
        api_response = api_instance.is_name_unique(name, geo_name_id=geo_name_id, managing_entity_identifier=managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->is_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->is_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search for uniqueness for this hotel name. | 
 **geo_name_id** | **str**| Search for uniqueness in relationship to a city. | [optional] 
 **managing_entity_identifier** | **str**| Optional, existing hotel identifier | [optional] 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**UniqueResultPayment**](UniqueResultPayment.md)

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

# **is_url_name_unique**
> UniqueResultAuthenticatedEntity is_url_name_unique(unique_request_authenticated_entity, wink_version=wink_version)

Verify Managing Entity Url Name

Check if affiliate url name is unique

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.unique_request_authenticated_entity import UniqueRequestAuthenticatedEntity
from trip_pay_payment.models.unique_result_authenticated_entity import UniqueResultAuthenticatedEntity
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
    unique_request_authenticated_entity = trip_pay_payment.UniqueRequestAuthenticatedEntity() # UniqueRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Verify Managing Entity Url Name
        api_response = api_instance.is_url_name_unique(unique_request_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->is_url_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->is_url_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_request_authenticated_entity** | [**UniqueRequestAuthenticatedEntity**](UniqueRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**UniqueResultAuthenticatedEntity**](UniqueResultAuthenticatedEntity.md)

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

# **remove_managing_entity**
> ManagingEntityAuthenticatedEntity remove_managing_entity(managing_entity_identifier, wink_version=wink_version, accept=accept)

Delete Managing Entity

Delete a managing entity by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
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
    managing_entity_identifier = 'managing_entity_identifier_example' # str | Delete managing entity with given identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Managing Entity
        api_response = api_instance.remove_managing_entity(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->remove_managing_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->remove_managing_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Delete managing entity with given identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **remove_my_account**
> ManagingEntityAuthenticatedEntity remove_my_account(wink_version=wink_version, accept=accept)

Delete My Account

Delete a managing entity by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
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
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete My Account
        api_response = api_instance.remove_my_account(wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->remove_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->remove_my_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **show_accessible_managing_entities**
> List[ManagingEntityAuthenticatedEntity] show_accessible_managing_entities(type=type, wink_version=wink_version, accept=accept)

List Managing Entities

List all companies owned by caller.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
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
    type = 'type_example' # str | Filter on managing entities of a specific type (optional)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # List Managing Entities
        api_response = api_instance.show_accessible_managing_entities(type=type, wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->show_accessible_managing_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_accessible_managing_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter on managing entities of a specific type | [optional] 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[ManagingEntityAuthenticatedEntity]**](ManagingEntityAuthenticatedEntity.md)

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

# **show_accessible_managing_entities_by_state**
> PageManagingEntityPayment show_accessible_managing_entities_by_state(state_payment, wink_version=wink_version)

Search Managing Entities

Retrieve a paginated list of entities that you manage.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.page_managing_entity_payment import PageManagingEntityPayment
from trip_pay_payment.models.state_payment import StatePayment
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
    state_payment = trip_pay_payment.StatePayment() # StatePayment | Filter grid by state request body
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Search Managing Entities
        api_response = api_instance.show_accessible_managing_entities_by_state(state_payment, wink_version=wink_version)
        print("The response of ManagingEntityApi->show_accessible_managing_entities_by_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_accessible_managing_entities_by_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_payment** | [**StatePayment**](StatePayment.md)| Filter grid by state request body | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**PageManagingEntityPayment**](PageManagingEntityPayment.md)

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

# **show_managing_entities**
> List[ManagingEntityAuthenticatedEntity] show_managing_entities(wink_version=wink_version, accept=accept)

Show All Managing Entities

Lists all entities user is associated with. Includes all entities the user is associated with.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
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
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show All Managing Entities
        api_response = api_instance.show_managing_entities(wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->show_managing_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_managing_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[ManagingEntityAuthenticatedEntity]**](ManagingEntityAuthenticatedEntity.md)

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

# **show_managing_entity**
> ManagingEntityAuthenticatedEntity show_managing_entity(managing_entity_identifier, wink_version=wink_version, accept=accept)

Show Managing Entity

Retrieve managing entity by identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
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
    managing_entity_identifier = 'managing_entity_identifier_example' # str | Select managing entity with given identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Managing Entity
        api_response = api_instance.show_managing_entity(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->show_managing_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_managing_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Select managing entity with given identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **show_my_account**
> ManagingEntityAuthenticatedEntity show_my_account(wink_version=wink_version, accept=accept)

Show My Account

Retrieve my own account on Wink

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
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
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show My Account
        api_response = api_instance.show_my_account(wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->show_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_my_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **show_sales_channels**
> List[KeyValuePairAuthenticatedEntity] show_sales_channels(name, wink_version=wink_version, accept=accept)

Search Sales Channel by Name

Search for sales channels by name

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.key_value_pair_authenticated_entity import KeyValuePairAuthenticatedEntity
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
    name = 'name_example' # str | Search for sales channel with name
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Search Sales Channel by Name
        api_response = api_instance.show_sales_channels(name, wink_version=wink_version, accept=accept)
        print("The response of ManagingEntityApi->show_sales_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->show_sales_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search for sales channel with name | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePairAuthenticatedEntity]**](KeyValuePairAuthenticatedEntity.md)

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

# **update_managing_entity_account_representative**
> ManagingEntityAuthenticatedEntity update_managing_entity_account_representative(update_account_representative_request_authenticated_entity, wink_version=wink_version)

Update Account Representative

Updates managing entity account representative.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
from trip_pay_payment.models.update_account_representative_request_authenticated_entity import UpdateAccountRepresentativeRequestAuthenticatedEntity
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
    update_account_representative_request_authenticated_entity = trip_pay_payment.UpdateAccountRepresentativeRequestAuthenticatedEntity() # UpdateAccountRepresentativeRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Account Representative
        api_response = api_instance.update_managing_entity_account_representative(update_account_representative_request_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->update_managing_entity_account_representative:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->update_managing_entity_account_representative: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_account_representative_request_authenticated_entity** | [**UpdateAccountRepresentativeRequestAuthenticatedEntity**](UpdateAccountRepresentativeRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **update_my_account_address**
> ManagingEntityAuthenticatedEntity update_my_account_address(simple_address_authenticated_entity, wink_version=wink_version)

Update Address

Updates managing entity address.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
from trip_pay_payment.models.simple_address_authenticated_entity import SimpleAddressAuthenticatedEntity
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
    simple_address_authenticated_entity = trip_pay_payment.SimpleAddressAuthenticatedEntity() # SimpleAddressAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Address
        api_response = api_instance.update_my_account_address(simple_address_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->update_my_account_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->update_my_account_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simple_address_authenticated_entity** | [**SimpleAddressAuthenticatedEntity**](SimpleAddressAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **update_my_account_logo**
> ManagingEntityAuthenticatedEntity update_my_account_logo(upsert_image_request_authenticated_entity, wink_version=wink_version)

Update Logo

Updates managing entity logo.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
from trip_pay_payment.models.upsert_image_request_authenticated_entity import UpsertImageRequestAuthenticatedEntity
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
    upsert_image_request_authenticated_entity = trip_pay_payment.UpsertImageRequestAuthenticatedEntity() # UpsertImageRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Logo
        api_response = api_instance.update_my_account_logo(upsert_image_request_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->update_my_account_logo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->update_my_account_logo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_image_request_authenticated_entity** | [**UpsertImageRequestAuthenticatedEntity**](UpsertImageRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **update_profile**
> ManagingEntityAuthenticatedEntity update_profile(managing_entity_identifier, update_managing_entity_information_request_authenticated_entity, wink_version=wink_version)

Update Profile

Update managing entity profile.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
from trip_pay_payment.models.update_managing_entity_information_request_authenticated_entity import UpdateManagingEntityInformationRequestAuthenticatedEntity
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
    managing_entity_identifier = 'managing_entity_identifier_example' # str | Update managing entity with given identifier
    update_managing_entity_information_request_authenticated_entity = trip_pay_payment.UpdateManagingEntityInformationRequestAuthenticatedEntity() # UpdateManagingEntityInformationRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Profile
        api_response = api_instance.update_profile(managing_entity_identifier, update_managing_entity_information_request_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Update managing entity with given identifier | 
 **update_managing_entity_information_request_authenticated_entity** | [**UpdateManagingEntityInformationRequestAuthenticatedEntity**](UpdateManagingEntityInformationRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

# **update_profile_picture**
> ManagingEntityAuthenticatedEntity update_profile_picture(upsert_image_request_authenticated_entity, wink_version=wink_version)

Update Profile Picture

Updates managing entity profile picture.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity
from trip_pay_payment.models.upsert_image_request_authenticated_entity import UpsertImageRequestAuthenticatedEntity
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
    upsert_image_request_authenticated_entity = trip_pay_payment.UpsertImageRequestAuthenticatedEntity() # UpsertImageRequestAuthenticatedEntity | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Update Profile Picture
        api_response = api_instance.update_profile_picture(upsert_image_request_authenticated_entity, wink_version=wink_version)
        print("The response of ManagingEntityApi->update_profile_picture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagingEntityApi->update_profile_picture: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_image_request_authenticated_entity** | [**UpsertImageRequestAuthenticatedEntity**](UpsertImageRequestAuthenticatedEntity.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAuthenticatedEntity**](ManagingEntityAuthenticatedEntity.md)

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

