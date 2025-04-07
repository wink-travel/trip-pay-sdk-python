# CreateAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_identifier** | **str** | Unique external record identifier | [optional] 
**type** | **str** | Type of account tells us what the account is capable of. | 
**owner_type** | **str** | Type of account owner tells us whether ths account is managed by a company or an individual. | 
**name** | **str** | Name of company / full name of person | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**user_identifier** | **str** | The authenticated user that owns this account. | [optional] 
**account_email** | **str** | Account email is where we will send KYC documents and other account specific mailings | 
**account_phone_number** | **str** | Account phone number is mostly used for KYC purchases | [optional] 
**description** | **str** | Short company / person description. | 
**url** | **str** | Company website. If private person with no personal website, link to main social network account. | 
**currency_code** | **str** | Account&#39;s main currency. | 
**address** | [**UpsertCityOnlyAddressRequest**](UpsertCityOnlyAddressRequest.md) |  | [optional] 
**acquirers** | [**List[Integrator]**](Integrator.md) |  | [optional] 
**bank_accounts** | [**List[UpsertBankAccountRequest]**](UpsertBankAccountRequest.md) |  | [optional] 
**owner_type_identifier** | **str** | This is the tax identification number (TIN) for individuals and entity identification number (EIN) for companies. | [optional] 
**dob** | **date** | This is the individual&#39;s date of birth. | [optional] 
**disbursement_type** | **str** | The method which the account holder wishes to be paid. | [optional] 

## Example

```python
from trip_pay_payment.models.create_account_request import CreateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountRequest from a JSON string
create_account_request_instance = CreateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAccountRequest.to_json())

# convert the object into a dict
create_account_request_dict = create_account_request_instance.to_dict()
# create an instance of CreateAccountRequest from a dict
create_account_request_from_dict = CreateAccountRequest.from_dict(create_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


