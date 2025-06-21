# SubCountryLightweight

Country subdivision such as a state or province

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code | [optional] 
**country_code** | **str** | Country code | [optional] 
**sub_country_code** | **str** | Sub-country code | [optional] 
**name** | **str** | Sub-country name | [optional] 
**ascii_name** | **str** | Sub-country ascii name | [optional] 
**geo_name_id** | **str** | Sub-country GeoNames identifier | [optional] 

## Example

```python
from trip_pay_payment.models.sub_country_lightweight import SubCountryLightweight

# TODO update the JSON string below
json = "{}"
# create an instance of SubCountryLightweight from a JSON string
sub_country_lightweight_instance = SubCountryLightweight.from_json(json)
# print the JSON string representation of the object
print(SubCountryLightweight.to_json())

# convert the object into a dict
sub_country_lightweight_dict = sub_country_lightweight_instance.to_dict()
# create an instance of SubCountryLightweight from a dict
sub_country_lightweight_from_dict = SubCountryLightweight.from_dict(sub_country_lightweight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


