import re
import sys
from itertools import chain
from flask import Blueprint, Flask, request
from werkzeug.exceptions import HTTPException
from flask_api.compat import is_flask_legacy
from flask_api.exceptions import APIException
from flask_api.request import APIRequest
from flask_api.response import APIResponse
from flask_api.settings import APISettings
from flask_api.status import HTTP_204_NO_CONTENT
api_resources = Blueprint('flask-api', __name__, url_prefix='/flask-api', template_folder='templates', static_folder='static')

def urlize_quoted_links(content):
    pass

class FlaskAPI(Flask):
    request_class = APIRequest
    response_class = APIResponse

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_settings = APISettings(self.config)
        self.register_blueprint(api_resources)
        self.jinja_env.filters['urlize_quoted_links'] = urlize_quoted_links

    def preprocess_request(self):
        pass

    def make_response(self, rv):
        """
        We override this so that we can additionally handle
        list and dict types by default.
        """
        pass

    def handle_user_exception(self, e):
        """
        We override the default behavior in order to deal with APIException.
        """
        pass

    def handle_api_exception(self, exc):
        pass

    def create_url_adapter(self, request):
        """
        We need to override the default behavior slightly here,
        to ensure the any method-based routing takes account of
        any method overloading, so that eg PUT requests from the
        browsable API are routed to the correct view.
        """
        pass
