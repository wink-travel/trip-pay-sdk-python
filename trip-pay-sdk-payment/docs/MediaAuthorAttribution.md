# MediaAuthorAttribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from trip_pay_payment.models.media_author_attribution import MediaAuthorAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAuthorAttribution from a JSON string
media_author_attribution_instance = MediaAuthorAttribution.from_json(json)
# print the JSON string representation of the object
print(MediaAuthorAttribution.to_json())

# convert the object into a dict
media_author_attribution_dict = media_author_attribution_instance.to_dict()
# create an instance of MediaAuthorAttribution from a dict
media_author_attribution_from_dict = MediaAuthorAttribution.from_dict(media_author_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


