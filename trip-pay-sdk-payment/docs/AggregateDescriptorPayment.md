# AggregateDescriptorPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to run aggregate function on | [optional] 
**aggregate** | **str** | Aggregate function | [optional] 

## Example

```python
from trip_pay_payment.models.aggregate_descriptor_payment import AggregateDescriptorPayment

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateDescriptorPayment from a JSON string
aggregate_descriptor_payment_instance = AggregateDescriptorPayment.from_json(json)
# print the JSON string representation of the object
print(AggregateDescriptorPayment.to_json())

# convert the object into a dict
aggregate_descriptor_payment_dict = aggregate_descriptor_payment_instance.to_dict()
# create an instance of AggregateDescriptorPayment from a dict
aggregate_descriptor_payment_from_dict = AggregateDescriptorPayment.from_dict(aggregate_descriptor_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


