# ExternalBookingContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**Mapping**](Mapping.md) |  | 
**booking_contract** | [**BookingContract**](BookingContract.md) |  | 

## Example

```python
from trip_pay_payment.models.external_booking_contract import ExternalBookingContract

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalBookingContract from a JSON string
external_booking_contract_instance = ExternalBookingContract.from_json(json)
# print the JSON string representation of the object
print(ExternalBookingContract.to_json())

# convert the object into a dict
external_booking_contract_dict = external_booking_contract_instance.to_dict()
# create an instance of ExternalBookingContract from a dict
external_booking_contract_from_dict = ExternalBookingContract.from_dict(external_booking_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


