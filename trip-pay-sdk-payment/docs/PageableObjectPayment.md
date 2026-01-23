# PageableObjectPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**paged** | **bool** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**unpaged** | **bool** |  | [optional] 
**sort** | [**SortObjectPayment**](SortObjectPayment.md) |  | [optional] 

## Example

```python
from trip_pay_payment.models.pageable_object_payment import PageableObjectPayment

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectPayment from a JSON string
pageable_object_payment_instance = PageableObjectPayment.from_json(json)
# print the JSON string representation of the object
print(PageableObjectPayment.to_json())

# convert the object into a dict
pageable_object_payment_dict = pageable_object_payment_instance.to_dict()
# create an instance of PageableObjectPayment from a dict
pageable_object_payment_from_dict = PageableObjectPayment.from_dict(pageable_object_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


