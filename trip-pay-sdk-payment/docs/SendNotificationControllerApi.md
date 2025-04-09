# trip_pay_payment.SendNotificationControllerApi

All URIs are relative to *https://api.trippay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](SendNotificationControllerApi.md#create_notification) | **POST** /api/administration/notification | 


# **create_notification**
> List[NotificationView] create_notification(send_notification, wink_version=wink_version)

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import trip_pay_payment
from trip_pay_payment.models.notification_view import NotificationView
from trip_pay_payment.models.send_notification import SendNotification
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
    api_instance = trip_pay_payment.SendNotificationControllerApi(api_client)
    send_notification = trip_pay_payment.SendNotification() # SendNotification | 
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        api_response = api_instance.create_notification(send_notification, wink_version=wink_version)
        print("The response of SendNotificationControllerApi->create_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendNotificationControllerApi->create_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification** | [**SendNotification**](SendNotification.md)|  | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**List[NotificationView]**](NotificationView.md)

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

