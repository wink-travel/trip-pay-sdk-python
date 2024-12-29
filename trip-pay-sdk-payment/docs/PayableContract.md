# PayableContract

A contract record is what gets saved upon pricing and converted to a BookingContract on reactive and subsequently removed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**affiliate** | [**AffiliateInformation**](AffiliateInformation.md) |  | 
**display_currency** | **str** | The desired quote | [default to 'USD']
**redirect_url** | **str** | Where to redirect to after booking [in-]complete | 
**contract** | [**PricedSupplierContractWithAcquirer**](PricedSupplierContractWithAcquirer.md) |  | 
**acquirer_list** | [**List[Acquirer]**](Acquirer.md) |  | 
**metadata** | **Dict[str, str]** | Depending on the acquirer, we put in required data for creating the payment. | [optional] 
**instant** | **datetime** | Date to attach TTL. Self-deletes after 1 hour of unuse. | 

## Example

```python
from trip_pay_payment.models.payable_contract import PayableContract

# TODO update the JSON string below
json = "{}"
# create an instance of PayableContract from a JSON string
payable_contract_instance = PayableContract.from_json(json)
# print the JSON string representation of the object
print(PayableContract.to_json())

# convert the object into a dict
payable_contract_dict = payable_contract_instance.to_dict()
# create an instance of PayableContract from a dict
payable_contract_from_dict = PayableContract.from_dict(payable_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


