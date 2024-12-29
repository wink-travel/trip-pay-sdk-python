# ExternalEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document identifier | [optional] [readonly] 
**created_date** | **datetime** | Datetime this record was first created | [optional] [readonly] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] [readonly] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] [readonly] 
**instant** | **datetime** | Date to attach TTL. Self-deletes after 3 days. | 
**sender** | **str** | The sender of the request payload | 
**receiver** | **str** | The receiver of the request payload | 
**type** | **str** | The type of request payload | 
**entity_identifier** | **str** | The ID of the remote event to query against | 
**request** | **str** | Request sent to external endpoint | [optional] 
**response** | **str** | Response from external endpoint | [optional] 
**media_type** | **str** | The content MIME type | 
**http_response_code** | **int** | Response status code | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from trip_pay_payment.models.external_event import ExternalEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalEvent from a JSON string
external_event_instance = ExternalEvent.from_json(json)
# print the JSON string representation of the object
print(ExternalEvent.to_json())

# convert the object into a dict
external_event_dict = external_event_instance.to_dict()
# create an instance of ExternalEvent from a dict
external_event_from_dict = ExternalEvent.from_dict(external_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


