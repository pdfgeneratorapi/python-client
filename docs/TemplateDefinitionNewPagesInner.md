# TemplateDefinitionNewPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Page width in units | [optional] 
**height** | **float** | Page height in units | [optional] 
**margins** | [**TemplateDefinitionNewPagesInnerMargins**](TemplateDefinitionNewPagesInnerMargins.md) |  | [optional] 
**border** | **bool** | Stored for older templates. It draws nothing. | [optional] [default to False]
**components** | **List[object]** | The page&#39;s components. The fields of each depend on its cls; the template schema (Get schema endpoint) lists them. | [optional] 
**layout** | [**TemplateDefinitionNewPagesInnerLayout**](TemplateDefinitionNewPagesInnerLayout.md) |  | [optional] 
**conditional_formats** | **List[object]** |  | [optional] 
**background_image** | **str** | The page&#39;s background image: an image URL, a data URI or a {data field} placeholder, PNG, JPEG, GIF or SVG. It is drawn over the background color and under everything else on the page, as backgroundImageFit says. A template with a background PDF does not draw it. Empty or null for none. | [optional] 
**background_color** | **str** | The page&#39;s background color in hex color code, #RRGGBB or #RGB, or with an alpha, #RRGGBBAA, #RGBA or rgba(r, g, b, a); a translucent one is lighter, the white of the paper showing through. It fills every sheet the page runs onto, edge to edge, under everything on it, the background image included; on a sheet of labels it fills each label. A template with a background PDF is not filled. Empty or null for none. | [optional] 
**background_image_fit** | **str** | How the background image covers the page, centred: &#x60;stretch&#x60;, stretched to the page, as when none is set; &#x60;contain&#x60;, fitted inside the page, keeping its proportions; &#x60;cover&#x60;, filling the page, keeping its proportions, with what overflows cut off. Null for stretch. | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_definition_new_pages_inner import TemplateDefinitionNewPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionNewPagesInner from a JSON string
template_definition_new_pages_inner_instance = TemplateDefinitionNewPagesInner.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionNewPagesInner.to_json())

# convert the object into a dict
template_definition_new_pages_inner_dict = template_definition_new_pages_inner_instance.to_dict()
# create an instance of TemplateDefinitionNewPagesInner from a dict
template_definition_new_pages_inner_from_dict = TemplateDefinitionNewPagesInner.from_dict(template_definition_new_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


