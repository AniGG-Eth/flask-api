from flask import request

from flask_api import exceptions
from flask_api.mediatypes import MediaType, parse_accept_header


class BaseNegotiation:
    def select_parser(self, parsers):
        pass

    def select_renderer(self, renderers):
        pass


class DefaultNegotiation(BaseNegotiation):
    def select_parser(self, parsers):
        """
        Determine which parser to use for parsing the request body.
        Returns a two-tuple of (parser, content type).
        """
        pass

    def select_renderer(self, renderers):
        """
        Determine which renderer to use for rendering the response body.
        Returns a two-tuple of (renderer, content type).
        """
        pass
