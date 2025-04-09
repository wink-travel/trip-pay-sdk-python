# CountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True if count query worked. | 
**count** | **int** | Number of reviews for this property. | 

## Example

```python
from trip_pay_payment.models.count_response import CountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CountResponse from a JSON string
count_response_instance = CountResponse.from_json(json)
# print the JSON string representation of the object
print(CountResponse.to_json())

# convert the object into a dict
count_response_dict = count_response_instance.to_dict()
# create an instance of CountResponse from a dict
count_response_from_dict = CountResponse.from_dict(count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


