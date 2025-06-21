# UpdateApplicationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier. | 
**name** | **str** | Name of the application. | [optional] 
**entity** | [**ManagingEntity**](ManagingEntity.md) | Name of the application. | 
**redirect_uris** | **List[object]** |  | [optional] 

## Example

```python
from trip_pay_payment.models.update_application_response import UpdateApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationResponse from a JSON string
update_application_response_instance = UpdateApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicationResponse.to_json())

# convert the object into a dict
update_application_response_dict = update_application_response_instance.to_dict()
# create an instance of UpdateApplicationResponse from a dict
update_application_response_from_dict = UpdateApplicationResponse.from_dict(update_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


