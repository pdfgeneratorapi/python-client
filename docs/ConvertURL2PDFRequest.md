# ConvertURL2PDFRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Public URL | [optional] 
**paper_size** | **str** | PDF page size | [optional] [default to 'a4']
**orientation** | **str** |  | [optional] [default to 'portrait']
**output** | **str** | Output | [optional] [default to 'base64']
**filename** | **str** | Document name | [optional] 
**wait_for_css** | **str** | CSS selector of an element to wait for before the page is printed; see &#x60;wait_for_css_state&#x60; | [optional] 
**wait_for_css_state** | **str** | How &#x60;wait_for_css&#x60; matches. &#x60;present&#x60; waits until the element exists, even if it is empty or hidden (e.g. a &#x60;&lt;div id&#x3D;\&quot;report-ready\&quot;&gt;&lt;/div&gt;&#x60; marker); &#x60;visible&#x60; waits until it is also visible with a non-empty size (e.g. a chart that appears when data has loaded). | [optional] [default to 'present']
**wait_for_js** | **str** | JavaScript expression evaluated in the page every 100ms; the page is printed once it is truthy. Promises are awaited, and an expression that throws counts as not ready yet. | [optional] 
**wait_timeout** | **int** | Seconds to wait for &#x60;wait_for_css&#x60; / &#x60;wait_for_js&#x60; before applying &#x60;on_wait_timeout&#x60; | [optional] [default to 30]
**on_wait_timeout** | **str** | What to do when the wait signal is not met within &#x60;wait_timeout&#x60;. &#x60;error&#x60; returns a 422 response; &#x60;print&#x60; prints the page as it is. | [optional] [default to 'error']

## Example

```python
from pdf_generator_api_client.models.convert_url2_pdf_request import ConvertURL2PDFRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertURL2PDFRequest from a JSON string
convert_url2_pdf_request_instance = ConvertURL2PDFRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertURL2PDFRequest.to_json())

# convert the object into a dict
convert_url2_pdf_request_dict = convert_url2_pdf_request_instance.to_dict()
# create an instance of ConvertURL2PDFRequest from a dict
convert_url2_pdf_request_from_dict = ConvertURL2PDFRequest.from_dict(convert_url2_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


