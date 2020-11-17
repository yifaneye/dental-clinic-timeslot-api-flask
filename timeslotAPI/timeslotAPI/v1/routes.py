# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .api.timeslots import Timeslots
from .api.timeslots_id import TimeslotsId

routes = [
    dict(resource=Timeslots, urls=['/timeslots'], endpoint='timeslots'),
    dict(resource=TimeslotsId, urls=['/timeslots/<id>'], endpoint='timeslots_id'),
]
