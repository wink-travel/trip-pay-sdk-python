# ManagingEntityManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email | 
**status** | **str** | Contact phone number | [optional] 
**user_identifier** | **UUID** | User identifier | [optional] 
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**secondary_email** | **str** | Contact secondary Email | [optional] 
**phone_number** | **str** | Contact phone number | [optional] 
**profile_picture** | [**SimpleMultimedia**](SimpleMultimedia.md) | Profile picture is available | [optional] 
**owner** | **bool** | Account owner | [optional] 
**roles** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from trip_pay_payment.models.managing_entity_manager import ManagingEntityManager

# TODO update the JSON string below
json = "{}"
# create an instance of ManagingEntityManager from a JSON string
managing_entity_manager_instance = ManagingEntityManager.from_json(json)
# print the JSON string representation of the object
print(ManagingEntityManager.to_json())

# convert the object into a dict
managing_entity_manager_dict = managing_entity_manager_instance.to_dict()
# create an instance of ManagingEntityManager from a dict
managing_entity_manager_from_dict = ManagingEntityManager.from_dict(managing_entity_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


