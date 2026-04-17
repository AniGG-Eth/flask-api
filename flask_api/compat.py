from flask import __version__ as flask_version
try:
    import markdown
    from markdown.extensions.toc import TocExtension

    def apply_markdown(text):
        """
        Simple wrapper around :func:`markdown.markdown` to set the base level
        of '#' style headers to <h2>.
        """
        pass
except ImportError:
    apply_markdown = None

def is_flask_legacy():
    pass
