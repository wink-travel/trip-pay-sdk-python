# MultiBookingContractResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[BookingContract]**](BookingContract.md) | Finalized booking contract | 

## Example

```python
from trip_pay_payment.models.multi_booking_contract_response import MultiBookingContractResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultiBookingContractResponse from a JSON string
multi_booking_contract_response_instance = MultiBookingContractResponse.from_json(json)
# print the JSON string representation of the object
print(MultiBookingContractResponse.to_json())

# convert the object into a dict
multi_booking_contract_response_dict = multi_booking_contract_response_instance.to_dict()
# create an instance of MultiBookingContractResponse from a dict
multi_booking_contract_response_from_dict = MultiBookingContractResponse.from_dict(multi_booking_contract_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


