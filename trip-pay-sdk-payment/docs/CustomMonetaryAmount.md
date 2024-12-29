# CustomMonetaryAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**currency** | **str** |  | 

## Example

```python
from trip_pay_payment.models.custom_monetary_amount import CustomMonetaryAmount

# TODO update the JSON string below
json = "{}"
# create an instance of CustomMonetaryAmount from a JSON string
custom_monetary_amount_instance = CustomMonetaryAmount.from_json(json)
# print the JSON string representation of the object
print(CustomMonetaryAmount.to_json())

# convert the object into a dict
custom_monetary_amount_dict = custom_monetary_amount_instance.to_dict()
# create an instance of CustomMonetaryAmount from a dict
custom_monetary_amount_from_dict = CustomMonetaryAmount.from_dict(custom_monetary_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


