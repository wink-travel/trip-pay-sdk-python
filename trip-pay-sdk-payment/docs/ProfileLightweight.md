# ProfileLightweight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **UUID** | Profile identifier | 
**user_identifier** | **UUID** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUser**](ProfileUser.md) | User details | 
**personal** | [**Personal**](Personal.md) | Detailed customer information for this profile | 
**preferences** | [**Preferences**](Preferences.md) | Customer preferences | 

## Example

```python
from trip_pay_payment.models.profile_lightweight import ProfileLightweight

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileLightweight from a JSON string
profile_lightweight_instance = ProfileLightweight.from_json(json)
# print the JSON string representation of the object
print(ProfileLightweight.to_json())

# convert the object into a dict
profile_lightweight_dict = profile_lightweight_instance.to_dict()
# create an instance of ProfileLightweight from a dict
profile_lightweight_from_dict = ProfileLightweight.from_dict(profile_lightweight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


