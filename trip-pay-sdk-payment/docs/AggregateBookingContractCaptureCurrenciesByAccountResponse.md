# AggregateBookingContractCaptureCurrenciesByAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** | Account identifier with these capture currencies | 
**list** | [**List[AvailableFunds]**](AvailableFunds.md) | List of capture currencies | 

## Example

```python
from trip_pay_payment.models.aggregate_booking_contract_capture_currencies_by_account_response import AggregateBookingContractCaptureCurrenciesByAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateBookingContractCaptureCurrenciesByAccountResponse from a JSON string
aggregate_booking_contract_capture_currencies_by_account_response_instance = AggregateBookingContractCaptureCurrenciesByAccountResponse.from_json(json)
# print the JSON string representation of the object
print(AggregateBookingContractCaptureCurrenciesByAccountResponse.to_json())

# convert the object into a dict
aggregate_booking_contract_capture_currencies_by_account_response_dict = aggregate_booking_contract_capture_currencies_by_account_response_instance.to_dict()
# create an instance of AggregateBookingContractCaptureCurrenciesByAccountResponse from a dict
aggregate_booking_contract_capture_currencies_by_account_response_from_dict = AggregateBookingContractCaptureCurrenciesByAccountResponse.from_dict(aggregate_booking_contract_capture_currencies_by_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


