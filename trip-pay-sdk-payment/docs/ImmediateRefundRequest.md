# ImmediateRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of why an immediate refunds was requested. | 

## Example

```python
from trip_pay_payment.models.immediate_refund_request import ImmediateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImmediateRefundRequest from a JSON string
immediate_refund_request_instance = ImmediateRefundRequest.from_json(json)
# print the JSON string representation of the object
print(ImmediateRefundRequest.to_json())

# convert the object into a dict
immediate_refund_request_dict = immediate_refund_request_instance.to_dict()
# create an instance of ImmediateRefundRequest from a dict
immediate_refund_request_from_dict = ImmediateRefundRequest.from_dict(immediate_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


