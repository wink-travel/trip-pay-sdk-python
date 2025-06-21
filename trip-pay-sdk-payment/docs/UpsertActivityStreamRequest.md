# UpsertActivityStreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **str** | Who can track this stream? | 
**entity_identifier** | **str** | ID of tracked entity | 
**event_date** | **datetime** | Optional way to indicate when event occurred | [optional] 
**emotion** | **str** | Optional emotion. The actual implementation of the emotion is down to the consumer of the stream. | [optional] 
**comment** | **str** | Optional comment. For when the activity was created manually by a user. If i18nKey is not populated, comment is required. | [optional] 
**i18n_key** | **str** | Optional localized key. Key will be used to generate text on the front-end. If comment is not populated, i18n is required. | 
**attachment_id** | **str** | Optional attachment. For when we allow users to upload documents to the activity via Cloudinary. | [optional] 
**user** | [**ActivityStreamUser**](ActivityStreamUser.md) | Optional user. Attached when an authenticated user is available in the context of the activity. | [optional] 

## Example

```python
from trip_pay_payment.models.upsert_activity_stream_request import UpsertActivityStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertActivityStreamRequest from a JSON string
upsert_activity_stream_request_instance = UpsertActivityStreamRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertActivityStreamRequest.to_json())

# convert the object into a dict
upsert_activity_stream_request_dict = upsert_activity_stream_request_instance.to_dict()
# create an instance of UpsertActivityStreamRequest from a dict
upsert_activity_stream_request_from_dict = UpsertActivityStreamRequest.from_dict(upsert_activity_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


