# SimpleMultimediaAuthenticatedEntity

Multimedia that contains less information than Multimedia object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multimedia_identifier** | **UUID** | Document identifier | 
**identifier** | **str** | Use this identifier to communicate with Cloudinary. | 
**type** | **str** | Whether Cloudinary media is a VIDEO or IMAGE. | 
**source** | **str** | Currently ONLY using Cloudinary to store all image / video assets. | [default to 'CLOUDINARY']
**sort** | **int** | Sort allows you to control how you want to sort this record in a list of media records. | [default to 999]
**angle** | **str** | Media angle | [optional] 
**width** | **int** | Media width in pixels. | 
**height** | **int** | Media height in pixels. | 
**published** | **bool** | Instead of deleting the media, choose to un-publish it instead for later re-use. Could be you keep seasonal images of the property. | [optional] [default to False]
**category** | **str** | Supported OTA specification &#x60;PIC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**descriptions** | [**List[SimpleDescription]**](SimpleDescription.md) | Localized media captions to give user some context about where this media was taken. | [optional] 
**lifestyle_type** | **str** | Associate this media with a specific lifestyle type. A user searching and filtering inventory based on lifestyles can be shown relevant media first. | [optional] 
**attribution** | [**List[MediaAuthorAttribution]**](MediaAuthorAttribution.md) | Whether image has attribution properties | [optional] 
**is_landscape** | **bool** | True if media width is greater or equal to height | [optional] 

## Example

```python
from trip_pay_payment.models.simple_multimedia_authenticated_entity import SimpleMultimediaAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleMultimediaAuthenticatedEntity from a JSON string
simple_multimedia_authenticated_entity_instance = SimpleMultimediaAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SimpleMultimediaAuthenticatedEntity.to_json())

# convert the object into a dict
simple_multimedia_authenticated_entity_dict = simple_multimedia_authenticated_entity_instance.to_dict()
# create an instance of SimpleMultimediaAuthenticatedEntity from a dict
simple_multimedia_authenticated_entity_from_dict = SimpleMultimediaAuthenticatedEntity.from_dict(simple_multimedia_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


