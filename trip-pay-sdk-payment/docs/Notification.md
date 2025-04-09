# Notification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Notification identifier | 
**owner_identifier** | **str** | Owner identifier | 
**priority** | **str** | Importance of message | 
**type** | **str** | Message type | 
**recipient_type** | **str** | Recipient type | 
**application** | **str** | Application domain | 
**message_template_id** | **str** | Message template | 
**subject** | **str** | Subject of message | 
**body** | **str** | Subject of message | 
**cta_url** | **str** | Path to feature | 
**read** | **bool** | Company read announcement | [optional] 
**marked_as_removed** | **bool** | Message marked as removed | [optional] 
**notify_via_email** | **bool** | Also send email announcement | [optional] 

## Example

```python
from trip_pay_payment.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


