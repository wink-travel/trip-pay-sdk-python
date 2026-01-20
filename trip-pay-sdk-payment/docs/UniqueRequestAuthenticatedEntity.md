# UniqueRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name we want to check uniqueness for | 
**identifier** | **UUID** | An optional accompanying identifier so it doesn&#39;t check itself on an update | [optional] 

## Example

```python
from trip_pay_payment.models.unique_request_authenticated_entity import UniqueRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueRequestAuthenticatedEntity from a JSON string
unique_request_authenticated_entity_instance = UniqueRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UniqueRequestAuthenticatedEntity.to_json())

# convert the object into a dict
unique_request_authenticated_entity_dict = unique_request_authenticated_entity_instance.to_dict()
# create an instance of UniqueRequestAuthenticatedEntity from a dict
unique_request_authenticated_entity_from_dict = UniqueRequestAuthenticatedEntity.from_dict(unique_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


