# RawDailyRate

In case of LODGING, include daily rates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date this rate is applicable for. | 
**price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 

## Example

```python
from trip_pay_payment.models.raw_daily_rate import RawDailyRate

# TODO update the JSON string below
json = "{}"
# create an instance of RawDailyRate from a JSON string
raw_daily_rate_instance = RawDailyRate.from_json(json)
# print the JSON string representation of the object
print(RawDailyRate.to_json())

# convert the object into a dict
raw_daily_rate_dict = raw_daily_rate_instance.to_dict()
# create an instance of RawDailyRate from a dict
raw_daily_rate_from_dict = RawDailyRate.from_dict(raw_daily_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


