# GeoNameLightweightPayment

GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier | [optional] 
**type** | **str** | GeoNameLightweight type | [optional] 
**name** | **str** | Name of city | [optional] 
**url_name** | **str** | Url name | [optional] 
**ascii_name** | **str** | Ascii name of city | [optional] 
**location** | [**GeoJsonPoint**](GeoJsonPoint.md) | Coordinate points of the city | [optional] 
**feature_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**timezone** | **str** | Timezone | [optional] 
**country** | [**CountryLightweight**](CountryLightweight.md) | Country | [optional] 
**sub_country** | [**SubCountryLightweight**](SubCountryLightweight.md) | Country sub division | [optional] 
**sub_sub_country** | [**SubSubCountryLightweight**](SubSubCountryLightweight.md) | Country sub sub division | [optional] 

## Example

```python
from trip_pay_payment.models.geo_name_lightweight_payment import GeoNameLightweightPayment

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameLightweightPayment from a JSON string
geo_name_lightweight_payment_instance = GeoNameLightweightPayment.from_json(json)
# print the JSON string representation of the object
print(GeoNameLightweightPayment.to_json())

# convert the object into a dict
geo_name_lightweight_payment_dict = geo_name_lightweight_payment_instance.to_dict()
# create an instance of GeoNameLightweightPayment from a dict
geo_name_lightweight_payment_from_dict = GeoNameLightweightPayment.from_dict(geo_name_lightweight_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


