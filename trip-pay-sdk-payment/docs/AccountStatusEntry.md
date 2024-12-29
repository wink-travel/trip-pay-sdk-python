# AccountStatusEntry

Describes a specific issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Unique task identifier. | 
**type** | **str** | Type of textual entry | 
**text** | **str** | Textual description of . | 

## Example

```python
from trip_pay_payment.models.account_status_entry import AccountStatusEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatusEntry from a JSON string
account_status_entry_instance = AccountStatusEntry.from_json(json)
# print the JSON string representation of the object
print(AccountStatusEntry.to_json())

# convert the object into a dict
account_status_entry_dict = account_status_entry_instance.to_dict()
# create an instance of AccountStatusEntry from a dict
account_status_entry_from_dict = AccountStatusEntry.from_dict(account_status_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


