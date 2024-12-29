# Country

Country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso** | **str** | ISO code | [optional] 
**iso3** | **str** | 3 character ISO code | [optional] 
**iso_numeric** | **int** | Numeric ISO code | [optional] 
**fips** | **str** | FIPS country code | [optional] 
**name** | **str** | Country name | [optional] 
**capital** | **str** | Country capital | [optional] 
**area** | **float** | Area in square kilometers | [optional] 
**population** | **int** | Country population | [optional] 
**continent** | **str** | Continent code | [optional] 
**top_level_domain** | **str** | Country TLD | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**currency_name** | **str** | Currency name | [optional] 
**phone** | **str** | Calling code | [optional] 
**postal_code_format** | **str** | Postal code format | [optional] 
**postal_code_reg_ex** | **str** | Postal code regular expression | [optional] 
**languages** | **List[str]** | Country languages | [optional] 
**geo_name_id** | **str** | Country GeoNames identifier | [optional] 
**neighbors** | **List[str]** | Neighboring countries | [optional] 

## Example

```python
from trip_pay_payment.models.country import Country

# TODO update the JSON string below
json = "{}"
# create an instance of Country from a JSON string
country_instance = Country.from_json(json)
# print the JSON string representation of the object
print(Country.to_json())

# convert the object into a dict
country_dict = country_instance.to_dict()
# create an instance of Country from a dict
country_from_dict = Country.from_dict(country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


