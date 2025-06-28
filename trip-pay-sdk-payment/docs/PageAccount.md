# PageAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Account]**](Account.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from trip_pay_payment.models.page_account import PageAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PageAccount from a JSON string
page_account_instance = PageAccount.from_json(json)
# print the JSON string representation of the object
print(PageAccount.to_json())

# convert the object into a dict
page_account_dict = page_account_instance.to_dict()
# create an instance of PageAccount from a dict
page_account_from_dict = PageAccount.from_dict(page_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


