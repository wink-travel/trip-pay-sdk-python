# Mapping

Mapping record is responsible for mapping a local account identifier with a remote system. When a booking comes in from the remote system, we will know how to properly assign funds to the correct accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**account_owner_identifier** | **str** | The entity that owns this account. | 
**local_account_identifier** | **str** | Local account identifier is the account identifier of the remote entity within TripPay | 
**external_identifier** | **str** | External identifier is the identifier of this entity in a remote system | 
**account_identifier** | **str** | Account identifier is the account doing the mapping | 
**name** | **str** | Name of the entity being mapped | 

## Example

```python
from trip_pay_payment.models.mapping import Mapping

# TODO update the JSON string below
json = "{}"
# create an instance of Mapping from a JSON string
mapping_instance = Mapping.from_json(json)
# print the JSON string representation of the object
print(Mapping.to_json())

# convert the object into a dict
mapping_dict = mapping_instance.to_dict()
# create an instance of Mapping from a dict
mapping_from_dict = Mapping.from_dict(mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


