# UpsertAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_type_identifier** | **str** | Account phone number is mostly used for KYC purchases | [optional] 
**dob** | **date** | Account&#39;s main currency. | [optional] 
**preferred_disbursement_type** | **str** | The preferred method which the account holder wishes to be paid. This will play a role if we choose to automate the payout flow. | [optional] [default to 'BANK_TRANSFER']

## Example

```python
from trip_pay_payment.models.upsert_account_request import UpsertAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAccountRequest from a JSON string
upsert_account_request_instance = UpsertAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertAccountRequest.to_json())

# convert the object into a dict
upsert_account_request_dict = upsert_account_request_instance.to_dict()
# create an instance of UpsertAccountRequest from a dict
upsert_account_request_from_dict = UpsertAccountRequest.from_dict(upsert_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


