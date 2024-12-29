# AggregateBookingContractCancellationState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **bool** | Whether booking contract was cancelled | 
**count** | **int** | Aggregate booking contract of the cancellation state | 

## Example

```python
from trip_pay_payment.models.aggregate_booking_contract_cancellation_state import AggregateBookingContractCancellationState

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateBookingContractCancellationState from a JSON string
aggregate_booking_contract_cancellation_state_instance = AggregateBookingContractCancellationState.from_json(json)
# print the JSON string representation of the object
print(AggregateBookingContractCancellationState.to_json())

# convert the object into a dict
aggregate_booking_contract_cancellation_state_dict = aggregate_booking_contract_cancellation_state_instance.to_dict()
# create an instance of AggregateBookingContractCancellationState from a dict
aggregate_booking_contract_cancellation_state_from_dict = AggregateBookingContractCancellationState.from_dict(aggregate_booking_contract_cancellation_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


