import io

from flask import Request
from werkzeug.datastructures import MultiDict
from werkzeug.wsgi import get_content_length

from flask_api.helpers import url_decode_stream
from flask_api.negotiation import DefaultNegotiation
from flask_api.settings import default_settings


class APIRequest(Request):
    parser_classes = default_settings.DEFAULT_PARSERS
    renderer_classes = default_settings.DEFAULT_RENDERERS
    negotiator_class = DefaultNegotiation
    empty_data_class = MultiDict

    # Request parsing...

    @property
    def data(self):
        pass

    @property
    def form(self):
        pass

    @property
    def files(self):
        pass

    def _parse(self):
        """
        Parse the body of the request, using whichever parser satisfies the
        client 'Content-Type' header.
        """
        pass

    def _get_parser_options(self):
        """
        Any additional information to pass to the parser.
        """
        pass

    def _set_empty_data(self):
        """
        If the request does not contain data then return an empty representation.
        """
        pass

    # Content negotiation...

    @property
    def accepted_renderer(self):
        pass

    @property
    def accepted_media_type(self):
        pass

    def _perform_content_negotiation(self):
        """
        Determine which of the available renderers should be used for
        rendering the response content, based on the client 'Accept' header.
        """
        pass

    # Method and content type overloading.

    @property
    def method(self):
        pass

    @method.setter
    def method(self, value):
        pass

    @property
    def content_type(self):
        pass

    @property
    def content_length(self):
        pass

    @property
    def stream(self):
        pass

    def _perform_method_overloading(self):
        """
        Perform method and content type overloading.

        Provides support for browser PUT, PATCH, DELETE & other requests,
        by specifying a '_method' form field.

        Also provides support for browser non-form requests (eg JSON),
        by specifying '_content' and '_content_type' form fields.
        """
        pass

    # Misc...

    @property
    def full_path(self):
        """
        Werzueg's full_path implementation always appends '?', even when the
        query string is empty.  Let's fix that.
        """
        pass

    # @property
    # def auth(self):
    #     if not has_attribute(self, '_auth'):
    #         self._authenticate()
    #     return self._auth

    # def _authenticate(self):
    #     for authentication_class in self.authentication_classes:
    #         authenticator = authentication_class()
    #         try:
    #             auth = authenticator.authenticate(self)
    #         except exceptions.APIException:
    #             self._not_authenticated()
    #             raise

    #         if not auth is None:
    #             self._authenticator = authenticator
    #             self._auth = auth
    #             return

    #     self._not_authenticated()

    # def _not_authenticated(self):
    #     self._authenticator = None
    #     self._auth = None
