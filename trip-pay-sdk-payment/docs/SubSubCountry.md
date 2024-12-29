# SubSubCountry

Country sub sub division

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
from trip_pay_payment.models.sub_sub_country import SubSubCountry

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountry from a JSON string
sub_sub_country_instance = SubSubCountry.from_json(json)
# print the JSON string representation of the object
print(SubSubCountry.to_json())

# convert the object into a dict
sub_sub_country_dict = sub_sub_country_instance.to_dict()
# create an instance of SubSubCountry from a dict
sub_sub_country_from_dict = SubSubCountry.from_dict(sub_sub_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


