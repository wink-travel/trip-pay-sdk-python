# DailyRate

In case of LODGING, include daily rates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date this rate is applicable for. | 
**price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The displayPrice of this item in the original displayPrice quoted in the TripPay contract. | 
**display_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The displayPrice of this item converted to desired quote. | 
**supplier_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The displayPrice of this item converted to supplier quote. | 
**internal_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The internalPrice of this item. The price in platform currency. | 
**capture_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | The capturePrice of this item. The price we charged with the acquirer. | 

## Example

```python
from trip_pay_payment.models.daily_rate import DailyRate

# TODO update the JSON string below
json = "{}"
# create an instance of DailyRate from a JSON string
daily_rate_instance = DailyRate.from_json(json)
# print the JSON string representation of the object
print(DailyRate.to_json())

# convert the object into a dict
daily_rate_dict = daily_rate_instance.to_dict()
# create an instance of DailyRate from a dict
daily_rate_from_dict = DailyRate.from_dict(daily_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


