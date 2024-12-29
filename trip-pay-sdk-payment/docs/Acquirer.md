# Acquirer

Payment method with the details describing how to make a reactive happen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirer_id** | **str** | Unique identifier. | 
**priority** | **int** | Determines how vendors are displayed in a list | 
**vendor** | **str** | Name of acquiring vendor | 
**type** | **str** | Technology taking the charge | 
**currency_code** | **str** | Currency in coverage region. | 
**credentials** | [**List[AcquirerCredentials]**](AcquirerCredentials.md) |  | 
**webhook_secret** | **str** |  | [optional] 
**public_token** | **str** |  | [optional] 

## Example

```python
from trip_pay_payment.models.acquirer import Acquirer

# TODO update the JSON string below
json = "{}"
# create an instance of Acquirer from a JSON string
acquirer_instance = Acquirer.from_json(json)
# print the JSON string representation of the object
print(Acquirer.to_json())

# convert the object into a dict
acquirer_dict = acquirer_instance.to_dict()
# create an instance of Acquirer from a dict
acquirer_from_dict = Acquirer.from_dict(acquirer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


