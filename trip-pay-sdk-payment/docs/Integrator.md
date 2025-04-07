# Integrator

Payment method with the details describing how to make a reactive happen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier. | 
**name** | **str** | Integrator. | 
**priority** | **int** | Determines how vendors are displayed in a list | 
**vendor** | **str** | Name of acquiring vendor | 
**type** | **str** | Technology taking the charge | 
**currency_code** | **str** | Currency in coverage region. | 
**credentials** | [**List[AcquirerCredentials]**](AcquirerCredentials.md) |  | 
**webhook_secret** | **str** |  | [optional] 
**public_token** | **str** |  | [optional] 

## Example

```python
from trip_pay_payment.models.integrator import Integrator

# TODO update the JSON string below
json = "{}"
# create an instance of Integrator from a JSON string
integrator_instance = Integrator.from_json(json)
# print the JSON string representation of the object
print(Integrator.to_json())

# convert the object into a dict
integrator_dict = integrator_instance.to_dict()
# create an instance of Integrator from a dict
integrator_from_dict = Integrator.from_dict(integrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


