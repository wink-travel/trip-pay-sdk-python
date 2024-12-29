# AcquirerCredentials

How we interact with the acquirer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of credentials | 
**key1** | **str** | A key that can be used as a token | 
**key2** | **str** | Can be used alongside key1 as credentials | 

## Example

```python
from trip_pay_payment.models.acquirer_credentials import AcquirerCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AcquirerCredentials from a JSON string
acquirer_credentials_instance = AcquirerCredentials.from_json(json)
# print the JSON string representation of the object
print(AcquirerCredentials.to_json())

# convert the object into a dict
acquirer_credentials_dict = acquirer_credentials_instance.to_dict()
# create an instance of AcquirerCredentials from a dict
acquirer_credentials_from_dict = AcquirerCredentials.from_dict(acquirer_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


