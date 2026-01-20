# ChangeManagingEntityNameRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_name** | **str** | Doing business as name. | 
**legal_name** | **str** | Hotel chain name if property is part of that chain. | [optional] 

## Example

```python
from trip_pay_payment.models.change_managing_entity_name_request_authenticated_entity import ChangeManagingEntityNameRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeManagingEntityNameRequestAuthenticatedEntity from a JSON string
change_managing_entity_name_request_authenticated_entity_instance = ChangeManagingEntityNameRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ChangeManagingEntityNameRequestAuthenticatedEntity.to_json())

# convert the object into a dict
change_managing_entity_name_request_authenticated_entity_dict = change_managing_entity_name_request_authenticated_entity_instance.to_dict()
# create an instance of ChangeManagingEntityNameRequestAuthenticatedEntity from a dict
change_managing_entity_name_request_authenticated_entity_from_dict = ChangeManagingEntityNameRequestAuthenticatedEntity.from_dict(change_managing_entity_name_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


