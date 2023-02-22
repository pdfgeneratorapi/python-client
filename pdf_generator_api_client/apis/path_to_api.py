import typing_extensions

from pdf_generator_api_client.paths import PathValues
from pdf_generator_api_client.apis.paths.templates import Templates
from pdf_generator_api_client.apis.paths.templates_template_id import TemplatesTemplateId
from pdf_generator_api_client.apis.paths.templates_template_id_copy import TemplatesTemplateIdCopy
from pdf_generator_api_client.apis.paths.templates_template_id_editor import TemplatesTemplateIdEditor
from pdf_generator_api_client.apis.paths.templates_template_id_output import TemplatesTemplateIdOutput
from pdf_generator_api_client.apis.paths.templates_output import TemplatesOutput
from pdf_generator_api_client.apis.paths.workspaces_workspace_id import WorkspacesWorkspaceId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_TEMPLATE_ID: TemplatesTemplateId,
        PathValues.TEMPLATES_TEMPLATE_ID_COPY: TemplatesTemplateIdCopy,
        PathValues.TEMPLATES_TEMPLATE_ID_EDITOR: TemplatesTemplateIdEditor,
        PathValues.TEMPLATES_TEMPLATE_ID_OUTPUT: TemplatesTemplateIdOutput,
        PathValues.TEMPLATES_OUTPUT: TemplatesOutput,
        PathValues.WORKSPACES_WORKSPACE_ID: WorkspacesWorkspaceId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_TEMPLATE_ID: TemplatesTemplateId,
        PathValues.TEMPLATES_TEMPLATE_ID_COPY: TemplatesTemplateIdCopy,
        PathValues.TEMPLATES_TEMPLATE_ID_EDITOR: TemplatesTemplateIdEditor,
        PathValues.TEMPLATES_TEMPLATE_ID_OUTPUT: TemplatesTemplateIdOutput,
        PathValues.TEMPLATES_OUTPUT: TemplatesOutput,
        PathValues.WORKSPACES_WORKSPACE_ID: WorkspacesWorkspaceId,
    }
)
