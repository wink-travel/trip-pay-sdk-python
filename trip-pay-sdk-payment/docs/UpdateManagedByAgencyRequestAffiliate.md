# UpdateManagedByAgencyRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managing_entity_identifier** | **str** | Existing user account managingEntityIdentifier to make manager | 
**commission_in_percent** | **float** | Agency commission | 
**rules** | [**ManagedByEntityRulesAffiliate**](ManagedByEntityRulesAffiliate.md) | Optional rules for expiration date etc when agency is no longer managing this entity. | [optional] 

## Example

```python
from trip_pay_payment.models.update_managed_by_agency_request_affiliate import UpdateManagedByAgencyRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManagedByAgencyRequestAffiliate from a JSON string
update_managed_by_agency_request_affiliate_instance = UpdateManagedByAgencyRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpdateManagedByAgencyRequestAffiliate.to_json())

# convert the object into a dict
update_managed_by_agency_request_affiliate_dict = update_managed_by_agency_request_affiliate_instance.to_dict()
# create an instance of UpdateManagedByAgencyRequestAffiliate from a dict
update_managed_by_agency_request_affiliate_from_dict = UpdateManagedByAgencyRequestAffiliate.from_dict(update_managed_by_agency_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


