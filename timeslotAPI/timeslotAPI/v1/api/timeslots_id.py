# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class TimeslotsId(Resource):

    def get(self, id):

        return {'date': 'something', 'dentist': 'something', 'startTime': 'something', 'status': 'something'}, 200, None

    def patch(self, id):
        print(g.json)

        return {'date': 'something', 'dentist': 'something', 'startTime': 'something', 'status': 'something'}, 200, None