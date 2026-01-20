# ManagedByEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Entity identifier | 
**name** | **str** | Name of entity | 
**commission_in_percent** | **float** | Agency commission | 
**rules** | [**ManagedByEntityRules**](ManagedByEntityRules.md) | Optional rules for expiration date etc when agency is no longer managing this entity. | [optional] 
**valid** | **bool** | Whether managing entity is eligible a commission. | [optional] [readonly] 

## Example

```python
from trip_pay_payment.models.managed_by_entity import ManagedByEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedByEntity from a JSON string
managed_by_entity_instance = ManagedByEntity.from_json(json)
# print the JSON string representation of the object
print(ManagedByEntity.to_json())

# convert the object into a dict
managed_by_entity_dict = managed_by_entity_instance.to_dict()
# create an instance of ManagedByEntity from a dict
managed_by_entity_from_dict = ManagedByEntity.from_dict(managed_by_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


