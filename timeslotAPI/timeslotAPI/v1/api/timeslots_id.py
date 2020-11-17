# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json

from flask import request, g

from . import Resource
from .. import schemas


class TimeslotsId(Resource):

    @staticmethod
    def get_all_timeslots():
        with open('timeslots.json', 'r') as jsonFile:
            timeslots = json.loads(jsonFile.read())
        return timeslots

    @staticmethod
    def update_all_timeslots(timeslots):
        with open('timeslots.json', 'w') as jsonFile:
            json.dump(timeslots, jsonFile)
        return

    def get_timeslot_by_id(self, requestedID):
        timeslots = self.get_all_timeslots()
        for timeslot in timeslots:
            if str(timeslot['id']) == requestedID:
                return timeslot
        return None

    def patch_timeslot_by_id(self, requestedID, desiredTimeslot):
        timeslots = self.get_all_timeslots()
        hasMatchedTimeslot = False
        for timeslot in timeslots:
            if str(timeslot['id']) == requestedID:
                hasMatchedTimeslot = True
                timeslot['status'] = desiredTimeslot['status']
                break
        if hasMatchedTimeslot:
            self.update_all_timeslots(timeslots)
            return desiredTimeslot
        return None

    def get(self, id):
        timeslot = self.get_timeslot_by_id(id)
        if timeslot:
            return timeslot, 200, None
        return {}, 404, None

    def patch(self, id):
        updatedTimeslot = self.patch_timeslot_by_id(id, g.json)
        if updatedTimeslot:
            return updatedTimeslot, 200, None
        return {}, 404, None
