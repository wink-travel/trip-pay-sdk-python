# SimpleAddress

Address information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | [optional] 
**county** | **str** | County | [optional] 
**city** | **str** | City name | [optional] 
**country_code** | **str** | Country | [optional] 
**country** | **str** | Country | [optional] [readonly] 
**full_address** | **str** | Address 1, Address 2, City, State, Postal / Zip code, Country | [optional] [readonly] 

## Example

```python
from trip_pay_payment.models.simple_address import SimpleAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAddress from a JSON string
simple_address_instance = SimpleAddress.from_json(json)
# print the JSON string representation of the object
print(SimpleAddress.to_json())

# convert the object into a dict
simple_address_dict = simple_address_instance.to_dict()
# create an instance of SimpleAddress from a dict
simple_address_from_dict = SimpleAddress.from_dict(simple_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


