# Account

Account holds KYC, bank account and contact information of an affiliate, supplier, user or any type of entity that is to be a beneficiary of funds through the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**type** | **str** | Type of account tells us what the account is capable of. | 
**owner_type** | **str** | Type of account owner tells us whether ths account is managed by a company or an individual. | 
**account_owner_identifier** | **str** | The entity that created this account. | 
**name** | **str** | Name of company / full name of person | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**user_identifier** | **str** | The authenticated user that owns this account. | 
**owner** | [**Contact**](Contact.md) | The owning user entity. | 
**account_email** | **str** | Account email is where we will send KYC documents and other account specific mailings | 
**account_phone_number** | **str** | Account phone number is mostly used for KYC purchases | [optional] 
**description** | **str** | Short company / person description. | 
**url** | **str** | AffiliateAccount website. If private person with no personal website, link to main social network account. | 
**status** | **str** | Account status shows if it&#39;s approved | [default to 'REGISTERED']
**currency_code** | **str** | Account&#39;s main currency. | 
**address** | [**Address**](Address.md) | Account address. Usually the business address | 
**acquirers** | **List[object]** |  | [optional] 
**bank_accounts** | [**List[BankAccount]**](BankAccount.md) |  | [optional] 
**owner_type_identifier** | **str** | This is the tax identification number (TIN) for individuals and entity identification number (EIN) for companies. | [optional] 
**dob** | **date** | This is the individual&#39;s date of birth. | [optional] 
**tasks** | **List[object]** |  | [optional] 
**preferred_disbursement_type** | **str** | The preferred method which the account holder wishes to be paid. This will play a role if we choose to automate the payout flow. | [optional] [default to 'BANK_TRANSFER']
**vat_id** | **str** | An optional VAT ID | [optional] 

## Example

```python
from trip_pay_payment.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


