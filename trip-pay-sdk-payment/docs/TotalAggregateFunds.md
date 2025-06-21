# TotalAggregateFunds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** |  | [optional] 
**display_currency** | **str** |  | [optional] 
**supplier_currency** | **str** |  | [optional] 
**internal_currency** | **str** |  | [optional] 
**capture_currency** | **str** |  | [optional] 
**source_amount** | **float** |  | [optional] 
**display_amount** | **float** |  | [optional] 
**supplier_amount** | **float** |  | [optional] 
**internal_amount** | **float** |  | [optional] 
**capture_amount** | **float** |  | [optional] 

## Example

```python
from trip_pay_payment.models.total_aggregate_funds import TotalAggregateFunds

# TODO update the JSON string below
json = "{}"
# create an instance of TotalAggregateFunds from a JSON string
total_aggregate_funds_instance = TotalAggregateFunds.from_json(json)
# print the JSON string representation of the object
print(TotalAggregateFunds.to_json())

# convert the object into a dict
total_aggregate_funds_dict = total_aggregate_funds_instance.to_dict()
# create an instance of TotalAggregateFunds from a dict
total_aggregate_funds_from_dict = TotalAggregateFunds.from_dict(total_aggregate_funds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


