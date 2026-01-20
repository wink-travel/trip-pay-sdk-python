# InviteManagerRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Existing user account email to make manager | 

## Example

```python
from trip_pay_payment.models.invite_manager_request_affiliate import InviteManagerRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of InviteManagerRequestAffiliate from a JSON string
invite_manager_request_affiliate_instance = InviteManagerRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(InviteManagerRequestAffiliate.to_json())

# convert the object into a dict
invite_manager_request_affiliate_dict = invite_manager_request_affiliate_instance.to_dict()
# create an instance of InviteManagerRequestAffiliate from a dict
invite_manager_request_affiliate_from_dict = InviteManagerRequestAffiliate.from_dict(invite_manager_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


