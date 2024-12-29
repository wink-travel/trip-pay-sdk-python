# PetInfoDto

Array of customer's pets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from trip_pay_payment.models.pet_info_dto import PetInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoDto from a JSON string
pet_info_dto_instance = PetInfoDto.from_json(json)
# print the JSON string representation of the object
print(PetInfoDto.to_json())

# convert the object into a dict
pet_info_dto_dict = pet_info_dto_instance.to_dict()
# create an instance of PetInfoDto from a dict
pet_info_dto_from_dict = PetInfoDto.from_dict(pet_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


