"""Exceptions for the whole package."""


class RowNotFound(Exception):
    """The DwC-A Row cannot be found."""


class InvalidArchive(Exception):
    """The archive appears to be invalid."""


class BadlyFormedMetaXml(Exception):
    """The meta.xml appears to be invalid."""


class InvalidSimpleArchive(InvalidArchive):
    """The simple archive appears to be invalid."""


class NotADataFile(Exception):
    """The file doesn't exist or is not a data file."""
