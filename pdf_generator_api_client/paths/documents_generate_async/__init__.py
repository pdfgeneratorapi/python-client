# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pdf_generator_api_client.paths.documents_generate_async import Api

from pdf_generator_api_client.paths import PathValues

path = PathValues.DOCUMENTS_GENERATE_ASYNC