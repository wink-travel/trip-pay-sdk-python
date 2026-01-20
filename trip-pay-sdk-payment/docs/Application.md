# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier. | 
**user_identifier** | **UUID** | Unique user record identifier | 
**owner_identifier** | **UUID** | Unique owner record identifier | 
**owner_name** | **str** | Name of company owner. | 
**name** | **str** | Name of this customization application. The first customization for every integrator will have the same name as its company name. | 
**redirect_uris** | **List[str]** | Where to redirect after web components successfully authenticate. For OAuth2 purposes. | [optional] 
**client_id** | **str** | Client identifier used to authenticate an Oauth2 or web component request. | 

## Example

```python
from trip_pay_payment.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


