# SimpleAddressAuthenticatedEntity

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
from trip_pay_payment.models.simple_address_authenticated_entity import SimpleAddressAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAddressAuthenticatedEntity from a JSON string
simple_address_authenticated_entity_instance = SimpleAddressAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SimpleAddressAuthenticatedEntity.to_json())

# convert the object into a dict
simple_address_authenticated_entity_dict = simple_address_authenticated_entity_instance.to_dict()
# create an instance of SimpleAddressAuthenticatedEntity from a dict
simple_address_authenticated_entity_from_dict = SimpleAddressAuthenticatedEntity.from_dict(simple_address_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


