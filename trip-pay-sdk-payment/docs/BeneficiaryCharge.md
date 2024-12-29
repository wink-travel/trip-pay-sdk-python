# BeneficiaryCharge

A variable charge can be a fixed amount or a percentage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of charge | 
**percent** | **float** | A percentage of the total stay amount for an early checkin or late checkout | [optional] 

## Example

```python
from trip_pay_payment.models.beneficiary_charge import BeneficiaryCharge

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryCharge from a JSON string
beneficiary_charge_instance = BeneficiaryCharge.from_json(json)
# print the JSON string representation of the object
print(BeneficiaryCharge.to_json())

# convert the object into a dict
beneficiary_charge_dict = beneficiary_charge_instance.to_dict()
# create an instance of BeneficiaryCharge from a dict
beneficiary_charge_from_dict = BeneficiaryCharge.from_dict(beneficiary_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


