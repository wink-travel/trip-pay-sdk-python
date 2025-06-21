# BookingContractItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier_item_booking_code** | **str** | Booking code identifying the supplier line item. | 
**user** | [**GuestUser**](GuestUser.md) |  | 
**name_in_english** | **str** | Name of item in English included in booking. | 
**description_in_english** | **str** | Short description in English of item included in booking. | 
**itinerary** | [**SimpleDateTimeItinerary**](SimpleDateTimeItinerary.md) |  | 
**pricing_type** | **str** | How to calculate the total amount. | 
**type** | **str** | Type of item this is. | 
**beneficiary_list** | [**List[Beneficiary]**](Beneficiary.md) |  | 
**payable** | **str** | When to charge for this item. | 
**policy** | [**SupplierContractItemPolicy**](SupplierContractItemPolicy.md) |  | [optional] 
**external_identifier** | **str** | Optional externalIdentifier to remote inventory. | [optional] 
**tokens_earned** | **int** | Tokens minted for this item | [optional] 
**daily_rate_list** | **List[object]** |  | [optional] 
**cancelled** | **bool** | Optional geoname externalIdentifier to remote inventory. | [optional] 
**source_currency** | **str** | The source currency | 
**display_currency** | **str** | The display currency | 
**supplier_currency** | **str** | The supplier currency | 
**internal_currency** | **str** | The internal currency | 
**capture_currency** | **str** | The capture currency | 
**source_amount** | **float** | The total initial price as quoted in the original TripPay contract. | 
**display_amount** | **float** | The total display price. | 
**supplier_amount** | **float** | The total supplier price. | 
**internal_amount** | **float** | The total internal price. | 
**capture_amount** | **float** | The total capture price. | 
**source_amount_refund_modifier** | **float** | The source amount still due after a partial refund occurs. | [optional] 
**display_amount_refund_modifier** | **float** | The display amount still due after a partial refund occurs. | [optional] 
**supplier_amount_refund_modifier** | **float** | The supplier amount still due after a partial refund occurs. | [optional] 
**internal_amount_refund_modifier** | **float** | The internal amount still due after a partial refund occurs. | [optional] 
**capture_amount_refund_modifier** | **float** | The capture amount still due after a partial refund occurs. | [optional] 
**net_source_amount** | **float** | Source amount minus source modifier. | 
**net_display_amount** | **float** | Display amount minus display modifier. | 
**net_supplier_amount** | **float** | Supplier amount minus supplier modifier. | 
**net_internal_amount** | **float** | Internal amount minus internal modifier. | 
**net_capture_amount** | **float** | Capture amount minus capture modifier. | 
**metadata** | **Dict[str, str]** | Place to add more data related to the booking contract item. | [optional] 
**cancellable_by_traveler** | **bool** | Whether the booking can still be cancelled by the traveller. | [optional] 
**cancellable_by_supplier_or_agent** | **bool** | Whether the booking can still be cancelled by the supplier. A supplier cancellation overrides the refundable | [optional] 
**cancellable_with_no_charges** | **bool** | Whether the booking can still be cancelled and whether cancellation charges might still occur. | [optional] 
**cancellable_with_potential_charges** | **bool** | Whether the booking can still be cancelled and whether cancellation charges might still occur. | [optional] 

## Example

```python
from trip_pay_payment.models.booking_contract_item import BookingContractItem

# TODO update the JSON string below
json = "{}"
# create an instance of BookingContractItem from a JSON string
booking_contract_item_instance = BookingContractItem.from_json(json)
# print the JSON string representation of the object
print(BookingContractItem.to_json())

# convert the object into a dict
booking_contract_item_dict = booking_contract_item_instance.to_dict()
# create an instance of BookingContractItem from a dict
booking_contract_item_from_dict = BookingContractItem.from_dict(booking_contract_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


