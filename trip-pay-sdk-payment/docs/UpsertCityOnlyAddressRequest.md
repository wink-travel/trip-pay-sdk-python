# UpsertCityOnlyAddressRequest

This address object only requires that cityGeoNameId be present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city_geo_name_id** | **str** | City geo name ID | 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | [optional] 
**county** | **str** | County | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from trip_pay_payment.models.upsert_city_only_address_request import UpsertCityOnlyAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCityOnlyAddressRequest from a JSON string
upsert_city_only_address_request_instance = UpsertCityOnlyAddressRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertCityOnlyAddressRequest.to_json())

# convert the object into a dict
upsert_city_only_address_request_dict = upsert_city_only_address_request_instance.to_dict()
# create an instance of UpsertCityOnlyAddressRequest from a dict
upsert_city_only_address_request_from_dict = UpsertCityOnlyAddressRequest.from_dict(upsert_city_only_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


