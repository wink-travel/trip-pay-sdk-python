# trip_pay_payment.AccountManagerApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_manager_invite**](AccountManagerApi.md#accept_manager_invite) | **GET** /api/manager/invite/{managingEntityIdentifier}/accept | Accept Invite
[**invite_manager**](AccountManagerApi.md#invite_manager) | **PATCH** /api/manager/invite | Invite Manager
[**reject_invite**](AccountManagerApi.md#reject_invite) | **DELETE** /api/manager/invite/{managingEntityIdentifier}/reject | Reject Invite
[**remove_company_user**](AccountManagerApi.md#remove_company_user) | **DELETE** /api/manager/{email} | Remove Manager
[**remove_manager_agency**](AccountManagerApi.md#remove_manager_agency) | **DELETE** /api/manager/agency | Remove Managing Agency
[**show_manager_invite_list**](AccountManagerApi.md#show_manager_invite_list) | **GET** /api/manager/invite/list | Show Invites
[**update_manager_agency**](AccountManagerApi.md#update_manager_agency) | **PATCH** /api/manager/agency | Set Managing Agency


# **accept_manager_invite**
> ManagingEntitySupplier accept_manager_invite(managing_entity_identifier, wink_version=wink_version, accept=accept)

Accept Invite

Accepts the invite to manager a property or account.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_supplier import ManagingEntitySupplier
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
    api_instance = trip_pay_payment.AccountManagerApi(api_client)
    managing_entity_identifier = 'hotel-1' # str | ManagingEntity identifier for which to accept invite to
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Accept Invite
        api_response = api_instance.accept_manager_invite(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->accept_manager_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->accept_manager_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| ManagingEntity identifier for which to accept invite to | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntitySupplier**](ManagingEntitySupplier.md)

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

# **invite_manager**
> ManagingEntityAffiliate invite_manager(invite_manager_request_affiliate, wink_version=wink_version)

Invite Manager

Invite user to be a manager for this managing entity.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.invite_manager_request_affiliate import InviteManagerRequestAffiliate
from trip_pay_payment.models.managing_entity_affiliate import ManagingEntityAffiliate
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
    api_instance = trip_pay_payment.AccountManagerApi(api_client)
    invite_manager_request_affiliate = trip_pay_payment.InviteManagerRequestAffiliate() # InviteManagerRequestAffiliate | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Invite Manager
        api_response = api_instance.invite_manager(invite_manager_request_affiliate, wink_version=wink_version)
        print("The response of AccountManagerApi->invite_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->invite_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_manager_request_affiliate** | [**InviteManagerRequestAffiliate**](InviteManagerRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAffiliate**](ManagingEntityAffiliate.md)

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

# **reject_invite**
> ManagingEntitySupplier reject_invite(managing_entity_identifier, wink_version=wink_version, accept=accept)

Reject Invite

Remove manager by specified identifier

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_supplier import ManagingEntitySupplier
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
    api_instance = trip_pay_payment.AccountManagerApi(api_client)
    managing_entity_identifier = 'hotel-1' # str | Remove manager from this property identifier
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Reject Invite
        api_response = api_instance.reject_invite(managing_entity_identifier, wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->reject_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->reject_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managing_entity_identifier** | **str**| Remove manager from this property identifier | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntitySupplier**](ManagingEntitySupplier.md)

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

# **remove_company_user**
> ManagingEntityAffiliate remove_company_user(email, wink_version=wink_version, accept=accept)

Remove Manager

Disassociate user from this managing entity.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_affiliate import ManagingEntityAffiliate
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
    api_instance = trip_pay_payment.AccountManagerApi(api_client)
    email = 'email_example' # str | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Manager
        api_response = api_instance.remove_company_user(email, wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->remove_company_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->remove_company_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntityAffiliate**](ManagingEntityAffiliate.md)

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

# **remove_manager_agency**
> ManagingEntityAffiliate remove_manager_agency(wink_version=wink_version, accept=accept)

Remove Managing Agency

Unset managing agency.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_affiliate import ManagingEntityAffiliate
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
    api_instance = trip_pay_payment.AccountManagerApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Remove Managing Agency
        api_response = api_instance.remove_manager_agency(wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->remove_manager_agency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->remove_manager_agency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**ManagingEntityAffiliate**](ManagingEntityAffiliate.md)

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

# **show_manager_invite_list**
> List[ManagerInviteAffiliate] show_manager_invite_list(wink_version=wink_version, accept=accept)

Show Invites

Retrieve list of invites for user

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.manager_invite_affiliate import ManagerInviteAffiliate
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
    api_instance = trip_pay_payment.AccountManagerApi(api_client)
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)
    accept = 'accept_example' # str |  (optional)

    try:
        # Show Invites
        api_response = api_instance.show_manager_invite_list(wink_version=wink_version, accept=accept)
        print("The response of AccountManagerApi->show_manager_invite_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->show_manager_invite_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wink_version** | **str**|  | [optional] [default to 2.0.0]
 **accept** | **str**|  | [optional] 

### Return type

[**List[ManagerInviteAffiliate]**](ManagerInviteAffiliate.md)

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

# **update_manager_agency**
> ManagingEntityAffiliate update_manager_agency(update_managed_by_agency_request_affiliate, wink_version=wink_version)

Set Managing Agency

Indicates that the entity is managed by an another entity on the platform. This does not give privileges to manage the account but entitles the agency to a commission.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.managing_entity_affiliate import ManagingEntityAffiliate
from trip_pay_payment.models.update_managed_by_agency_request_affiliate import UpdateManagedByAgencyRequestAffiliate
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
    api_instance = trip_pay_payment.AccountManagerApi(api_client)
    update_managed_by_agency_request_affiliate = trip_pay_payment.UpdateManagedByAgencyRequestAffiliate() # UpdateManagedByAgencyRequestAffiliate | 
    wink_version = 2.0.0 # str |  (optional) (default to 2.0.0)

    try:
        # Set Managing Agency
        api_response = api_instance.update_manager_agency(update_managed_by_agency_request_affiliate, wink_version=wink_version)
        print("The response of AccountManagerApi->update_manager_agency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagerApi->update_manager_agency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_managed_by_agency_request_affiliate** | [**UpdateManagedByAgencyRequestAffiliate**](UpdateManagedByAgencyRequestAffiliate.md)|  | 
 **wink_version** | **str**|  | [optional] [default to 2.0.0]

### Return type

[**ManagingEntityAffiliate**](ManagingEntityAffiliate.md)

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

