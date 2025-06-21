# GuestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**profile** | [**ProfileLightweight**](ProfileLightweight.md) | Optional profile record | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from trip_pay_payment.models.guest_user import GuestUser

# TODO update the JSON string below
json = "{}"
# create an instance of GuestUser from a JSON string
guest_user_instance = GuestUser.from_json(json)
# print the JSON string representation of the object
print(GuestUser.to_json())

# convert the object into a dict
guest_user_dict = guest_user_instance.to_dict()
# create an instance of GuestUser from a dict
guest_user_from_dict = GuestUser.from_dict(guest_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


