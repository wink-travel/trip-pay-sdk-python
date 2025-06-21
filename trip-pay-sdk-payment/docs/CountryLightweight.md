# CountryLightweight

CountryLightweight

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso** | **str** | ISO code | [optional] 
**iso3** | **str** | 3 character ISO code | [optional] 
**iso_numeric** | **int** | Numeric ISO code | [optional] 
**fips** | **str** | FIPS country code | [optional] 
**name** | **str** | CountryLightweight name | [optional] 
**capital** | **str** | CountryLightweight capital | [optional] 
**area** | **float** | Area in square kilometers | [optional] 
**population** | **int** | CountryLightweight population | [optional] 
**continent** | **str** | Continent code | [optional] 
**top_level_domain** | **str** | CountryLightweight TLD | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**currency_name** | **str** | Currency name | [optional] 
**phone** | **str** | Calling code | [optional] 
**postal_code_format** | **str** | Postal code format | [optional] 
**postal_code_reg_ex** | **str** | Postal code regular expression | [optional] 
**languages** | **List[object]** |  | [optional] 
**geo_name_id** | **str** | CountryLightweight GeoNames identifier | [optional] 
**neighbors** | **List[object]** |  | [optional] 

## Example

```python
from trip_pay_payment.models.country_lightweight import CountryLightweight

# TODO update the JSON string below
json = "{}"
# create an instance of CountryLightweight from a JSON string
country_lightweight_instance = CountryLightweight.from_json(json)
# print the JSON string representation of the object
print(CountryLightweight.to_json())

# convert the object into a dict
country_lightweight_dict = country_lightweight_instance.to_dict()
# create an instance of CountryLightweight from a dict
country_lightweight_from_dict = CountryLightweight.from_dict(country_lightweight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


