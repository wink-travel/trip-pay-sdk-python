# UpsertWebhookManagingEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Managing entity identifier. | 
**name** | **str** | Descriptive name of managing entity. | 

## Example

```python
from trip_pay_payment.models.upsert_webhook_managing_entity_request import UpsertWebhookManagingEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertWebhookManagingEntityRequest from a JSON string
upsert_webhook_managing_entity_request_instance = UpsertWebhookManagingEntityRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertWebhookManagingEntityRequest.to_json())

# convert the object into a dict
upsert_webhook_managing_entity_request_dict = upsert_webhook_managing_entity_request_instance.to_dict()
# create an instance of UpsertWebhookManagingEntityRequest from a dict
upsert_webhook_managing_entity_request_from_dict = UpsertWebhookManagingEntityRequest.from_dict(upsert_webhook_managing_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


