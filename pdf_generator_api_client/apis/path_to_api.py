import typing_extensions

from pdf_generator_api_client.paths import PathValues
from pdf_generator_api_client.apis.paths.templates import Templates
from pdf_generator_api_client.apis.paths.templates_template_id import TemplatesTemplateId
from pdf_generator_api_client.apis.paths.templates_template_id_data import TemplatesTemplateIdData
from pdf_generator_api_client.apis.paths.templates_template_id_copy import TemplatesTemplateIdCopy
from pdf_generator_api_client.apis.paths.templates_template_id_editor import TemplatesTemplateIdEditor
from pdf_generator_api_client.apis.paths.documents import Documents
from pdf_generator_api_client.apis.paths.documents_generate import DocumentsGenerate
from pdf_generator_api_client.apis.paths.documents_generate_async import DocumentsGenerateAsync
from pdf_generator_api_client.apis.paths.documents_generate_batch import DocumentsGenerateBatch
from pdf_generator_api_client.apis.paths.documents_generate_batch_async import DocumentsGenerateBatchAsync
from pdf_generator_api_client.apis.paths.workspaces import Workspaces
from pdf_generator_api_client.apis.paths.workspaces_workspace_identifier import WorkspacesWorkspaceIdentifier
from pdf_generator_api_client.apis.paths.conversion_html2pdf import ConversionHtml2pdf
from pdf_generator_api_client.apis.paths.conversion_url2pdf import ConversionUrl2pdf

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_TEMPLATE_ID: TemplatesTemplateId,
        PathValues.TEMPLATES_TEMPLATE_ID_DATA: TemplatesTemplateIdData,
        PathValues.TEMPLATES_TEMPLATE_ID_COPY: TemplatesTemplateIdCopy,
        PathValues.TEMPLATES_TEMPLATE_ID_EDITOR: TemplatesTemplateIdEditor,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_GENERATE: DocumentsGenerate,
        PathValues.DOCUMENTS_GENERATE_ASYNC: DocumentsGenerateAsync,
        PathValues.DOCUMENTS_GENERATE_BATCH: DocumentsGenerateBatch,
        PathValues.DOCUMENTS_GENERATE_BATCH_ASYNC: DocumentsGenerateBatchAsync,
        PathValues.WORKSPACES: Workspaces,
        PathValues.WORKSPACES_WORKSPACE_IDENTIFIER: WorkspacesWorkspaceIdentifier,
        PathValues.CONVERSION_HTML2PDF: ConversionHtml2pdf,
        PathValues.CONVERSION_URL2PDF: ConversionUrl2pdf,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_TEMPLATE_ID: TemplatesTemplateId,
        PathValues.TEMPLATES_TEMPLATE_ID_DATA: TemplatesTemplateIdData,
        PathValues.TEMPLATES_TEMPLATE_ID_COPY: TemplatesTemplateIdCopy,
        PathValues.TEMPLATES_TEMPLATE_ID_EDITOR: TemplatesTemplateIdEditor,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_GENERATE: DocumentsGenerate,
        PathValues.DOCUMENTS_GENERATE_ASYNC: DocumentsGenerateAsync,
        PathValues.DOCUMENTS_GENERATE_BATCH: DocumentsGenerateBatch,
        PathValues.DOCUMENTS_GENERATE_BATCH_ASYNC: DocumentsGenerateBatchAsync,
        PathValues.WORKSPACES: Workspaces,
        PathValues.WORKSPACES_WORKSPACE_IDENTIFIER: WorkspacesWorkspaceIdentifier,
        PathValues.CONVERSION_HTML2PDF: ConversionHtml2pdf,
        PathValues.CONVERSION_URL2PDF: ConversionUrl2pdf,
    }
)
