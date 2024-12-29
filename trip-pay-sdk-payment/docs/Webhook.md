# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **str** | Unique owner record identifier | 
**owner_identifier** | **str** | Unique owner record identifier | 
**owner_name** | **str** | Name of company owner. | 
**owner_type** | **str** | Type of entity. | 
**name** | **str** | Descriptive name of webhook. | 
**enabled** | **bool** | Whether this webhook is enabled. | [default to True]
**event_url** | **str** | The url to POST event to. | 
**event_list** | **List[str]** |  | 

## Example

```python
from trip_pay_payment.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


