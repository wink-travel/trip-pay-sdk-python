# KeyValuePairAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value that should be persisted. | 
**label** | **str** | English readable text of the value. | 

## Example

```python
from trip_pay_payment.models.key_value_pair_authenticated_entity import KeyValuePairAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairAuthenticatedEntity from a JSON string
key_value_pair_authenticated_entity_instance = KeyValuePairAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairAuthenticatedEntity.to_json())

# convert the object into a dict
key_value_pair_authenticated_entity_dict = key_value_pair_authenticated_entity_instance.to_dict()
# create an instance of KeyValuePairAuthenticatedEntity from a dict
key_value_pair_authenticated_entity_from_dict = KeyValuePairAuthenticatedEntity.from_dict(key_value_pair_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


