import importlib


def perform_imports(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    pass


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    pass


class APISettings:
    def __init__(self, user_config=None):
        self.user_config = user_config or {}

    @property
    def DEFAULT_PARSERS(self):
        pass

    @property
    def DEFAULT_RENDERERS(self):
        pass


default_settings = APISettings()
