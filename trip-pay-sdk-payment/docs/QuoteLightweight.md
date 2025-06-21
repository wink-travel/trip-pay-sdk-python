# QuoteLightweight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source | 
**target** | **str** | Target | 
**exchange_rate** | **float** | Exchange rate | 
**timestamp** | **int** | Timestamp | 

## Example

```python
from trip_pay_payment.models.quote_lightweight import QuoteLightweight

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLightweight from a JSON string
quote_lightweight_instance = QuoteLightweight.from_json(json)
# print the JSON string representation of the object
print(QuoteLightweight.to_json())

# convert the object into a dict
quote_lightweight_dict = quote_lightweight_instance.to_dict()
# create an instance of QuoteLightweight from a dict
quote_lightweight_from_dict = QuoteLightweight.from_dict(quote_lightweight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


