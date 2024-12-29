# PayoutFee

Fees incurred when making the withdrawal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Type of fee | 
**candidate** | **str** | Who pays for this fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from trip_pay_payment.models.payout_fee import PayoutFee

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutFee from a JSON string
payout_fee_instance = PayoutFee.from_json(json)
# print the JSON string representation of the object
print(PayoutFee.to_json())

# convert the object into a dict
payout_fee_dict = payout_fee_instance.to_dict()
# create an instance of PayoutFee from a dict
payout_fee_from_dict = PayoutFee.from_dict(payout_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


