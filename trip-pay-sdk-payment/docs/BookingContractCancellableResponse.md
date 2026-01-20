# BookingContractCancellableResponse

Contract cancellable response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Booking contract identifier | [optional] 
**cancellable** | **bool** | Whether the booking is cancellable or not | [optional] 
**list** | [**List[BookingContractItemCancellableResponse]**](BookingContractItemCancellableResponse.md) |  | [optional] 

## Example

```python
from trip_pay_payment.models.booking_contract_cancellable_response import BookingContractCancellableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BookingContractCancellableResponse from a JSON string
booking_contract_cancellable_response_instance = BookingContractCancellableResponse.from_json(json)
# print the JSON string representation of the object
print(BookingContractCancellableResponse.to_json())

# convert the object into a dict
booking_contract_cancellable_response_dict = booking_contract_cancellable_response_instance.to_dict()
# create an instance of BookingContractCancellableResponse from a dict
booking_contract_cancellable_response_from_dict = BookingContractCancellableResponse.from_dict(booking_contract_cancellable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


