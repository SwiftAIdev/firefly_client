# Budget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**active** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**order** | **int** |  | [optional] [readonly] 
**auto_budget_type** | [**AutoBudgetType**](AutoBudgetType.md) |  | [optional] 
**auto_budget_currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_amount** | **str** |  | [optional] 
**auto_budget_period** | [**AutoBudgetPeriod**](AutoBudgetPeriod.md) |  | [optional] 
**spent** | [**List[BudgetSpent]**](BudgetSpent.md) | Information on how much was spent in this budget. Is only filled in when the start and end date are submitted. | [optional] [readonly] 

## Example

```python
from firefly_client.models.budget import Budget

# TODO update the JSON string below
json = "{}"
# create an instance of Budget from a JSON string
budget_instance = Budget.from_json(json)
# print the JSON string representation of the object
print(Budget.to_json())

# convert the object into a dict
budget_dict = budget_instance.to_dict()
# create an instance of Budget from a dict
budget_from_dict = Budget.from_dict(budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


