# GroupDescriptor

Descriptors to group result sets by.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptor]**](AggregateDescriptor.md) | Primitive aggregate data points | [optional] 

## Example

```python
from trip_pay_payment.models.group_descriptor import GroupDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptor from a JSON string
group_descriptor_instance = GroupDescriptor.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptor.to_json())

# convert the object into a dict
group_descriptor_dict = group_descriptor_instance.to_dict()
# create an instance of GroupDescriptor from a dict
group_descriptor_from_dict = GroupDescriptor.from_dict(group_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


