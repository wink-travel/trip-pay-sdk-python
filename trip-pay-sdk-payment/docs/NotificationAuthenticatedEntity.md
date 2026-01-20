# NotificationAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **UUID** | Owner identifier | 
**managing_entity_identifier** | **UUID** | ManagingEntity identifier | [optional] 
**name** | **str** | Owner name | [optional] 
**priority** | **str** | Importance of message | 
**type** | **str** | Message type | 
**recipient_type** | **str** | Recipient type | 
**message_template_id** | **str** | Message template | 
**subject** | **str** | Subject of message | 
**body** | **str** | Subject of message | 
**cta_url** | **str** | Path to feature | [optional] 
**read** | **bool** | AffiliateAccount read announcement | [optional] 
**marked_as_removed** | **bool** | Message marked as removed | [optional] 
**notify_via_email** | **bool** | Also send email announcement | [optional] 

## Example

```python
from trip_pay_payment.models.notification_authenticated_entity import NotificationAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationAuthenticatedEntity from a JSON string
notification_authenticated_entity_instance = NotificationAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(NotificationAuthenticatedEntity.to_json())

# convert the object into a dict
notification_authenticated_entity_dict = notification_authenticated_entity_instance.to_dict()
# create an instance of NotificationAuthenticatedEntity from a dict
notification_authenticated_entity_from_dict = NotificationAuthenticatedEntity.from_dict(notification_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


