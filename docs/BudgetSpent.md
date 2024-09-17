# BudgetSpent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **str** | The amount spent. | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**currency_decimal_places** | **int** | Number of decimals supported by the currency | [optional] 

## Example

```python
from firefly_client.models.budget_spent import BudgetSpent

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSpent from a JSON string
budget_spent_instance = BudgetSpent.from_json(json)
# print the JSON string representation of the object
print(BudgetSpent.to_json())

# convert the object into a dict
budget_spent_dict = budget_spent_instance.to_dict()
# create an instance of BudgetSpent from a dict
budget_spent_from_dict = BudgetSpent.from_dict(budget_spent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


