# DisplayModeParam

How a PDF viewer opens the document (optional). Applies to PDF output. Any value left out keeps its default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zoom** | **str** | Initial zoom * &#x60;fullpage&#x60; - Fits the whole page in the window * &#x60;fullwidth&#x60; - Fits the page width to the window * &#x60;real&#x60; - Actual size (100%) * &#x60;default&#x60; - Leaves the zoom to the viewer. The PDF gets no open action, which some e-invoice validators require  | [optional] [default to 'fullwidth']
**layout** | **str** | Page layout * &#x60;SinglePage&#x60; - One page at a time * &#x60;OneColumn&#x60; - Pages in one continuous column * &#x60;TwoColumnLeft&#x60; - Pages in two columns, odd-numbered pages on the left * &#x60;TwoColumnRight&#x60; - Pages in two columns, odd-numbered pages on the right  | [optional] [default to 'SinglePage']
**mode** | **str** | Panel shown when the document opens * &#x60;UseNone&#x60; - No panel * &#x60;UseOutlines&#x60; - Document outline (bookmarks) * &#x60;UseThumbs&#x60; - Page thumbnails * &#x60;FullScreen&#x60; - Full-screen mode, without menu bar or window controls  | [optional] [default to 'UseNone']

## Example

```python
from pdf_generator_api_client.models.display_mode_param import DisplayModeParam

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayModeParam from a JSON string
display_mode_param_instance = DisplayModeParam.from_json(json)
# print the JSON string representation of the object
print(DisplayModeParam.to_json())

# convert the object into a dict
display_mode_param_dict = display_mode_param_instance.to_dict()
# create an instance of DisplayModeParam from a dict
display_mode_param_from_dict = DisplayModeParam.from_dict(display_mode_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


