# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pdf_generator_api_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    TEMPLATES = "/templates"
    TEMPLATES_TEMPLATE_ID = "/templates/{templateId}"
    TEMPLATES_TEMPLATE_ID_DATA = "/templates/{templateId}/data"
    TEMPLATES_TEMPLATE_ID_COPY = "/templates/{templateId}/copy"
    TEMPLATES_TEMPLATE_ID_EDITOR = "/templates/{templateId}/editor"
    DOCUMENTS = "/documents"
    DOCUMENTS_GENERATE = "/documents/generate"
    DOCUMENTS_GENERATE_ASYNC = "/documents/generate/async"
    DOCUMENTS_GENERATE_BATCH = "/documents/generate/batch"
    DOCUMENTS_GENERATE_BATCH_ASYNC = "/documents/generate/batch/async"
    WORKSPACES = "/workspaces"
    WORKSPACES_WORKSPACE_IDENTIFIER = "/workspaces/{workspaceIdentifier}"
    CONVERSION_HTML2PDF = "/conversion/html2pdf"
    CONVERSION_URL2PDF = "/conversion/url2pdf"
