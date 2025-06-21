# PayableContractSupplierItem

Holds one booking line item for a specific supplier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**GuestUser**](GuestUser.md) | Person doing the booking. | 
**name_in_english** | **str** | Name of item in English included in booking. | 
**description_in_english** | **str** | Short description in English of item included in booking. | 
**price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Raw incoming price. | 
**itinerary** | [**SimpleDateTimeItinerary**](SimpleDateTimeItinerary.md) |  | 
**pricing_type** | **str** | Indicates the way this item should be priced. | 
**type** | **str** | Type of item this is. | 
**beneficiary_list** | [**List[PayableContractSupplierItemBeneficiary]**](PayableContractSupplierItemBeneficiary.md) |  | 
**payable** | **str** | When to charge for this item. | 
**policy** | [**SupplierContractItemPolicy**](SupplierContractItemPolicy.md) |  | [optional] 
**external_identifier** | **str** | Optional geoname externalIdentifier to remote blocking. | [optional] 
**daily_rate_list** | **List[object]** |  | [optional] 
**metadata** | **Dict[str, str]** | Place to add more data related to the booking contract item. | [optional] 

## Example

```python
from trip_pay_payment.models.payable_contract_supplier_item import PayableContractSupplierItem

# TODO update the JSON string below
json = "{}"
# create an instance of PayableContractSupplierItem from a JSON string
payable_contract_supplier_item_instance = PayableContractSupplierItem.from_json(json)
# print the JSON string representation of the object
print(PayableContractSupplierItem.to_json())

# convert the object into a dict
payable_contract_supplier_item_dict = payable_contract_supplier_item_instance.to_dict()
# create an instance of PayableContractSupplierItem from a dict
payable_contract_supplier_item_from_dict = PayableContractSupplierItem.from_dict(payable_contract_supplier_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


