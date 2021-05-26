
from .keywords import ArchiveKeywords
from .version import VERSION

_version_ = VERSION


class ArchiveLibrary(ArchiveKeywords):
    """ ArchiveLibrary is a Robot Framework keyword library to
    handle ZIP and possibly other archive formats.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
