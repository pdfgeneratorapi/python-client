# Font


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The value of a component&#39;s &#x60;fontFamily&#x60; for this font | 
**name** | **str** | Font name, as the editor shows it | 
**parent** | **str** | The &#x60;id&#x60; of the font this one is grouped under, such as another weight of the same family | 
**styles** | **List[str]** | The styles the font has glyphs of its own for. Text in another style is drawn with the regular glyphs. | 
**blocks** | **Dict[str, int]** | The Unicode blocks the font has at least half of the characters of, with the share it has in percent. 100 means every character of the block. | 

## Example

```python
from pdf_generator_api_client.models.font import Font

# TODO update the JSON string below
json = "{}"
# create an instance of Font from a JSON string
font_instance = Font.from_json(json)
# print the JSON string representation of the object
print(Font.to_json())

# convert the object into a dict
font_dict = font_instance.to_dict()
# create an instance of Font from a dict
font_from_dict = Font.from_dict(font_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


