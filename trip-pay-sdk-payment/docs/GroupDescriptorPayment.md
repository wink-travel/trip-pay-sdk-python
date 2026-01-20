# GroupDescriptorPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptorPayment]**](AggregateDescriptorPayment.md) | Primitive aggregate data points | [optional] 

## Example

```python
from trip_pay_payment.models.group_descriptor_payment import GroupDescriptorPayment

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptorPayment from a JSON string
group_descriptor_payment_instance = GroupDescriptorPayment.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptorPayment.to_json())

# convert the object into a dict
group_descriptor_payment_dict = group_descriptor_payment_instance.to_dict()
# create an instance of GroupDescriptorPayment from a dict
group_descriptor_payment_from_dict = GroupDescriptorPayment.from_dict(group_descriptor_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


