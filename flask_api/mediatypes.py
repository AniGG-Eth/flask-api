class MediaType:

    def __init__(self, media_type):
        (self.main_type, self.sub_type, self.params) = self._parse(media_type)

    @property
    def full_type(self):
        pass

    @property
    def precedence(self):
        """
        Precedence is determined by how specific a media type is:

        3. 'type/subtype; param=val'
        2. 'type/subtype'
        1. 'type/*'
        0. '*/*'
        """
        pass

    def satisfies(self, other):
        """
        Returns `True` if this media type is a superset of `other`.
        Some examples of cases where this holds true:

        'application/json; version=1.0' >= 'application/json; version=1.0'
        'application/json'              >= 'application/json; indent=4'
        'text/*'                        >= 'text/plain'
        '*/*'                           >= 'text/plain'
        """
        pass

    def _parse(self, media_type):
        """
        Parse a media type string, like "application/json; indent=4" into a
        three-tuple, like: ('application', 'json', {'indent': 4})
        """
        pass

    def __repr__(self):
        return "<%s '%s'>" % (self.__class__.__name__, str(self))

    def __str__(self):
        """
        Return a canonical string representing the media type.
        Note that this ensures the params are sorted.
        """
        if self.params:
            params_str = ', '.join(['%s="%s"' % (key, val) for (key, val) in sorted(self.params.items())])
            return self.full_type + '; ' + params_str
        return self.full_type

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.full_type == other.full_type and self.params == other.params

def parse_accept_header(accept):
    """
    Parses the value of a clients accept header, and returns a list of sets
    of media types it included, ordered by precedence.

    For example, 'application/json, application/xml, */*' would return:

    [
        set([<MediaType "application/xml">, <MediaType "application/json">]),
        set([<MediaType "*/*">])
    ]
    """
    pass
