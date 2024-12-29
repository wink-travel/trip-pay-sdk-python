# BookingContractItemCancellableResponse

Contract item cancellable object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier_item_booking_code** | **str** | Booking code identifying the supplier line item. | [optional] 
**name_in_english** | **str** | Name of item in English included in booking. | [optional] 
**policy** | [**SupplierContractItemPolicy**](SupplierContractItemPolicy.md) |  | [optional] 
**type** | **str** | Type of item this is. | [optional] 
**source_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**supplier_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**capture_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**cancellable_by_traveler** | **bool** | Whether this item can be cancelled by traveler either fully or partially. | [optional] 
**cancellable_by_supplier** | **bool** | Whether this item can be cancelled by supplier either fully or partially. | [optional] 
**cancellable_with_charges** | **bool** | Whether this item can be cancelled by supplier either fully or partially. | [optional] 
**source_price_after_refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**supplier_price_after_refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**display_price_after_refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_price_after_refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**capture_price_after_refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from trip_pay_payment.models.booking_contract_item_cancellable_response import BookingContractItemCancellableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BookingContractItemCancellableResponse from a JSON string
booking_contract_item_cancellable_response_instance = BookingContractItemCancellableResponse.from_json(json)
# print the JSON string representation of the object
print(BookingContractItemCancellableResponse.to_json())

# convert the object into a dict
booking_contract_item_cancellable_response_dict = booking_contract_item_cancellable_response_instance.to_dict()
# create an instance of BookingContractItemCancellableResponse from a dict
booking_contract_item_cancellable_response_from_dict = BookingContractItemCancellableResponse.from_dict(booking_contract_item_cancellable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


