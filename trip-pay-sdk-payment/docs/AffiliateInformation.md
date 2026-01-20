# AffiliateInformation

Affiliate details response contains details about the affiliate facilitating the sale.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_identifier** | **UUID** | Affiliate identifier of entity making the same | [optional] 
**affiliate_name** | **str** | Affiliate name of entity making the same | [optional] 
**affiliate_url** | **str** | Affiliate url of entity making the same | [optional] 

## Example

```python
from trip_pay_payment.models.affiliate_information import AffiliateInformation

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateInformation from a JSON string
affiliate_information_instance = AffiliateInformation.from_json(json)
# print the JSON string representation of the object
print(AffiliateInformation.to_json())

# convert the object into a dict
affiliate_information_dict = affiliate_information_instance.to_dict()
# create an instance of AffiliateInformation from a dict
affiliate_information_from_dict = AffiliateInformation.from_dict(affiliate_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


