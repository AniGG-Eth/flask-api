import pydoc
import re

import flask
from flask import current_app, render_template, request

from flask_api.compat import apply_markdown
from flask_api.mediatypes import MediaType


def dedent(content):
    """
    Remove leading indent from a block of text.
    Used when generating descriptions from docstrings.

    Note that python's `textwrap.dedent` doesn't quite cut it,
    as it fails to dedent multiline docstrings that include
    unindented text on the initial line.
    """
    pass


def convert_to_title(name):
    pass


class BaseRenderer:
    media_type = None
    charset = "utf-8"
    handles_empty_responses = False

    def render(self, data, media_type, **options):
        pass


class JSONRenderer(BaseRenderer):
    media_type = "application/json"
    charset = None

    def render(self, data, media_type, **options):
        # Requested indentation may be set in the Accept header.
        pass


class HTMLRenderer:
    media_type = "text/html"
    charset = "utf-8"

    def render(self, data, media_type, **options):
        pass


class BrowsableAPIRenderer(BaseRenderer):
    media_type = "text/html"
    handles_empty_responses = True
    template = "base.html"

    def render(self, data, media_type, **options):
        # Render the content as it would have been if the client
        # had requested 'Accept: */*'.
        pass

    @staticmethod
    def _html_escape(text):
        pass
