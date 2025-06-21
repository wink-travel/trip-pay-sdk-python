# SubSubCountryLightweight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**sub_country_code** | **str** |  | [optional] 
**sub_sub_country_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from trip_pay_payment.models.sub_sub_country_lightweight import SubSubCountryLightweight

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountryLightweight from a JSON string
sub_sub_country_lightweight_instance = SubSubCountryLightweight.from_json(json)
# print the JSON string representation of the object
print(SubSubCountryLightweight.to_json())

# convert the object into a dict
sub_sub_country_lightweight_dict = sub_sub_country_lightweight_instance.to_dict()
# create an instance of SubSubCountryLightweight from a dict
sub_sub_country_lightweight_from_dict = SubSubCountryLightweight.from_dict(sub_sub_country_lightweight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


