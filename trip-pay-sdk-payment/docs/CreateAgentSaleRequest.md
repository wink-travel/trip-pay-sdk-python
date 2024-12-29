# CreateAgentSaleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | [**PayableContractRequest**](PayableContractRequest.md) |  | 

## Example

```python
from trip_pay_payment.models.create_agent_sale_request import CreateAgentSaleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentSaleRequest from a JSON string
create_agent_sale_request_instance = CreateAgentSaleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAgentSaleRequest.to_json())

# convert the object into a dict
create_agent_sale_request_dict = create_agent_sale_request_instance.to_dict()
# create an instance of CreateAgentSaleRequest from a dict
create_agent_sale_request_from_dict = CreateAgentSaleRequest.from_dict(create_agent_sale_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


