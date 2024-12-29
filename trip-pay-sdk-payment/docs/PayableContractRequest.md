# PayableContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**AuthenticatedUser**](AuthenticatedUser.md) |  | 
**affiliate_account_identifier** | **str** | affiliate account making the request | 
**affiliate_account_identifier_type** | **str** | Type of identifier this is | 
**display_currency** | **str** | The desired quote | [default to 'USD']
**contract_list** | [**List[PayableContractSupplier]**](PayableContractSupplier.md) |  | 
**trace_id** | **str** | Integrator can choose to include a unique identifier to help identify the collection of bookings | [optional] 
**redirect_url** | **str** | Where to redirect to after booking [in-]complete | 
**source_url** | **str** | Where the booking originate from | 
**metadata** | **Dict[str, str]** | Place to add more data related to the booking contract. | [optional] 

## Example

```python
from trip_pay_payment.models.payable_contract_request import PayableContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayableContractRequest from a JSON string
payable_contract_request_instance = PayableContractRequest.from_json(json)
# print the JSON string representation of the object
print(PayableContractRequest.to_json())

# convert the object into a dict
payable_contract_request_dict = payable_contract_request_instance.to_dict()
# create an instance of PayableContractRequest from a dict
payable_contract_request_from_dict = PayableContractRequest.from_dict(payable_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


