# CreateIssuingCardEphemeralKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Which coverage area is Stripe customer occurring in. | 

## Example

```python
from trip_pay_payment.models.create_issuing_card_ephemeral_key_response import CreateIssuingCardEphemeralKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssuingCardEphemeralKeyResponse from a JSON string
create_issuing_card_ephemeral_key_response_instance = CreateIssuingCardEphemeralKeyResponse.from_json(json)
# print the JSON string representation of the object
print(CreateIssuingCardEphemeralKeyResponse.to_json())

# convert the object into a dict
create_issuing_card_ephemeral_key_response_dict = create_issuing_card_ephemeral_key_response_instance.to_dict()
# create an instance of CreateIssuingCardEphemeralKeyResponse from a dict
create_issuing_card_ephemeral_key_response_from_dict = CreateIssuingCardEphemeralKeyResponse.from_dict(create_issuing_card_ephemeral_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


