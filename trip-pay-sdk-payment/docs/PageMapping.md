# PageMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Mapping]**](Mapping.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectPayment**](PageableObjectPayment.md) |  | [optional] 
**sort** | [**SortObjectPayment**](SortObjectPayment.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from trip_pay_payment.models.page_mapping import PageMapping

# TODO update the JSON string below
json = "{}"
# create an instance of PageMapping from a JSON string
page_mapping_instance = PageMapping.from_json(json)
# print the JSON string representation of the object
print(PageMapping.to_json())

# convert the object into a dict
page_mapping_dict = page_mapping_instance.to_dict()
# create an instance of PageMapping from a dict
page_mapping_from_dict = PageMapping.from_dict(page_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


