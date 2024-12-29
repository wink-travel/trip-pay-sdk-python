# CancelBookingContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canceller_type** | **str** | Who is doing the cancellation | 
**type** | **str** | Type of cancellation | 
**reason** | **str** | Reason for cancellation | 

## Example

```python
from trip_pay_payment.models.cancel_booking_contract_request import CancelBookingContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelBookingContractRequest from a JSON string
cancel_booking_contract_request_instance = CancelBookingContractRequest.from_json(json)
# print the JSON string representation of the object
print(CancelBookingContractRequest.to_json())

# convert the object into a dict
cancel_booking_contract_request_dict = cancel_booking_contract_request_instance.to_dict()
# create an instance of CancelBookingContractRequest from a dict
cancel_booking_contract_request_from_dict = CancelBookingContractRequest.from_dict(cancel_booking_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


