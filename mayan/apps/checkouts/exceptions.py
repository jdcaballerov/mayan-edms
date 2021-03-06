from __future__ import unicode_literals

from django.utils.translation import ugettext


class DocumentNotCheckedOut(Exception):
    """
    Raised when trying to checkin a document that is not checkedout
    """
    pass


class DocumentAlreadyCheckedOut(Exception):
    """
    Raised when trying to checkout an already checkedout document
    """
    def __unicode__(self):
        return ugettext('Document already checked out.')
