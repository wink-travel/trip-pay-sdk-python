# BeneficiaryAggregateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** | Beneficiary account identifier | 
**account_name** | **str** | Beneficiary account name | 
**type** | **str** | Type of reactive to beneficiary | 
**total_items_sold** | **int** | Total items sold | 
**supplier_currency** | **str** | The supplier currency | 
**internal_currency** | **str** | The internal currency | 
**supplier_amount** | **float** | Amount sold in supplier currency | 
**internal_amount** | **float** | Amount sold in internal currency | 

## Example

```python
from trip_pay_payment.models.beneficiary_aggregate_data import BeneficiaryAggregateData

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryAggregateData from a JSON string
beneficiary_aggregate_data_instance = BeneficiaryAggregateData.from_json(json)
# print the JSON string representation of the object
print(BeneficiaryAggregateData.to_json())

# convert the object into a dict
beneficiary_aggregate_data_dict = beneficiary_aggregate_data_instance.to_dict()
# create an instance of BeneficiaryAggregateData from a dict
beneficiary_aggregate_data_from_dict = BeneficiaryAggregateData.from_dict(beneficiary_aggregate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


