# UpdateManagingEntityInformationRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of account | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**description** | **str** | Short description of entity | 

## Example

```python
from trip_pay_payment.models.update_managing_entity_information_request_authenticated_entity import UpdateManagingEntityInformationRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManagingEntityInformationRequestAuthenticatedEntity from a JSON string
update_managing_entity_information_request_authenticated_entity_instance = UpdateManagingEntityInformationRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UpdateManagingEntityInformationRequestAuthenticatedEntity.to_json())

# convert the object into a dict
update_managing_entity_information_request_authenticated_entity_dict = update_managing_entity_information_request_authenticated_entity_instance.to_dict()
# create an instance of UpdateManagingEntityInformationRequestAuthenticatedEntity from a dict
update_managing_entity_information_request_authenticated_entity_from_dict = UpdateManagingEntityInformationRequestAuthenticatedEntity.from_dict(update_managing_entity_information_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


