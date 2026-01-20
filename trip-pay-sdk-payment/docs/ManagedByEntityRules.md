# ManagedByEntityRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **date** | Optional expiration date when agency is no longer managing this entity. | [optional] 
**num_bookings** | **int** | Optional total number of bookings [left] the agency is entitled to commission. This number will decrement every time a booking is made with this agency involved. | [optional] 
**non_expired** | **bool** | Whether managing entity rules has expired. | [optional] [readonly] 

## Example

```python
from trip_pay_payment.models.managed_by_entity_rules import ManagedByEntityRules

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedByEntityRules from a JSON string
managed_by_entity_rules_instance = ManagedByEntityRules.from_json(json)
# print the JSON string representation of the object
print(ManagedByEntityRules.to_json())

# convert the object into a dict
managed_by_entity_rules_dict = managed_by_entity_rules_instance.to_dict()
# create an instance of ManagedByEntityRules from a dict
managed_by_entity_rules_from_dict = ManagedByEntityRules.from_dict(managed_by_entity_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


