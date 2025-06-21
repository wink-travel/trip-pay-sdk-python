# Preferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_location_pref** | **str** | Indicates preference for hotel property locations. | [optional] 
**property_type_pref** | **str** | Indicates preference for hotel property types. | [optional] 
**hotel_chain_pref** | **str** | Identifies a preferred company by name. | [optional] 
**property_amenity_pref** | **List[str]** |  | [optional] 
**recreation_srvc_pref** | **List[str]** |  | [optional] 
**business_srvc_pref** | **List[str]** |  | [optional] 
**security_feature_pref** | **List[str]** |  | [optional] 
**phys_chal_feature_pref** | **List[str]** | Indicates preferences for type of features required to meet the needs of persons with physical challenges, disabilities, etc. | [optional] 
**smoking_allowed** | **bool** | Indicates preference for smooking allowed rooms.. | [optional] 
**room_location_pref** | **str** | Indicates preference for hotel room locations. | [optional] 
**bed_type_pref** | **str** | Indicates preferences for the size and features of hotel bed types. | [optional] 
**food_srvc_pref** | **str** | Indicates preferences for type of food listener facilities in a hotel. | [optional] 
**room_amenity_pref** | **List[str]** |  | [optional] 
**guest_type** | **str** | Guest type | [optional] 
**meal_pref** | **str** | Indicates meal preference. | [optional] 
**cuisine_pref** | **str** | Indicates cuisine preference. | [optional] 
**interest_pref** | **List[str]** |  | [optional] 
**beverage_pref** | **List[str]** |  | [optional] 
**food_pref** | **List[str]** |  | [optional] 
**allergies** | **List[str]** |  | [optional] 
**pets_pref** | **List[str]** |  | [optional] 

## Example

```python
from trip_pay_payment.models.preferences import Preferences

# TODO update the JSON string below
json = "{}"
# create an instance of Preferences from a JSON string
preferences_instance = Preferences.from_json(json)
# print the JSON string representation of the object
print(Preferences.to_json())

# convert the object into a dict
preferences_dict = preferences_instance.to_dict()
# create an instance of Preferences from a dict
preferences_from_dict = Preferences.from_dict(preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


