# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json

from flask import request, g

from . import Resource
from .. import schemas


class Timeslots(Resource):

    @staticmethod
    def get():
        POSSIBLE_PARAMETERS = ['dentist', 'date', 'startTime', 'status']
        with open('timeslots.json', 'r') as jsonFile:
            timeslots = json.loads(jsonFile.read())
        matchedTimeslots = []
        for timeslot in timeslots:
            isMatched = True
            for parameter in POSSIBLE_PARAMETERS:
                if g.args.get(parameter) and timeslot[parameter] != g.args.get(parameter):
                    isMatched = False
                    break
            if isMatched:
                matchedTimeslots.append(timeslot)
        return matchedTimeslots, 200, None
