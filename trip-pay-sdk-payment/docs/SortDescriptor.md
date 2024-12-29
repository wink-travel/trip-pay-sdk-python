# SortDescriptor

Descriptors used for sorting result set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from trip_pay_payment.models.sort_descriptor import SortDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptor from a JSON string
sort_descriptor_instance = SortDescriptor.from_json(json)
# print the JSON string representation of the object
print(SortDescriptor.to_json())

# convert the object into a dict
sort_descriptor_dict = sort_descriptor_instance.to_dict()
# create an instance of SortDescriptor from a dict
sort_descriptor_from_dict = SortDescriptor.from_dict(sort_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


