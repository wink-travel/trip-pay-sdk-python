# CreateMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_account_identifier** | **UUID** | Local account identifier is the local identifier | 
**external_identifier** | **str** | External identifier is the identifier of this entity in a remote system | 
**account_identifier** | **UUID** | Account identifier is the account doing the mapping | 
**name** | **str** | Name of the entity being mapped | 

## Example

```python
from trip_pay_payment.models.create_mapping_request import CreateMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMappingRequest from a JSON string
create_mapping_request_instance = CreateMappingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMappingRequest.to_json())

# convert the object into a dict
create_mapping_request_dict = create_mapping_request_instance.to_dict()
# create an instance of CreateMappingRequest from a dict
create_mapping_request_from_dict = CreateMappingRequest.from_dict(create_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


