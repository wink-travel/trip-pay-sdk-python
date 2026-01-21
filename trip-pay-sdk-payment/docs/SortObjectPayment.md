# SortObjectPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 
**unsorted** | **bool** |  | [optional] 
**sorted** | **bool** |  | [optional] 

## Example

```python
from trip_pay_payment.models.sort_object_payment import SortObjectPayment

# TODO update the JSON string below
json = "{}"
# create an instance of SortObjectPayment from a JSON string
sort_object_payment_instance = SortObjectPayment.from_json(json)
# print the JSON string representation of the object
print(SortObjectPayment.to_json())

# convert the object into a dict
sort_object_payment_dict = sort_object_payment_instance.to_dict()
# create an instance of SortObjectPayment from a dict
sort_object_payment_from_dict = SortObjectPayment.from_dict(sort_object_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


