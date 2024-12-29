# trip_pay_payment.AccountApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_account_status**](AccountApi.md#check_account_status) | **GET** /api/account/{id}/status | Check Account Status
[**check_external_account_status**](AccountApi.md#check_external_account_status) | **GET** /api/account/external/{id}/status | Check External Account Status
[**create_account**](AccountApi.md#create_account) | **POST** /api/account | Create Account
[**create_account_bank_account**](AccountApi.md#create_account_bank_account) | **POST** /api/account/{id}/bank-account | Add Bank Account
[**create_external_account_bank_account**](AccountApi.md#create_external_account_bank_account) | **POST** /api/account/external/{id}/bank-account | Add Bank Account to External
[**delete_account**](AccountApi.md#delete_account) | **DELETE** /api/account/{id} | Delete Account
[**is_account_name_unique**](AccountApi.md#is_account_name_unique) | **GET** /api/account/unique/{name} | Verify Account Name
[**load_account**](AccountApi.md#load_account) | **GET** /api/account/{id} | Show Account
[**load_account_by_name**](AccountApi.md#load_account_by_name) | **GET** /api/account/name/{name} | Show Accounts by Name
[**load_account_by_name_like**](AccountApi.md#load_account_by_name_like) | **GET** /api/account/name | Show Accounts by Name like
[**load_account_grid_for_authenticated_user**](AccountApi.md#load_account_grid_for_authenticated_user) | **POST** /api/account/grid | Show Account Grid for User
[**load_accounts_for_authenticated_user**](AccountApi.md#load_accounts_for_authenticated_user) | **GET** /api/account/list | Show Account for User
[**load_external_account**](AccountApi.md#load_external_account) | **GET** /api/account/external/{externalAccountIdentifier} | Show Account for External
[**remove_account_bank_account**](AccountApi.md#remove_account_bank_account) | **DELETE** /api/account/{id}/bank-account/{bankAccountId} | Remove Bank Account
[**remove_external_account_bank_account**](AccountApi.md#remove_external_account_bank_account) | **DELETE** /api/account/external/{id}/bank-account/{bankAccountId} | Remove Bank Account for External
[**search_account_by_name**](AccountApi.md#search_account_by_name) | **GET** /api/account/search/{name} | Search Accounts by Name
[**show_accounts_by_owner**](AccountApi.md#show_accounts_by_owner) | **GET** /api/account/owner/list | Show Accounts by Owner
[**update_account**](AccountApi.md#update_account) | **PATCH** /api/account/{id} | Update Account
[**update_external_account**](AccountApi.md#update_external_account) | **PATCH** /api/account/external/{id} | Update External Account
[**update_national_identifier**](AccountApi.md#update_national_identifier) | **PATCH** /api/account/{id}/task/{taskId}/tid | Submit Tax ID
[**upsert_account_bank_account**](AccountApi.md#upsert_account_bank_account) | **PUT** /api/account/{id}/bank-account/{bankAccountId} | Update Bank Account
[**upsert_external_account_bank_account**](AccountApi.md#upsert_external_account_bank_account) | **PUT** /api/account/external/{id}/bank-account/{bankAccountId} | Update Bank Account for External
[**verify_account**](AccountApi.md#verify_account) | **PATCH** /api/account/{id}/verify | Verify Account


# **check_account_status**
> AccountStatusResponse check_account_status(id, wink_version=wink_version, accept=accept)

Check Account Status

Returns account status about whether this account has been verified and whether it is active.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account_status_response import AccountStatusResponse
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Check Account Status
        api_response = api_instance.check_account_status(id, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->check_account_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->check_account_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AccountStatusResponse**](AccountStatusResponse.md)

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

# **check_external_account_status**
> AccountStatusResponse check_external_account_status(id, wink_version=wink_version, accept=accept)

Check External Account Status

Returns account status about whether this account has been verified and whether it is active.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account_status_response import AccountStatusResponse
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Check External Account Status
        api_response = api_instance.check_external_account_status(id, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->check_external_account_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->check_external_account_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AccountStatusResponse**](AccountStatusResponse.md)

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

# **create_account**
> Account create_account(create_account_request, wink_version=wink_version)

Create Account

Create a new account

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.create_account_request import CreateAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    create_account_request = trip_pay_payment.CreateAccountRequest() # CreateAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Account
        api_response = api_instance.create_account(create_account_request, wink_version=wink_version)
        print("The response of AccountApi->create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_request** | [**CreateAccountRequest**](CreateAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **create_account_bank_account**
> Account create_account_bank_account(id, upsert_bank_account_request, wink_version=wink_version)

Add Bank Account

Add a bank account to an existing account using local account identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.upsert_bank_account_request import UpsertBankAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    upsert_bank_account_request = trip_pay_payment.UpsertBankAccountRequest() # UpsertBankAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add Bank Account
        api_response = api_instance.create_account_bank_account(id, upsert_bank_account_request, wink_version=wink_version)
        print("The response of AccountApi->create_account_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->create_account_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_bank_account_request** | [**UpsertBankAccountRequest**](UpsertBankAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **create_external_account_bank_account**
> Account create_external_account_bank_account(id, upsert_bank_account_request, wink_version=wink_version)

Add Bank Account to External

Add a bank account to an existing account using the external account identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.upsert_bank_account_request import UpsertBankAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    upsert_bank_account_request = trip_pay_payment.UpsertBankAccountRequest() # UpsertBankAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Add Bank Account to External
        api_response = api_instance.create_external_account_bank_account(id, upsert_bank_account_request, wink_version=wink_version)
        print("The response of AccountApi->create_external_account_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->create_external_account_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_bank_account_request** | [**UpsertBankAccountRequest**](UpsertBankAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **delete_account**
> RemoveEntryResponse delete_account(id, wink_version=wink_version, accept=accept)

Delete Account

Show a specific account

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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Delete Account
        api_response = api_instance.delete_account(id, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
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

# **is_account_name_unique**
> UniqueResult is_account_name_unique(name, identifier=identifier, wink_version=wink_version, accept=accept)

Verify Account Name

Check if account name is unique

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.unique_result import UniqueResult
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    name = 'name_example' # str | 
    identifier = 'identifier_example' # str |  (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Verify Account Name
        api_response = api_instance.is_account_name_unique(name, identifier=identifier, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->is_account_name_unique:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->is_account_name_unique: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **identifier** | **str**|  | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**UniqueResult**](UniqueResult.md)

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

# **load_account**
> Account load_account(id, wink_version=wink_version, accept=accept)

Show Account

Show a specific account

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Account
        api_response = api_instance.load_account(id, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->load_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->load_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **load_account_by_name**
> List[Account] load_account_by_name(name, wink_version=wink_version, accept=accept)

Show Accounts by Name

Show accounts matching name

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    name = 'name_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Accounts by Name
        api_response = api_instance.load_account_by_name(name, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->load_account_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->load_account_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **load_account_by_name_like**
> List[Account] load_account_by_name_like(name, ignore_case=ignore_case, wink_version=wink_version, accept=accept)

Show Accounts by Name like

Show accounts matching name that are like...

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    name = 'name_example' # str | 
    ignore_case = True # bool |  (optional) (default to True)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Accounts by Name like
        api_response = api_instance.load_account_by_name_like(name, ignore_case=ignore_case, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->load_account_by_name_like:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->load_account_by_name_like: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **ignore_case** | **bool**|  | [optional] [default to True]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **load_account_grid_for_authenticated_user**
> PageAccount load_account_grid_for_authenticated_user(state, wink_version=wink_version)

Show Account Grid for User

Load account grid for authenticated user

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.page_account import PageAccount
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    state = trip_pay_payment.State() # State | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Show Account Grid for User
        api_response = api_instance.load_account_grid_for_authenticated_user(state, wink_version=wink_version)
        print("The response of AccountApi->load_account_grid_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->load_account_grid_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**State**](State.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PageAccount**](PageAccount.md)

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

# **load_accounts_for_authenticated_user**
> List[Account] load_accounts_for_authenticated_user(wink_version=wink_version, accept=accept)

Show Account for User

Load account details for authenticated user

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Account for User
        api_response = api_instance.load_accounts_for_authenticated_user(wink_version=wink_version, accept=accept)
        print("The response of AccountApi->load_accounts_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->load_accounts_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **load_external_account**
> Account load_external_account(external_account_identifier, wink_version=wink_version, accept=accept)

Show Account for External

Show a specific account by passing your own external identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    external_account_identifier = 'external_account_identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Account for External
        api_response = api_instance.load_external_account(external_account_identifier, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->load_external_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->load_external_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **remove_account_bank_account**
> Account remove_account_bank_account(id, bank_account_id, wink_version=wink_version, accept=accept)

Remove Bank Account

Remove an existing bank account for an existing account using local account identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Bank Account
        api_response = api_instance.remove_account_bank_account(id, bank_account_id, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->remove_account_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->remove_account_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bank_account_id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **remove_external_account_bank_account**
> Account remove_external_account_bank_account(id, bank_account_id, wink_version=wink_version, accept=accept)

Remove Bank Account for External

Remove an existing bank account for an account using the external account identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Bank Account for External
        api_response = api_instance.remove_external_account_bank_account(id, bank_account_id, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->remove_external_account_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->remove_external_account_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bank_account_id** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **search_account_by_name**
> List[KeyValuePair] search_account_by_name(name, ignorecase=ignorecase, wink_version=wink_version, accept=accept)

Search Accounts by Name

Show accounts matching name

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.key_value_pair import KeyValuePair
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    name = 'name_example' # str | 
    ignorecase = False # bool |  (optional) (default to False)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Search Accounts by Name
        api_response = api_instance.search_account_by_name(name, ignorecase=ignorecase, wink_version=wink_version, accept=accept)
        print("The response of AccountApi->search_account_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->search_account_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **ignorecase** | **bool**|  | [optional] [default to False]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[KeyValuePair]**](KeyValuePair.md)

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

# **show_accounts_by_owner**
> List[Account] show_accounts_by_owner(wink_version=wink_version, accept=accept)

Show Accounts by Owner

List all accounts owned by creating entity

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Accounts by Owner
        api_response = api_instance.show_accounts_by_owner(wink_version=wink_version, accept=accept)
        print("The response of AccountApi->show_accounts_by_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->show_accounts_by_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[Account]**](Account.md)

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

# **update_account**
> Account update_account(id, upsert_account_request, wink_version=wink_version)

Update Account

Update an existing account

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.upsert_account_request import UpsertAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    upsert_account_request = trip_pay_payment.UpsertAccountRequest() # UpsertAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Account
        api_response = api_instance.update_account(id, upsert_account_request, wink_version=wink_version)
        print("The response of AccountApi->update_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_account_request** | [**UpsertAccountRequest**](UpsertAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **update_external_account**
> Account update_external_account(id, upsert_account_request, wink_version=wink_version)

Update External Account

Update an existing account using the externalIdentifier to find the account

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.upsert_account_request import UpsertAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    upsert_account_request = trip_pay_payment.UpsertAccountRequest() # UpsertAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update External Account
        api_response = api_instance.update_external_account(id, upsert_account_request, wink_version=wink_version)
        print("The response of AccountApi->update_external_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->update_external_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upsert_account_request** | [**UpsertAccountRequest**](UpsertAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **update_national_identifier**
> Account update_national_identifier(id, task_id, set_tax_identifier_request, wink_version=wink_version)

Submit Tax ID

Accounts can respond to an invalid Tax ID error by completing this task

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.set_tax_identifier_request import SetTaxIdentifierRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    task_id = 'task_id_example' # str | 
    set_tax_identifier_request = trip_pay_payment.SetTaxIdentifierRequest() # SetTaxIdentifierRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Submit Tax ID
        api_response = api_instance.update_national_identifier(id, task_id, set_tax_identifier_request, wink_version=wink_version)
        print("The response of AccountApi->update_national_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->update_national_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **task_id** | **str**|  | 
 **set_tax_identifier_request** | [**SetTaxIdentifierRequest**](SetTaxIdentifierRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **upsert_account_bank_account**
> Account upsert_account_bank_account(id, bank_account_id, upsert_bank_account_request, wink_version=wink_version)

Update Bank Account

Update an existing bank account for an existing account using local account identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.upsert_bank_account_request import UpsertBankAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    upsert_bank_account_request = trip_pay_payment.UpsertBankAccountRequest() # UpsertBankAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Bank Account
        api_response = api_instance.upsert_account_bank_account(id, bank_account_id, upsert_bank_account_request, wink_version=wink_version)
        print("The response of AccountApi->upsert_account_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->upsert_account_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bank_account_id** | **str**|  | 
 **upsert_bank_account_request** | [**UpsertBankAccountRequest**](UpsertBankAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **upsert_external_account_bank_account**
> Account upsert_external_account_bank_account(id, bank_account_id, upsert_bank_account_request, wink_version=wink_version)

Update Bank Account for External

Update an existing bank account for an account using the external account identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.upsert_bank_account_request import UpsertBankAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    upsert_bank_account_request = trip_pay_payment.UpsertBankAccountRequest() # UpsertBankAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Update Bank Account for External
        api_response = api_instance.upsert_external_account_bank_account(id, bank_account_id, upsert_bank_account_request, wink_version=wink_version)
        print("The response of AccountApi->upsert_external_account_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->upsert_external_account_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bank_account_id** | **str**|  | 
 **upsert_bank_account_request** | [**UpsertBankAccountRequest**](UpsertBankAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

# **verify_account**
> Account verify_account(id, verify_account_request, wink_version=wink_version)

Verify Account

Enriches account with supplemental data that missing in the account creation phase.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.account import Account
from trip_pay_payment.models.verify_account_request import VerifyAccountRequest
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
    api_instance = trip_pay_payment.AccountApi(api_client)
    id = 'id_example' # str | 
    verify_account_request = trip_pay_payment.VerifyAccountRequest() # VerifyAccountRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Verify Account
        api_response = api_instance.verify_account(id, verify_account_request, wink_version=wink_version)
        print("The response of AccountApi->verify_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->verify_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **verify_account_request** | [**VerifyAccountRequest**](VerifyAccountRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

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

