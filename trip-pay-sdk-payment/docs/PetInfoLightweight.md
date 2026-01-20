# PetInfoLightweight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from trip_pay_payment.models.pet_info_lightweight import PetInfoLightweight

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoLightweight from a JSON string
pet_info_lightweight_instance = PetInfoLightweight.from_json(json)
# print the JSON string representation of the object
print(PetInfoLightweight.to_json())

# convert the object into a dict
pet_info_lightweight_dict = pet_info_lightweight_instance.to_dict()
# create an instance of PetInfoLightweight from a dict
pet_info_lightweight_from_dict = PetInfoLightweight.from_dict(pet_info_lightweight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


