# AccountStatusResponse

Shows where the account is in terms of onboarding and readiness

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **UUID** | Local account identifier. | 
**status** | **str** | Account status shows if it&#39;s approved | 
**task_list** | [**List[AccountStatusEntry]**](AccountStatusEntry.md) |  | [optional] 

## Example

```python
from trip_pay_payment.models.account_status_response import AccountStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatusResponse from a JSON string
account_status_response_instance = AccountStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AccountStatusResponse.to_json())

# convert the object into a dict
account_status_response_dict = account_status_response_instance.to_dict()
# create an instance of AccountStatusResponse from a dict
account_status_response_from_dict = AccountStatusResponse.from_dict(account_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


