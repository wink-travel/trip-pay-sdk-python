# ActivityStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**acl** | **str** | Who can track this stream? | 
**entity_identifier** | **str** | ID of tracked entity | 
**emotion** | **str** | Optional emotion. The actual implementation of the emotion is down to the consumer of the stream. | [optional] 
**comment** | **str** | Optional comment. For when the activity was created manually by a user. If i18nKey is not populated, comment is required. | [optional] 
**i18n_key** | **str** | Localized key. Key will be used to generate text on the front-end. If comment is not populated, i18n is required. | 
**attachment_id** | **str** | Optional attachment. For when we allow users to upload documents to the activity via Cloudinary. | [optional] 
**user** | [**ActivityStreamUser**](ActivityStreamUser.md) | Optional user. Attached when an authenticated user is available in the context of the activity. | [optional] 

## Example

```python
from trip_pay_payment.models.activity_stream import ActivityStream

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStream from a JSON string
activity_stream_instance = ActivityStream.from_json(json)
# print the JSON string representation of the object
print(ActivityStream.to_json())

# convert the object into a dict
activity_stream_dict = activity_stream_instance.to_dict()
# create an instance of ActivityStream from a dict
activity_stream_from_dict = ActivityStream.from_dict(activity_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


