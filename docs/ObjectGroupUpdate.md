# ObjectGroupUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**order** | **int** | Order of the object group | [optional] 

## Example

```python
from firefly_client.models.object_group_update import ObjectGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectGroupUpdate from a JSON string
object_group_update_instance = ObjectGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(ObjectGroupUpdate.to_json())

# convert the object into a dict
object_group_update_dict = object_group_update_instance.to_dict()
# create an instance of ObjectGroupUpdate from a dict
object_group_update_from_dict = ObjectGroupUpdate.from_dict(object_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


