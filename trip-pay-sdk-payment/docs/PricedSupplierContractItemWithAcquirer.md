# PricedSupplierContractItemWithAcquirer

Holds one booking line item for a specific supplier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**GuestUser**](GuestUser.md) |  | 
**name_in_english** | **str** | Name of item in English included in booking. | 
**description_in_english** | **str** | Short description in English of item included in booking. | 
**price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Raw incoming price. | 
**display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The displayPrice of this item. | 
**supplier_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The supplierPrice of this item. How it was captured by the acquirer. | 
**internal_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The internalPrice of this item. The price in platform currency. | 
**capture_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The capturePrice of this item. The price in capture currency. | 
**itinerary** | [**SimpleDateTimeItinerary**](SimpleDateTimeItinerary.md) |  | 
**pricing_type** | **str** | How to calculate the total amount. | 
**type** | **str** | Type of item this is. | 
**beneficiary_list** | [**List[PayableContractSupplierItemBeneficiary]**](PayableContractSupplierItemBeneficiary.md) |  | 
**payable** | **str** | When to charge for this item. | 
**policy** | [**SupplierContractItemPolicy**](SupplierContractItemPolicy.md) |  | [optional] 
**external_identifier** | **str** | Optional geoname externalIdentifier to remote inventory. | [optional] 
**daily_rate_list** | [**List[DailyRate]**](DailyRate.md) |  | [optional] 
**metadata** | **Dict[str, str]** | Place to add more data related to the booking contract. | [optional] 

## Example

```python
from trip_pay_payment.models.priced_supplier_contract_item_with_acquirer import PricedSupplierContractItemWithAcquirer

# TODO update the JSON string below
json = "{}"
# create an instance of PricedSupplierContractItemWithAcquirer from a JSON string
priced_supplier_contract_item_with_acquirer_instance = PricedSupplierContractItemWithAcquirer.from_json(json)
# print the JSON string representation of the object
print(PricedSupplierContractItemWithAcquirer.to_json())

# convert the object into a dict
priced_supplier_contract_item_with_acquirer_dict = priced_supplier_contract_item_with_acquirer_instance.to_dict()
# create an instance of PricedSupplierContractItemWithAcquirer from a dict
priced_supplier_contract_item_with_acquirer_from_dict = PricedSupplierContractItemWithAcquirer.from_dict(priced_supplier_contract_item_with_acquirer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


