# CompositeFilterDescriptorPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptorPayment]**](FilterDescriptorPayment.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from trip_pay_payment.models.composite_filter_descriptor_payment import CompositeFilterDescriptorPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptorPayment from a JSON string
composite_filter_descriptor_payment_instance = CompositeFilterDescriptorPayment.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptorPayment.to_json())

# convert the object into a dict
composite_filter_descriptor_payment_dict = composite_filter_descriptor_payment_instance.to_dict()
# create an instance of CompositeFilterDescriptorPayment from a dict
composite_filter_descriptor_payment_from_dict = CompositeFilterDescriptorPayment.from_dict(composite_filter_descriptor_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


