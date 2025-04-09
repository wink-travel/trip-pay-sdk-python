# AvailableFunds

Object that holds before and after values of a particular amount after refund has been applied

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** |  | 
**supplier_currency** | **str** |  | 
**capture_currency** | **str** |  | 
**supplier_amount** | **float** |  | 
**capture_amount** | **float** |  | 

## Example

```python
from trip_pay_payment.models.available_funds import AvailableFunds

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableFunds from a JSON string
available_funds_instance = AvailableFunds.from_json(json)
# print the JSON string representation of the object
print(AvailableFunds.to_json())

# convert the object into a dict
available_funds_dict = available_funds_instance.to_dict()
# create an instance of AvailableFunds from a dict
available_funds_from_dict = AvailableFunds.from_dict(available_funds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


