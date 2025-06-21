# ActivityStreamUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User ID of authenticated person that created the stream. | 
**name** | **str** | Full name of user. | 
**profile_picture_url** | **str** | Optional url of user&#39;s profile picture | [optional] 

## Example

```python
from trip_pay_payment.models.activity_stream_user import ActivityStreamUser

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStreamUser from a JSON string
activity_stream_user_instance = ActivityStreamUser.from_json(json)
# print the JSON string representation of the object
print(ActivityStreamUser.to_json())

# convert the object into a dict
activity_stream_user_dict = activity_stream_user_instance.to_dict()
# create an instance of ActivityStreamUser from a dict
activity_stream_user_from_dict = ActivityStreamUser.from_dict(activity_stream_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


