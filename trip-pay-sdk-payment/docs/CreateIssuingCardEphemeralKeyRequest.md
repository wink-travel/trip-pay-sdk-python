# CreateIssuingCardEphemeralKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_identifier** | **str** | Which coverage area is Stripe customer occurring in. | 
**issuing_card** | **str** | The cardholder unique ID. | 
**nonce** | **str** | A unique none. | 

## Example

```python
from trip_pay_payment.models.create_issuing_card_ephemeral_key_request import CreateIssuingCardEphemeralKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssuingCardEphemeralKeyRequest from a JSON string
create_issuing_card_ephemeral_key_request_instance = CreateIssuingCardEphemeralKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateIssuingCardEphemeralKeyRequest.to_json())

# convert the object into a dict
create_issuing_card_ephemeral_key_request_dict = create_issuing_card_ephemeral_key_request_instance.to_dict()
# create an instance of CreateIssuingCardEphemeralKeyRequest from a dict
create_issuing_card_ephemeral_key_request_from_dict = CreateIssuingCardEphemeralKeyRequest.from_dict(create_issuing_card_ephemeral_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


