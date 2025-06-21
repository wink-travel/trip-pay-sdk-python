# BankAccount

Accounts use bank accounts to get paid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique bank account identifier | 
**country_code** | **str** | Country of bank account | 
**currency_code** | **str** | Currency of bank account | 
**account_holder_name** | **str** | Bank account holder name | 
**swift_code** | **str** | Bank SWIFT code. Unique code identifier the bank and branch of the bank account. | [optional] 
**routing_number** | **str** | Bank account routing number. This is sort code in HK and Zengin code in JP. | [optional] 
**account_number** | **str** | Bank account number. In all EU countries, this would be the IBAN. In other countries, the routing number will apply as well. | 
**primary** | **bool** | One bank account always needs to be primary. | 

## Example

```python
from trip_pay_payment.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print(BankAccount.to_json())

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_from_dict = BankAccount.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


