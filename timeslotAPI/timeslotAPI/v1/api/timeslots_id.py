# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json

from flask import request, g

from . import Resource
from .. import schemas


class TimeslotsId(Resource):

    @staticmethod
    def get(id):
        requestedID = id
        with open('timeslots.json', 'r') as jsonFile:
            timeslots = json.loads(jsonFile.read())
        for timeslot in timeslots:
            if str(timeslot['id']) == requestedID:
                return timeslot, 200, None
        return {}, 404, None

    def patch(self, id):
        print(g.json)

        return {'date': 'something', 'dentist': 'something', 'startTime': 'something', 'status': 'something'}, 200, None