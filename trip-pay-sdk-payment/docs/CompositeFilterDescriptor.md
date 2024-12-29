# CompositeFilterDescriptor

Descriptors used for filtering result set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptor]**](FilterDescriptor.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from trip_pay_payment.models.composite_filter_descriptor import CompositeFilterDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptor from a JSON string
composite_filter_descriptor_instance = CompositeFilterDescriptor.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptor.to_json())

# convert the object into a dict
composite_filter_descriptor_dict = composite_filter_descriptor_instance.to_dict()
# create an instance of CompositeFilterDescriptor from a dict
composite_filter_descriptor_from_dict = CompositeFilterDescriptor.from_dict(composite_filter_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


