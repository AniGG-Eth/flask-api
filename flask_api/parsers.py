import json

from werkzeug.formparser import MultiPartParser as WerkzeugMultiPartParser
from werkzeug.formparser import default_stream_factory

from flask_api.helpers import url_decode_stream
from flask_api import exceptions


class BaseParser:
    media_type = None
    handles_file_uploads = False  # If set then 'request.files' will be populated.
    handles_form_data = False  # If set then 'request.form' will be populated.

    def parse(self, stream, media_type, **options):
        pass


class JSONParser(BaseParser):
    media_type = "application/json"

    def parse(self, stream, media_type, **options):
        pass


class MultiPartParser(BaseParser):
    media_type = "multipart/form-data"
    handles_file_uploads = True
    handles_form_data = True

    def parse(self, stream, media_type, **options):
        pass


class URLEncodedParser(BaseParser):
    media_type = "application/x-www-form-urlencoded"
    handles_form_data = True

    def parse(self, stream, media_type, **options):
        pass
