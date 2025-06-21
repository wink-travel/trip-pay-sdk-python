# CreateApplicationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier. | 
**owner_identifier** | **str** | Unique owner record identifier | 
**owner_name** | **str** | Name of company owner. | 
**owner_type** | **str** | Type of entity. | 
**name** | **str** | Name of this customization application. The first customization for every integrator will have the same name as its company name. | 
**redirect_uris** | **List[str]** | Where to redirect after web components successfully authenticate. For OAuth2 purposes. | [optional] 
**client_id** | **str** | Client identifier used to authenticate an Oauth2 or web component request. | 
**secret_key** | **str** | Password used to authenticate an Oauth2 request. | 

## Example

```python
from trip_pay_payment.models.create_application_response import CreateApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationResponse from a JSON string
create_application_response_instance = CreateApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationResponse.to_json())

# convert the object into a dict
create_application_response_dict = create_application_response_instance.to_dict()
# create an instance of CreateApplicationResponse from a dict
create_application_response_from_dict = CreateApplicationResponse.from_dict(create_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


