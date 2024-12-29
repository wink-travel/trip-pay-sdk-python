# UpdateMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the entity being mapped | 

## Example

```python
from trip_pay_payment.models.update_mapping_request import UpdateMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMappingRequest from a JSON string
update_mapping_request_instance = UpdateMappingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMappingRequest.to_json())

# convert the object into a dict
update_mapping_request_dict = update_mapping_request_instance.to_dict()
# create an instance of UpdateMappingRequest from a dict
update_mapping_request_from_dict = UpdateMappingRequest.from_dict(update_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


