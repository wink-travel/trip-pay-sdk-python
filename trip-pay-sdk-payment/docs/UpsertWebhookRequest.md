# UpsertWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name of webhook. | 
**entity** | [**ManagingEntity**](ManagingEntity.md) | Name of the application. | 
**enabled** | **bool** | Whether this webhook is enabled. | [default to True]
**event_url** | **str** | The url to POST event to. | 
**event_list** | **List[object]** |  | 

## Example

```python
from trip_pay_payment.models.upsert_webhook_request import UpsertWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertWebhookRequest from a JSON string
upsert_webhook_request_instance = UpsertWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertWebhookRequest.to_json())

# convert the object into a dict
upsert_webhook_request_dict = upsert_webhook_request_instance.to_dict()
# create an instance of UpsertWebhookRequest from a dict
upsert_webhook_request_from_dict = UpsertWebhookRequest.from_dict(upsert_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


