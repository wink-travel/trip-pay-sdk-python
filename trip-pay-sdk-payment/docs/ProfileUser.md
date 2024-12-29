# ProfileUser

User details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email | [optional] 
**phone** | **str** | Telephone | [optional] 
**profile_picture_url** | **str** | Profile picture URL | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from trip_pay_payment.models.profile_user import ProfileUser

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileUser from a JSON string
profile_user_instance = ProfileUser.from_json(json)
# print the JSON string representation of the object
print(ProfileUser.to_json())

# convert the object into a dict
profile_user_dict = profile_user_instance.to_dict()
# create an instance of ProfileUser from a dict
profile_user_from_dict = ProfileUser.from_dict(profile_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


