# PendingRefund

When a refund is first requested, it ends up here. Once it is applied, it moves out of this list and into the parent modifier property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_identifier** | **str** | This is the refund identifier located on the root bookingContract.refunds object | 
**source_amount_refund_modifier** | **float** | The delta from the original source amount after a refund occurred | 
**display_amount_refund_modifier** | **float** | The delta from the original display amount after a refund occurred | 
**supplier_amount_refund_modifier** | **float** | The delta from the original supplier amount after a refund occurred | 
**internal_amount_refund_modifier** | **float** | The delta from the original internal amount after a refund occurred | 
**capture_amount_refund_modifier** | **float** | The delta from the original capture amount after a refund occurred | 

## Example

```python
from trip_pay_payment.models.pending_refund import PendingRefund

# TODO update the JSON string below
json = "{}"
# create an instance of PendingRefund from a JSON string
pending_refund_instance = PendingRefund.from_json(json)
# print the JSON string representation of the object
print(PendingRefund.to_json())

# convert the object into a dict
pending_refund_dict = pending_refund_instance.to_dict()
# create an instance of PendingRefund from a dict
pending_refund_from_dict = PendingRefund.from_dict(pending_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


