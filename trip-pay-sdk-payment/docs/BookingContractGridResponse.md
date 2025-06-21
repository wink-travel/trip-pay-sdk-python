# BookingContractGridResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PageBookingContract**](PageBookingContract.md) | Page of booking contracts | 
**total_funds** | [**TotalAggregateFunds**](TotalAggregateFunds.md) | Aggregate funds for all booking contracts | 

## Example

```python
from trip_pay_payment.models.booking_contract_grid_response import BookingContractGridResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BookingContractGridResponse from a JSON string
booking_contract_grid_response_instance = BookingContractGridResponse.from_json(json)
# print the JSON string representation of the object
print(BookingContractGridResponse.to_json())

# convert the object into a dict
booking_contract_grid_response_dict = booking_contract_grid_response_instance.to_dict()
# create an instance of BookingContractGridResponse from a dict
booking_contract_grid_response_from_dict = BookingContractGridResponse.from_dict(booking_contract_grid_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


