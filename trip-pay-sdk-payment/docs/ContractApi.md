# trip_pay_payment.ContractApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_booking_contract**](ContractApi.md#cancel_booking_contract) | **PATCH** /api/contract/{identifier}/cancel | Cancel booking
[**cancel_group_booking_contract**](ContractApi.md#cancel_group_booking_contract) | **PATCH** /api/contract/list/{traceId}/cancel | Cancel group bookings
[**create_payable_contracts**](ContractApi.md#create_payable_contracts) | **POST** /api/contract/payable | Create payable contracts
[**immediate_group_refund**](ContractApi.md#immediate_group_refund) | **PATCH** /api/contract/list/{traceId}/immediate-refund | Immediate group refund
[**immediate_refund**](ContractApi.md#immediate_refund) | **PATCH** /api/contract/{identifier}/immediate-refund | Immediate refund
[**is_contract_cancellable**](ContractApi.md#is_contract_cancellable) | **POST** /api/contract/{identifier}/cancellable | Contract cancellable
[**is_group_contract_cancellable**](ContractApi.md#is_group_contract_cancellable) | **POST** /api/contract/list/{traceId}/cancellable | Group contract cancellable
[**request_refund**](ContractApi.md#request_refund) | **PATCH** /api/contract/{identifier}/request-refund | Request refund
[**show_aggregate_booking_contract_data**](ContractApi.md#show_aggregate_booking_contract_data) | **GET** /api/account/{accountIdentifier}/contract/aggregate/beneficiary | Retrieve aggregate beneficiary data
[**show_aggregate_cancellation_data**](ContractApi.md#show_aggregate_cancellation_data) | **GET** /api/account/{accountIdentifier}/contract/aggregate/cancellation | Retrieve aggregate cancellation data
[**show_capture_currencies**](ContractApi.md#show_capture_currencies) | **GET** /api/account/{accountIdentifier}/contract/capture | Retrieve capture currencies
[**show_contract**](ContractApi.md#show_contract) | **GET** /api/contract/{identifier} | Retrieve single contract
[**show_contract_for_external_account**](ContractApi.md#show_contract_for_external_account) | **GET** /api/account/external/{externalAccountIdentifier}/contract/{bookingContractIdentifier} | Retrieve single contract for external account
[**show_contract_funds**](ContractApi.md#show_contract_funds) | **GET** /api/account/{accountIdentifier}/contract/funds | Retrieve contract funds
[**show_contract_grid**](ContractApi.md#show_contract_grid) | **POST** /api/account/{accountIdentifier}/contract/grid | Retrieve contract grid
[**show_contracts**](ContractApi.md#show_contracts) | **GET** /api/contract/list/{traceId} | Retrieve multiple contracts
[**show_external_contract**](ContractApi.md#show_external_contract) | **GET** /api/account/external/{externalAccountIdentifier}/contract/external/{externalBookingContractIdentifier} | Retrieve single contract for external
[**show_payable_contracts**](ContractApi.md#show_payable_contracts) | **GET** /api/contract/payable/{transientContractIdentifier} | Load payable contracts


# **cancel_booking_contract**
> BookingContract cancel_booking_contract(identifier, cancel_booking_contract_request, wink_version=wink_version)

Cancel booking

Cancels a booking contract. Based on the type of cancellation policy, will do a refund or partial refund to the payment method.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract import BookingContract
from trip_pay_payment.models.cancel_booking_contract_request import CancelBookingContractRequest
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    identifier = 'identifier_example' # str | Booking contract identifier
    cancel_booking_contract_request = trip_pay_payment.CancelBookingContractRequest() # CancelBookingContractRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Cancel booking
        api_response = api_instance.cancel_booking_contract(identifier, cancel_booking_contract_request, wink_version=wink_version)
        print("The response of ContractApi->cancel_booking_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->cancel_booking_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Booking contract identifier | 
 **cancel_booking_contract_request** | [**CancelBookingContractRequest**](CancelBookingContractRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingContract**](BookingContract.md)

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

# **cancel_group_booking_contract**
> List[BookingContract] cancel_group_booking_contract(trace_id, cancel_booking_contract_request, wink_version=wink_version)

Cancel group bookings

Cancels a group booking contract. All bookings under the same traceId.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract import BookingContract
from trip_pay_payment.models.cancel_booking_contract_request import CancelBookingContractRequest
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    trace_id = 'trace_id_example' # str | Booking contract traceId
    cancel_booking_contract_request = trip_pay_payment.CancelBookingContractRequest() # CancelBookingContractRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Cancel group bookings
        api_response = api_instance.cancel_group_booking_contract(trace_id, cancel_booking_contract_request, wink_version=wink_version)
        print("The response of ContractApi->cancel_group_booking_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->cancel_group_booking_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| Booking contract traceId | 
 **cancel_booking_contract_request** | [**CancelBookingContractRequest**](CancelBookingContractRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[BookingContract]**](BookingContract.md)

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

# **create_payable_contracts**
> List[PayableContractResponse] create_payable_contracts(payable_contract_request, wink_version=wink_version)

Create payable contracts

Returns a list of contracts that can be used alongside payment widget to initiate a payment.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.payable_contract_request import PayableContractRequest
from trip_pay_payment.models.payable_contract_response import PayableContractResponse
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    payable_contract_request = trip_pay_payment.PayableContractRequest() # PayableContractRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create payable contracts
        api_response = api_instance.create_payable_contracts(payable_contract_request, wink_version=wink_version)
        print("The response of ContractApi->create_payable_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->create_payable_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payable_contract_request** | [**PayableContractRequest**](PayableContractRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[PayableContractResponse]**](PayableContractResponse.md)

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

# **immediate_group_refund**
> List[BookingContract] immediate_group_refund(trace_id, immediate_refund_request, wink_version=wink_version)

Immediate group refund

In the event that a booking is not possible on the partner site due to lack of availability, or similar. This endpoint offers a 3-minute window to let that partner refund the traveler 100% of her funds.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract import BookingContract
from trip_pay_payment.models.immediate_refund_request import ImmediateRefundRequest
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    trace_id = 'trace_id_example' # str | Booking contract traceId
    immediate_refund_request = trip_pay_payment.ImmediateRefundRequest() # ImmediateRefundRequest | Accompanying payload that described the optional reason for using this endpoint.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Immediate group refund
        api_response = api_instance.immediate_group_refund(trace_id, immediate_refund_request, wink_version=wink_version)
        print("The response of ContractApi->immediate_group_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->immediate_group_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| Booking contract traceId | 
 **immediate_refund_request** | [**ImmediateRefundRequest**](ImmediateRefundRequest.md)| Accompanying payload that described the optional reason for using this endpoint. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[BookingContract]**](BookingContract.md)

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

# **immediate_refund**
> BookingContract immediate_refund(identifier, immediate_refund_request, wink_version=wink_version)

Immediate refund

In the event that a booking is not possible on the partner site due to lack of availability, or similar. This endpoint offers a 3-minute window to let that partner refund the traveler 100% of her funds.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract import BookingContract
from trip_pay_payment.models.immediate_refund_request import ImmediateRefundRequest
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    identifier = 'identifier_example' # str | Booking contract identifier
    immediate_refund_request = trip_pay_payment.ImmediateRefundRequest() # ImmediateRefundRequest | Accompanying payload that described the optional reason for using this endpoint.
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Immediate refund
        api_response = api_instance.immediate_refund(identifier, immediate_refund_request, wink_version=wink_version)
        print("The response of ContractApi->immediate_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->immediate_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Booking contract identifier | 
 **immediate_refund_request** | [**ImmediateRefundRequest**](ImmediateRefundRequest.md)| Accompanying payload that described the optional reason for using this endpoint. | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingContract**](BookingContract.md)

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

# **is_contract_cancellable**
> BookingContractCancellableResponse is_contract_cancellable(identifier, cancel_booking_contract_request, wink_version=wink_version)

Contract cancellable

Returns whether a booking can be cancelled or not and any rules associated with cancelling.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract_cancellable_response import BookingContractCancellableResponse
from trip_pay_payment.models.cancel_booking_contract_request import CancelBookingContractRequest
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    identifier = 'identifier_example' # str | Booking contract identifier
    cancel_booking_contract_request = trip_pay_payment.CancelBookingContractRequest() # CancelBookingContractRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Contract cancellable
        api_response = api_instance.is_contract_cancellable(identifier, cancel_booking_contract_request, wink_version=wink_version)
        print("The response of ContractApi->is_contract_cancellable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->is_contract_cancellable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Booking contract identifier | 
 **cancel_booking_contract_request** | [**CancelBookingContractRequest**](CancelBookingContractRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingContractCancellableResponse**](BookingContractCancellableResponse.md)

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

# **is_group_contract_cancellable**
> List[BookingContractCancellableResponse] is_group_contract_cancellable(trace_id, cancel_booking_contract_request, wink_version=wink_version, accept=accept)

Group contract cancellable

Returns whether a booking can be cancelled or not and any rules associated with cancelling.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract_cancellable_response import BookingContractCancellableResponse
from trip_pay_payment.models.cancel_booking_contract_request import CancelBookingContractRequest
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    trace_id = 'trace_id_example' # str | Booking contract traceId
    cancel_booking_contract_request = trip_pay_payment.CancelBookingContractRequest() # CancelBookingContractRequest | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Group contract cancellable
        api_response = api_instance.is_group_contract_cancellable(trace_id, cancel_booking_contract_request, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->is_group_contract_cancellable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->is_group_contract_cancellable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| Booking contract traceId | 
 **cancel_booking_contract_request** | [**CancelBookingContractRequest**](CancelBookingContractRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BookingContractCancellableResponse]**](BookingContractCancellableResponse.md)

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

# **request_refund**
> BookingContract request_refund(identifier, refund_request, wink_version=wink_version)

Request refund

Requests a refund for a booking contract. Creates a refund request record that needs to be approved by a payment admin.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract import BookingContract
from trip_pay_payment.models.refund_request import RefundRequest
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    identifier = 'identifier_example' # str | Booking contract identifier
    refund_request = trip_pay_payment.RefundRequest() # RefundRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Request refund
        api_response = api_instance.request_refund(identifier, refund_request, wink_version=wink_version)
        print("The response of ContractApi->request_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->request_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Booking contract identifier | 
 **refund_request** | [**RefundRequest**](RefundRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingContract**](BookingContract.md)

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

# **show_aggregate_booking_contract_data**
> List[BeneficiaryAggregateData] show_aggregate_booking_contract_data(account_identifier, type=type, wink_version=wink_version, accept=accept)

Retrieve aggregate beneficiary data

Returns aggregate contract data this account identifier has participated in.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.beneficiary_aggregate_data import BeneficiaryAggregateData
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    type = 'type_example' # str |  (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve aggregate beneficiary data
        api_response = api_instance.show_aggregate_booking_contract_data(account_identifier, type=type, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_aggregate_booking_contract_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_aggregate_booking_contract_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **type** | **str**|  | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BeneficiaryAggregateData]**](BeneficiaryAggregateData.md)

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

# **show_aggregate_cancellation_data**
> List[AggregateBookingContractCancellationState] show_aggregate_cancellation_data(account_identifier, wink_version=wink_version, accept=accept)

Retrieve aggregate cancellation data

Returns aggregate cancellation data this account identifier has participated in.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.aggregate_booking_contract_cancellation_state import AggregateBookingContractCancellationState
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve aggregate cancellation data
        api_response = api_instance.show_aggregate_cancellation_data(account_identifier, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_aggregate_cancellation_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_aggregate_cancellation_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[AggregateBookingContractCancellationState]**](AggregateBookingContractCancellationState.md)

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

# **show_capture_currencies**
> AggregateBookingContractCaptureCurrenciesByAccountResponse show_capture_currencies(account_identifier, state=state, wink_version=wink_version, accept=accept)

Retrieve capture currencies

Returns a list of capture currencies and amounts for the account identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.aggregate_booking_contract_capture_currencies_by_account_response import AggregateBookingContractCaptureCurrenciesByAccountResponse
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    account_identifier = 'account_identifier_example' # str | 
    state = 'state_example' # str |  (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve capture currencies
        api_response = api_instance.show_capture_currencies(account_identifier, state=state, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_capture_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_capture_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**|  | 
 **state** | **str**|  | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**AggregateBookingContractCaptureCurrenciesByAccountResponse**](AggregateBookingContractCaptureCurrenciesByAccountResponse.md)

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

# **show_contract**
> BookingContract show_contract(identifier, wink_version=wink_version, accept=accept)

Retrieve single contract

Returns a booking contract by its unique identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract import BookingContract
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    identifier = 'identifier_example' # str | Booking contract identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve single contract
        api_response = api_instance.show_contract(identifier, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Booking contract identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**BookingContract**](BookingContract.md)

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

# **show_contract_for_external_account**
> ExternalBookingContract show_contract_for_external_account(external_account_identifier, booking_contract_identifier, wink_version=wink_version, accept=accept)

Retrieve single contract for external account

Loads a booking contract based on external account identifier and actual contract identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.external_booking_contract import ExternalBookingContract
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    external_account_identifier = 'external_account_identifier_example' # str | Show contract owned by this external account
    booking_contract_identifier = 'booking_contract_identifier_example' # str | Booking contract identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve single contract for external account
        api_response = api_instance.show_contract_for_external_account(external_account_identifier, booking_contract_identifier, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_contract_for_external_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_contract_for_external_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_identifier** | **str**| Show contract owned by this external account | 
 **booking_contract_identifier** | **str**| Booking contract identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ExternalBookingContract**](ExternalBookingContract.md)

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

# **show_contract_funds**
> TotalAggregateFunds show_contract_funds(account_identifier, state=state, account_funds_only=account_funds_only, wink_version=wink_version, accept=accept)

Retrieve contract funds

Returns booking contract funds for account identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.total_aggregate_funds import TotalAggregateFunds
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    account_identifier = 'account_identifier_example' # str | The account owner
    state = 'state_example' # str | The optional state to want to receive funds for (optional)
    account_funds_only = False # bool | Whether to only returns funds for that account identifier or total funds that account identifier was part of. (defaults to false). (optional) (default to False)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve contract funds
        api_response = api_instance.show_contract_funds(account_identifier, state=state, account_funds_only=account_funds_only, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_contract_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_contract_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| The account owner | 
 **state** | **str**| The optional state to want to receive funds for | [optional] 
 **account_funds_only** | **bool**| Whether to only returns funds for that account identifier or total funds that account identifier was part of. (defaults to false). | [optional] [default to False]
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**TotalAggregateFunds**](TotalAggregateFunds.md)

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

# **show_contract_grid**
> BookingContractGridResponse show_contract_grid(account_identifier, state2, state=state, account_funds_only=account_funds_only, wink_version=wink_version)

Retrieve contract grid

Returns booking contracts for account identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract_grid_response import BookingContractGridResponse
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    account_identifier = 'account_identifier_example' # str | The account owner
    state2 = trip_pay_payment.State() # State | The optional state to filter on
    state = 'state_example' # str | The optional state to want to receive funds for (optional)
    account_funds_only = False # bool | Whether to only returns funds for that account identifier or total funds that account identifier was part of. (defaults to false). (optional) (default to False)
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Retrieve contract grid
        api_response = api_instance.show_contract_grid(account_identifier, state2, state=state, account_funds_only=account_funds_only, wink_version=wink_version)
        print("The response of ContractApi->show_contract_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_contract_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| The account owner | 
 **state2** | [**State**](State.md)| The optional state to filter on | 
 **state** | **str**| The optional state to want to receive funds for | [optional] 
 **account_funds_only** | **bool**| Whether to only returns funds for that account identifier or total funds that account identifier was part of. (defaults to false). | [optional] [default to False]
 **wink_version** | **str**|  | [optional] 

### Return type

[**BookingContractGridResponse**](BookingContractGridResponse.md)

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

# **show_contracts**
> List[BookingContract] show_contracts(trace_id, wink_version=wink_version, accept=accept)

Retrieve multiple contracts

Returns booking contracts matching traceId.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.booking_contract import BookingContract
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    trace_id = 'trace_id_example' # str | Trace identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve multiple contracts
        api_response = api_instance.show_contracts(trace_id, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| Trace identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**List[BookingContract]**](BookingContract.md)

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

# **show_external_contract**
> ExternalBookingContract show_external_contract(external_account_identifier, external_booking_contract_identifier, wink_version=wink_version, accept=accept)

Retrieve single contract for external

Loads a booking contract based on external account and contract identifiers.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.external_booking_contract import ExternalBookingContract
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    external_account_identifier = 'external_account_identifier_example' # str | Show contract owned by this external account
    external_booking_contract_identifier = 'external_booking_contract_identifier_example' # str | External booking contract identifier
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Retrieve single contract for external
        api_response = api_instance.show_external_contract(external_account_identifier, external_booking_contract_identifier, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_external_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_external_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_identifier** | **str**| Show contract owned by this external account | 
 **external_booking_contract_identifier** | **str**| External booking contract identifier | 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**ExternalBookingContract**](ExternalBookingContract.md)

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

# **show_payable_contracts**
> PayableContract show_payable_contracts(transient_contract_identifier, currency=currency, wink_version=wink_version, accept=accept)

Load payable contracts

Returns a transient contract based on specified identifier.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.payable_contract import PayableContract
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
    api_instance = trip_pay_payment.ContractApi(api_client)
    transient_contract_identifier = 'contract-1' # str | Transient contract to retrieve
    currency = 'contract-1' # str | Desired currency (optional)
    wink_version = 'wink_version_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Load payable contracts
        api_response = api_instance.show_payable_contracts(transient_contract_identifier, currency=currency, wink_version=wink_version, accept=accept)
        print("The response of ContractApi->show_payable_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->show_payable_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transient_contract_identifier** | **str**| Transient contract to retrieve | 
 **currency** | **str**| Desired currency | [optional] 
 **wink_version** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**PayableContract**](PayableContract.md)

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

