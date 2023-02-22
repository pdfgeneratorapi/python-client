import typing_extensions

from pdf_generator_api_client.apis.tags import TagValues
from pdf_generator_api_client.apis.tags.template_model_api import TemplateModelApi
from pdf_generator_api_client.apis.tags.template_definition_api import TemplateDefinitionApi
from pdf_generator_api_client.apis.tags.component_model_api import ComponentModelApi
from pdf_generator_api_client.apis.tags.workspace_model_api import WorkspaceModelApi
from pdf_generator_api_client.apis.tags.documents_api import DocumentsApi
from pdf_generator_api_client.apis.tags.templates_api import TemplatesApi
from pdf_generator_api_client.apis.tags.workspaces_api import WorkspacesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TEMPLATE_MODEL: TemplateModelApi,
        TagValues.TEMPLATE_DEFINITION: TemplateDefinitionApi,
        TagValues.COMPONENT_MODEL: ComponentModelApi,
        TagValues.WORKSPACE_MODEL: WorkspaceModelApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.WORKSPACES: WorkspacesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TEMPLATE_MODEL: TemplateModelApi,
        TagValues.TEMPLATE_DEFINITION: TemplateDefinitionApi,
        TagValues.COMPONENT_MODEL: ComponentModelApi,
        TagValues.WORKSPACE_MODEL: WorkspaceModelApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.WORKSPACES: WorkspacesApi,
    }
)
