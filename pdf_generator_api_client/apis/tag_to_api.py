import typing_extensions

from pdf_generator_api_client.apis.tags import TagValues
from pdf_generator_api_client.apis.tags.conversion_api import ConversionApi
from pdf_generator_api_client.apis.tags.documents_api import DocumentsApi
from pdf_generator_api_client.apis.tags.templates_api import TemplatesApi
from pdf_generator_api_client.apis.tags.workspaces_api import WorkspacesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CONVERSION: ConversionApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.WORKSPACES: WorkspacesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CONVERSION: ConversionApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.WORKSPACES: WorkspacesApi,
    }
)
