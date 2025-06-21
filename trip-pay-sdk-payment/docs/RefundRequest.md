# RefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The amount refunded | 
**description** | **str** | A description of the refund that can be displayed to booker | 
**reason_type** | **str** | A description of the refund that can be displayed to booker | 
**cancel_on_refund** | **str** | Whether to cancel the booking alongside requesting a refund. | 

## Example

```python
from trip_pay_payment.models.refund_request import RefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequest from a JSON string
refund_request_instance = RefundRequest.from_json(json)
# print the JSON string representation of the object
print(RefundRequest.to_json())

# convert the object into a dict
refund_request_dict = refund_request_instance.to_dict()
# create an instance of RefundRequest from a dict
refund_request_from_dict = RefundRequest.from_dict(refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


