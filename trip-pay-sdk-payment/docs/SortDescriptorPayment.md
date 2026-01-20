# SortDescriptorPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from trip_pay_payment.models.sort_descriptor_payment import SortDescriptorPayment

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptorPayment from a JSON string
sort_descriptor_payment_instance = SortDescriptorPayment.from_json(json)
# print the JSON string representation of the object
print(SortDescriptorPayment.to_json())

# convert the object into a dict
sort_descriptor_payment_dict = sort_descriptor_payment_instance.to_dict()
# create an instance of SortDescriptorPayment from a dict
sort_descriptor_payment_from_dict = SortDescriptorPayment.from_dict(sort_descriptor_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


