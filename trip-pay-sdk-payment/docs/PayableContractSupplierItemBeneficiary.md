# PayableContractSupplierItemBeneficiary

PayableContractSupplierItemBeneficiary is a registered account with rights to compensation within a booking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | identifier of beneficiary that can map to an account with us | 
**identifier_type** | **str** | The identifierType tells us what type of identifier this is | 
**amount_due** | [**BeneficiaryCharge**](BeneficiaryCharge.md) |  | 
**type** | **str** | The type of beneficiary payment. | 
**metadata** | **Dict[str, str]** | Place to add more data related to the booking contract. | [optional] 

## Example

```python
from trip_pay_payment.models.payable_contract_supplier_item_beneficiary import PayableContractSupplierItemBeneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of PayableContractSupplierItemBeneficiary from a JSON string
payable_contract_supplier_item_beneficiary_instance = PayableContractSupplierItemBeneficiary.from_json(json)
# print the JSON string representation of the object
print(PayableContractSupplierItemBeneficiary.to_json())

# convert the object into a dict
payable_contract_supplier_item_beneficiary_dict = payable_contract_supplier_item_beneficiary_instance.to_dict()
# create an instance of PayableContractSupplierItemBeneficiary from a dict
payable_contract_supplier_item_beneficiary_from_dict = PayableContractSupplierItemBeneficiary.from_dict(payable_contract_supplier_item_beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


