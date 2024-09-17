# CurrencyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If the currency is enabled | [optional] 
**default** | **bool** | If the currency must be the default for the user. You can only submit TRUE. Submitting FALSE will not drop this currency as the default currency, because then the system would be without one. | [optional] 
**code** | **str** | The currency code | [optional] 
**name** | **str** | The currency name | [optional] 
**symbol** | **str** | The currency symbol | [optional] 
**decimal_places** | **int** | How many decimals to use when displaying this currency. Between 0 and 16. | [optional] 

## Example

```python
from firefly_client.models.currency_update import CurrencyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyUpdate from a JSON string
currency_update_instance = CurrencyUpdate.from_json(json)
# print the JSON string representation of the object
print(CurrencyUpdate.to_json())

# convert the object into a dict
currency_update_dict = currency_update_instance.to_dict()
# create an instance of CurrencyUpdate from a dict
currency_update_from_dict = CurrencyUpdate.from_dict(currency_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


