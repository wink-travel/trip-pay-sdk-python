# ManagingEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The value that should be persisted. | 
**name** | **str** | Text representation of the value. | 
**type** | **str** | Type of entity. | 
**metadata** | **Dict[str, object]** | Metadata | [optional] 

## Example

```python
from trip_pay_payment.models.managing_entity import ManagingEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ManagingEntity from a JSON string
managing_entity_instance = ManagingEntity.from_json(json)
# print the JSON string representation of the object
print(ManagingEntity.to_json())

# convert the object into a dict
managing_entity_dict = managing_entity_instance.to_dict()
# create an instance of ManagingEntity from a dict
managing_entity_from_dict = ManagingEntity.from_dict(managing_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


