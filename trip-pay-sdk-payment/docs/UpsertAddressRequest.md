# UpsertAddressRequest

Light-weight Address object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**city_geo_name_id** | **str** | City geo name ID | 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | 
**county** | **str** | County | [optional] 

## Example

```python
from trip_pay_payment.models.upsert_address_request import UpsertAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAddressRequest from a JSON string
upsert_address_request_instance = UpsertAddressRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertAddressRequest.to_json())

# convert the object into a dict
upsert_address_request_dict = upsert_address_request_instance.to_dict()
# create an instance of UpsertAddressRequest from a dict
upsert_address_request_from_dict = UpsertAddressRequest.from_dict(upsert_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


