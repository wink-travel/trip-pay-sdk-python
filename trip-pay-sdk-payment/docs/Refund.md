# Refund

Refund objects allow you to refund a charge that has previously been created but not yet refunded. Funds will be refunded to the credit or debit card that was originally charged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | A unique identifier | 
**acquirer_refund_identifier** | **str** | The acquirer refund identifier. Will get attached once it comes in on the webhook. | [optional] 
**requested_by_identifier** | **str** | The SSO person / entity that requested the refund. | [optional] 
**refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The amount refunded | 
**created** | **datetime** | When the amount was refunded | 
**description** | **str** | A description of the refund that can be displayed to booker | 
**reason_type** | **str** | A description of the refund that can be displayed to booker | 
**cancel_on_refund** | **str** | Whether to cancel the booking alongside requesting a refund. | 
**status_type** | **str** | Status of the refund | 
**request_type** | **str** | The entity making the refund request | 
**request_status** | **str** | Status of the refund request | 
**request_response** | **str** | Admin may choose to respond to the refund request made by the hotel | 
**receipt_url** | **str** | This is the receipt url that contains a friendly web confirmation page. Comes in on the webhook. | [optional] 
**retries** | **int** | In case a TripPay admin has to go in and re-send the refund request to Stripe, we want to not to the same calculations again when a retry is executed so we keep track of retries here. | [optional] [default to 0]
**allocation** | **str** | The type of refund determines how the funds are deducted each beneficiary. | [optional] [default to 'EQUAL_DISTRIBUTION']

## Example

```python
from trip_pay_payment.models.refund import Refund

# TODO update the JSON string below
json = "{}"
# create an instance of Refund from a JSON string
refund_instance = Refund.from_json(json)
# print the JSON string representation of the object
print(Refund.to_json())

# convert the object into a dict
refund_dict = refund_instance.to_dict()
# create an instance of Refund from a dict
refund_from_dict = Refund.from_dict(refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


