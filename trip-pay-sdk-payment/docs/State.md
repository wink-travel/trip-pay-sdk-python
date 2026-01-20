# State


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
from trip_pay_payment.models.state import State

# TODO update the JSON string below
json = "{}"
# create an instance of State from a JSON string
state_instance = State.from_json(json)
# print the JSON string representation of the object
print(State.to_json())

# convert the object into a dict
state_dict = state_instance.to_dict()
# create an instance of State from a dict
state_from_dict = State.from_dict(state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


