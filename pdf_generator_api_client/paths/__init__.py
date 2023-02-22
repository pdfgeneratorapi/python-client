# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pdf_generator_api_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    TEMPLATES = "/templates"
    TEMPLATES_TEMPLATE_ID = "/templates/{templateId}"
    TEMPLATES_TEMPLATE_ID_COPY = "/templates/{templateId}/copy"
    TEMPLATES_TEMPLATE_ID_EDITOR = "/templates/{templateId}/editor"
    TEMPLATES_TEMPLATE_ID_OUTPUT = "/templates/{templateId}/output"
    TEMPLATES_OUTPUT = "/templates/output"
    WORKSPACES_WORKSPACE_ID = "/workspaces/{workspaceId}"
