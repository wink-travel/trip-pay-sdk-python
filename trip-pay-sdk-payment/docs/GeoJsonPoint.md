# GeoJsonPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from trip_pay_payment.models.geo_json_point import GeoJsonPoint

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPoint from a JSON string
geo_json_point_instance = GeoJsonPoint.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPoint.to_json())

# convert the object into a dict
geo_json_point_dict = geo_json_point_instance.to_dict()
# create an instance of GeoJsonPoint from a dict
geo_json_point_from_dict = GeoJsonPoint.from_dict(geo_json_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


