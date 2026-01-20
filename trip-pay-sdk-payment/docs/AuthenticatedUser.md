# AuthenticatedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **UUID** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from trip_pay_payment.models.authenticated_user import AuthenticatedUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedUser from a JSON string
authenticated_user_instance = AuthenticatedUser.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedUser.to_json())

# convert the object into a dict
authenticated_user_dict = authenticated_user_instance.to_dict()
# create an instance of AuthenticatedUser from a dict
authenticated_user_from_dict = AuthenticatedUser.from_dict(authenticated_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


