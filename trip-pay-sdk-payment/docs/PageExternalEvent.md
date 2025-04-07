# PageExternalEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ExternalEvent]**](ExternalEvent.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from trip_pay_payment.models.page_external_event import PageExternalEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PageExternalEvent from a JSON string
page_external_event_instance = PageExternalEvent.from_json(json)
# print the JSON string representation of the object
print(PageExternalEvent.to_json())

# convert the object into a dict
page_external_event_dict = page_external_event_instance.to_dict()
# create an instance of PageExternalEvent from a dict
page_external_event_from_dict = PageExternalEvent.from_dict(page_external_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


