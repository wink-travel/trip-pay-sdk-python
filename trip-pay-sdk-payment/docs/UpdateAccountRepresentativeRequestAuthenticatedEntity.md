# UpdateAccountRepresentativeRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_email** | **str** | Account email | 
**account_phone_number** | **str** | Account phone number | 

## Example

```python
from trip_pay_payment.models.update_account_representative_request_authenticated_entity import UpdateAccountRepresentativeRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountRepresentativeRequestAuthenticatedEntity from a JSON string
update_account_representative_request_authenticated_entity_instance = UpdateAccountRepresentativeRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountRepresentativeRequestAuthenticatedEntity.to_json())

# convert the object into a dict
update_account_representative_request_authenticated_entity_dict = update_account_representative_request_authenticated_entity_instance.to_dict()
# create an instance of UpdateAccountRepresentativeRequestAuthenticatedEntity from a dict
update_account_representative_request_authenticated_entity_from_dict = UpdateAccountRepresentativeRequestAuthenticatedEntity.from_dict(update_account_representative_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


