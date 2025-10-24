# PageBookingContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingContract]**](BookingContract.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from trip_pay_payment.models.page_booking_contract import PageBookingContract

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingContract from a JSON string
page_booking_contract_instance = PageBookingContract.from_json(json)
# print the JSON string representation of the object
print(PageBookingContract.to_json())

# convert the object into a dict
page_booking_contract_dict = page_booking_contract_instance.to_dict()
# create an instance of PageBookingContract from a dict
page_booking_contract_from_dict = PageBookingContract.from_dict(page_booking_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


