# StatePayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of records to be skipped by the pager. | [optional] [default to 0]
**take** | **int** | Number of records to take. | [optional] [default to 30]
**sort** | [**List[SortDescriptorPayment]**](SortDescriptorPayment.md) | Descriptors used for sorting result set. | [optional] 
**filter** | [**CompositeFilterDescriptorPayment**](CompositeFilterDescriptorPayment.md) | Descriptors used for filtering result set | [optional] 
**group** | [**List[GroupDescriptorPayment]**](GroupDescriptorPayment.md) | Descriptors to group result sets by. | [optional] 

## Example

```python
from trip_pay_payment.models.state_payment import StatePayment

# TODO update the JSON string below
json = "{}"
# create an instance of StatePayment from a JSON string
state_payment_instance = StatePayment.from_json(json)
# print the JSON string representation of the object
print(StatePayment.to_json())

# convert the object into a dict
state_payment_dict = state_payment_instance.to_dict()
# create an instance of StatePayment from a dict
state_payment_from_dict = StatePayment.from_dict(state_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


