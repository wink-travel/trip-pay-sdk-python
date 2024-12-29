# SupplierContractItemPolicy

Outlines the policy for this item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refundable** | **bool** | Whether this booking is refundable or not. | 
**advance_cancellation_free_of_charge** | **str** | When the cancellation policy is refundable, this flag can be set and indicates there is more rules involved than just a no-questions-asked refundable. | [optional] 
**refundable_cancellation_charge** | **str** | If advanceCancellationFreeOfCharge rules is not honored, this property explains what the guest will be charged. | [optional] 
**no_show_charge** | **str** | In case the &#39;Refundable cancellation charge&#39; is set, a different no show charge can be applied. | [optional] 
**non_refundable_cancellation_charge** | **str** | When the cancellation policy is non-refundable, this flag can be set and indicates there is more rules involved to calculate what the guest will owe in case of a cancellation. | [optional] 
**non_refundable_deadline** | **str** | The non-refundable charge might can have a deadline. If that deadline passes, the guest might be charged more. | [optional] 
**non_refundable_after_deadline_cancellation_charge** | **str** | If the guest does not honor the non-refundable deadline rule, this charge dictates what she owes after the deadline passes. | [optional] 
**external_identifier** | **str** | Optional geoname externalIdentifier to remote policy. | [optional] 
**fully_refundable** | **bool** |  | [optional] [readonly] 
**partially_refundable** | **bool** |  | [optional] [readonly] 

## Example

```python
from trip_pay_payment.models.supplier_contract_item_policy import SupplierContractItemPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierContractItemPolicy from a JSON string
supplier_contract_item_policy_instance = SupplierContractItemPolicy.from_json(json)
# print the JSON string representation of the object
print(SupplierContractItemPolicy.to_json())

# convert the object into a dict
supplier_contract_item_policy_dict = supplier_contract_item_policy_instance.to_dict()
# create an instance of SupplierContractItemPolicy from a dict
supplier_contract_item_policy_from_dict = SupplierContractItemPolicy.from_dict(supplier_contract_item_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


