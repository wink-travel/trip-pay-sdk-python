# SetTaxIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | Updated tax identifier. I.e. SSN | 

## Example

```python
from trip_pay_payment.models.set_tax_identifier_request import SetTaxIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTaxIdentifierRequest from a JSON string
set_tax_identifier_request_instance = SetTaxIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(SetTaxIdentifierRequest.to_json())

# convert the object into a dict
set_tax_identifier_request_dict = set_tax_identifier_request_instance.to_dict()
# create an instance of SetTaxIdentifierRequest from a dict
set_tax_identifier_request_from_dict = SetTaxIdentifierRequest.from_dict(set_tax_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


