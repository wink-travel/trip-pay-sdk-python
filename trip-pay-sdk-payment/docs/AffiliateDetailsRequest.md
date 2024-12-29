# AffiliateDetailsRequest

Request for affiliate details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Account identifier type | 
**identifier** | **str** | Account identifier | 

## Example

```python
from trip_pay_payment.models.affiliate_details_request import AffiliateDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateDetailsRequest from a JSON string
affiliate_details_request_instance = AffiliateDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(AffiliateDetailsRequest.to_json())

# convert the object into a dict
affiliate_details_request_dict = affiliate_details_request_instance.to_dict()
# create an instance of AffiliateDetailsRequest from a dict
affiliate_details_request_from_dict = AffiliateDetailsRequest.from_dict(affiliate_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


