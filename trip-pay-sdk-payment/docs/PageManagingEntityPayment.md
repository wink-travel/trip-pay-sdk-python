# PageManagingEntityPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ManagingEntityPayment]**](ManagingEntityPayment.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectPayment**](PageableObjectPayment.md) |  | [optional] 
**sort** | [**SortObjectPayment**](SortObjectPayment.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from trip_pay_payment.models.page_managing_entity_payment import PageManagingEntityPayment

# TODO update the JSON string below
json = "{}"
# create an instance of PageManagingEntityPayment from a JSON string
page_managing_entity_payment_instance = PageManagingEntityPayment.from_json(json)
# print the JSON string representation of the object
print(PageManagingEntityPayment.to_json())

# convert the object into a dict
page_managing_entity_payment_dict = page_managing_entity_payment_instance.to_dict()
# create an instance of PageManagingEntityPayment from a dict
page_managing_entity_payment_from_dict = PageManagingEntityPayment.from_dict(page_managing_entity_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


