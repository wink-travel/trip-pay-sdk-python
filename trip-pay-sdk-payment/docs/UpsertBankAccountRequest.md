# UpsertBankAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Country of bank account | 
**currency_code** | **str** | Currency of bank account | 
**account_holder_name** | **str** | Bank account holder name | 
**swift_code** | **str** | Bank SWIFT code. Unique code identifier the bank and branch of the bank account. | [optional] 
**routing_number** | **str** | Bank account routing number. This is sort code in HK and Zengin code in JP. | [optional] 
**account_number** | **str** | Bank account number. In all EU countries, this would be the IBAN. In other countries, the routing number will apply as well. | 
**primary** | **bool** | One bank account always needs to be primary. | 

## Example

```python
from trip_pay_payment.models.upsert_bank_account_request import UpsertBankAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertBankAccountRequest from a JSON string
upsert_bank_account_request_instance = UpsertBankAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertBankAccountRequest.to_json())

# convert the object into a dict
upsert_bank_account_request_dict = upsert_bank_account_request_instance.to_dict()
# create an instance of UpsertBankAccountRequest from a dict
upsert_bank_account_request_from_dict = UpsertBankAccountRequest.from_dict(upsert_bank_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


