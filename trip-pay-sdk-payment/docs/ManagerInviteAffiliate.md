# ManagerInviteAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | AffiliateAccount ID | 
**name** | **str** | AffiliateAccount name | 
**image_identifier** | **str** | Image ID if available | [optional] 

## Example

```python
from trip_pay_payment.models.manager_invite_affiliate import ManagerInviteAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerInviteAffiliate from a JSON string
manager_invite_affiliate_instance = ManagerInviteAffiliate.from_json(json)
# print the JSON string representation of the object
print(ManagerInviteAffiliate.to_json())

# convert the object into a dict
manager_invite_affiliate_dict = manager_invite_affiliate_instance.to_dict()
# create an instance of ManagerInviteAffiliate from a dict
manager_invite_affiliate_from_dict = ManagerInviteAffiliate.from_dict(manager_invite_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


