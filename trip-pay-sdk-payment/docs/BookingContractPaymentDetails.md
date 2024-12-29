# BookingContractPaymentDetails

Details of the payment. Payment details will be empty if account type is AGENT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirer_identifier** | **str** | Unique acquiring identifier. Blank for agent payment | 
**vendor** | **str** | Name of acquiring vendor | 
**transaction_identifier** | **str** | Unique transaction id from the vendor. Agent adds their transaction identifier. | 
**customer_identifier** | **str** | Unique customer id from the vendor. Agent adds their own customer identifier. | 
**charge_identifier** | **str** | Unique charge id from the vendor.. | 
**status** | **str** | Unique transaction id from the vendor upon a successful sale. Agent adds their transaction identifier. | 
**agent_invoiced_date** | **datetime** | The date/time the invoice was generated | [optional] 
**agent_invoice_identifier** | **str** | The specific invoice this booking was registered on | [optional] 
**redirect_url** | **str** | Where to redirect to after payment [in-]complete | [optional] 
**fees** | [**List[Fee]**](Fee.md) |  | [optional] 
**vendor_specific** | **Dict[str, str]** | Vendor specific values that are returned in a successful response | 

## Example

```python
from trip_pay_payment.models.booking_contract_payment_details import BookingContractPaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BookingContractPaymentDetails from a JSON string
booking_contract_payment_details_instance = BookingContractPaymentDetails.from_json(json)
# print the JSON string representation of the object
print(BookingContractPaymentDetails.to_json())

# convert the object into a dict
booking_contract_payment_details_dict = booking_contract_payment_details_instance.to_dict()
# create an instance of BookingContractPaymentDetails from a dict
booking_contract_payment_details_from_dict = BookingContractPaymentDetails.from_dict(booking_contract_payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


