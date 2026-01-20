# ManagingEntityAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **str** | User owner. | 
**owner_identifier** | **str** | The App owner that created this record. | 
**managers** | [**List[ManagingEntityManagerPayment]**](ManagingEntityManagerPayment.md) |  | 
**managed_by** | [**ManagedByEntity**](ManagedByEntity.md) | If another company entity is managing this property, on behalf of the property, it can be specified here and the managing entity would be applicable a management fee on every booking. | [optional] 
**owner_type** | **str** | Type of entity this is. | 
**type** | **str** | Type of sales channel | 
**name** | **str** | Text representation of the value. | 
**description** | **str** | Short company / person description. | 
**legal_name** | **str** | Legal name of entity if other than name | 
**url_name** | **str** | Unique url-friendly slug to identify property | 
**unique_id** | **str** | Event shorter name | 
**account_email** | **str** | Account email is where we will send KYC documents and other account specific mailings | 
**account_phone_number** | **str** | Account phone number is mostly used for KYC purchases | 
**url** | **str** | AffiliateAccount website. If private person with no personal website, link to main social network account. | 
**currency_code** | **str** | Account&#39;s main currency. | 
**status** | **str** | Status of entity. | 
**city** | [**GeoNameLightweightPayment**](GeoNameLightweightPayment.md) | City location | 
**address** | [**SimpleAddress**](SimpleAddress.md) | Account address. Usually the business address | [optional] 
**plan** | [**ManagingEntityProvisionPayment**](ManagingEntityProvisionPayment.md) | Optional subscription for this entity. | [optional] 
**profile_picture** | [**SimpleMultimedia**](SimpleMultimedia.md) | Customize account with a custom profile picture. | [optional] 
**logo** | [**SimpleMultimediaPayment**](SimpleMultimediaPayment.md) | Entity logo | [optional] 
**marketing_optin_allowed** | **bool** | Account agrees to let us use theor logo and images for marketing purposes (with proper credits). | [optional] 
**place_id** | **str** | Optional Google placeId for properties with a Google Business account. | [optional] 

## Example

```python
from trip_pay_payment.models.managing_entity_authenticated_entity import ManagingEntityAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ManagingEntityAuthenticatedEntity from a JSON string
managing_entity_authenticated_entity_instance = ManagingEntityAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ManagingEntityAuthenticatedEntity.to_json())

# convert the object into a dict
managing_entity_authenticated_entity_dict = managing_entity_authenticated_entity_instance.to_dict()
# create an instance of ManagingEntityAuthenticatedEntity from a dict
managing_entity_authenticated_entity_from_dict = ManagingEntityAuthenticatedEntity.from_dict(managing_entity_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


