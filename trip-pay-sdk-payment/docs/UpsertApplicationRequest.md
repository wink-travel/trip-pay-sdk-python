# UpsertApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the application. | 
**entity** | [**ManagingEntity**](ManagingEntity.md) |  | 
**redirect_uris** | **List[str]** |  | 

## Example

```python
from trip_pay_payment.models.upsert_application_request import UpsertApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertApplicationRequest from a JSON string
upsert_application_request_instance = UpsertApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertApplicationRequest.to_json())

# convert the object into a dict
upsert_application_request_dict = upsert_application_request_instance.to_dict()
# create an instance of UpsertApplicationRequest from a dict
upsert_application_request_from_dict = UpsertApplicationRequest.from_dict(upsert_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


