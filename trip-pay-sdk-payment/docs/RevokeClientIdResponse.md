# RevokeClientIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier. | 
**client_id** | **str** | Client identifier used to authenticate an Oauth2 or web component request. | 
**secret_key** | **str** | Password used to authenticate an Oauth2 request. | 

## Example

```python
from trip_pay_payment.models.revoke_client_id_response import RevokeClientIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeClientIdResponse from a JSON string
revoke_client_id_response_instance = RevokeClientIdResponse.from_json(json)
# print the JSON string representation of the object
print(RevokeClientIdResponse.to_json())

# convert the object into a dict
revoke_client_id_response_dict = revoke_client_id_response_instance.to_dict()
# create an instance of RevokeClientIdResponse from a dict
revoke_client_id_response_from_dict = RevokeClientIdResponse.from_dict(revoke_client_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


