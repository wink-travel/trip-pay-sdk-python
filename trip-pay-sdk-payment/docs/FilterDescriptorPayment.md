# FilterDescriptorPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | **str** | Filter operator to use on field | 
**value** | **object** |  | 
**ignore_case** | **bool** | Make filter comparison case insensitive. Default: Case sensitive  | [optional] 

## Example

```python
from trip_pay_payment.models.filter_descriptor_payment import FilterDescriptorPayment

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDescriptorPayment from a JSON string
filter_descriptor_payment_instance = FilterDescriptorPayment.from_json(json)
# print the JSON string representation of the object
print(FilterDescriptorPayment.to_json())

# convert the object into a dict
filter_descriptor_payment_dict = filter_descriptor_payment_instance.to_dict()
# create an instance of FilterDescriptorPayment from a dict
filter_descriptor_payment_from_dict = FilterDescriptorPayment.from_dict(filter_descriptor_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


