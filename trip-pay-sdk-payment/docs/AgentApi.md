# trip_pay_payment.AgentApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_sale**](AgentApi.md#create_agent_sale) | **POST** /api/contract/agent | Create Agent Payment


# **create_agent_sale**
> MultiBookingContractResponse create_agent_sale(create_agent_sale_request, wink_version=wink_version)

Create Agent Payment

Attempt an immediate payment with Agent as acquirer. Checks for valid funds in account before booking instruction.

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.create_agent_sale_request import CreateAgentSaleRequest
from trip_pay_payment.models.multi_booking_contract_response import MultiBookingContractResponse
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
    api_instance = trip_pay_payment.AgentApi(api_client)
    create_agent_sale_request = trip_pay_payment.CreateAgentSaleRequest() # CreateAgentSaleRequest | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Create Agent Payment
        api_response = api_instance.create_agent_sale(create_agent_sale_request, wink_version=wink_version)
        print("The response of AgentApi->create_agent_sale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_agent_sale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_agent_sale_request** | [**CreateAgentSaleRequest**](CreateAgentSaleRequest.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**MultiBookingContractResponse**](MultiBookingContractResponse.md)

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

