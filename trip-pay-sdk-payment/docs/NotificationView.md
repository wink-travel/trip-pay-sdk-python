# NotificationView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**notification** | [**Notification**](Notification.md) |  | 

## Example

```python
from trip_pay_payment.models.notification_view import NotificationView

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationView from a JSON string
notification_view_instance = NotificationView.from_json(json)
# print the JSON string representation of the object
print(NotificationView.to_json())

# convert the object into a dict
notification_view_dict = notification_view_instance.to_dict()
# create an instance of NotificationView from a dict
notification_view_from_dict = NotificationView.from_dict(notification_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


