# UpsertImageRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**SimpleMultimediaAuthenticatedEntity**](SimpleMultimediaAuthenticatedEntity.md) | Customize account with a custom image / profile picture. | [optional] 

## Example

```python
from trip_pay_payment.models.upsert_image_request_authenticated_entity import UpsertImageRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertImageRequestAuthenticatedEntity from a JSON string
upsert_image_request_authenticated_entity_instance = UpsertImageRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UpsertImageRequestAuthenticatedEntity.to_json())

# convert the object into a dict
upsert_image_request_authenticated_entity_dict = upsert_image_request_authenticated_entity_instance.to_dict()
# create an instance of UpsertImageRequestAuthenticatedEntity from a dict
upsert_image_request_authenticated_entity_from_dict = UpsertImageRequestAuthenticatedEntity.from_dict(upsert_image_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


