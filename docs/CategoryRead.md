# CategoryRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**Category**](Category.md) |  | 

## Example

```python
from firefly_client.models.category_read import CategoryRead

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryRead from a JSON string
category_read_instance = CategoryRead.from_json(json)
# print the JSON string representation of the object
print(CategoryRead.to_json())

# convert the object into a dict
category_read_dict = category_read_instance.to_dict()
# create an instance of CategoryRead from a dict
category_read_from_dict = CategoryRead.from_dict(category_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


