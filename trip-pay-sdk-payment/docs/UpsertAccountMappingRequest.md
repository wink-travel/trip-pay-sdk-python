# UpsertAccountMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_account_identifier** | **UUID** | Local account identifier is the local identifier | 
**external_identifier** | **str** | External identifier is the identifier of this entity in a remote system | 

## Example

```python
from trip_pay_payment.models.upsert_account_mapping_request import UpsertAccountMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAccountMappingRequest from a JSON string
upsert_account_mapping_request_instance = UpsertAccountMappingRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertAccountMappingRequest.to_json())

# convert the object into a dict
upsert_account_mapping_request_dict = upsert_account_mapping_request_instance.to_dict()
# create an instance of UpsertAccountMappingRequest from a dict
upsert_account_mapping_request_from_dict = UpsertAccountMappingRequest.from_dict(upsert_account_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


