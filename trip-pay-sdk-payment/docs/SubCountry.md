# SubCountry

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
from trip_pay_payment.models.sub_country import SubCountry

# TODO update the JSON string below
json = "{}"
# create an instance of SubCountry from a JSON string
sub_country_instance = SubCountry.from_json(json)
# print the JSON string representation of the object
print(SubCountry.to_json())

# convert the object into a dict
sub_country_dict = sub_country_instance.to_dict()
# create an instance of SubCountry from a dict
sub_country_from_dict = SubCountry.from_dict(sub_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


