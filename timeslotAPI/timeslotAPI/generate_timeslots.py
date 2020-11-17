import json
from datetime import date, timedelta

DENTISTS = ['Dr Green', 'Dr James', 'Dr Smith']
START_DATE = date(2020, 11, 15)
END_DATE = date(2020, 12, 31)
DIFFERENCE_IN_DATES = END_DATE - START_DATE
START_TIMES = ['9', '10', '11', '12', '13', '14', '15', '16']

jsonOutput = []
timeslotIndex = 1

for dentist in DENTISTS:
    for dayIndex in range(DIFFERENCE_IN_DATES.days + 1):
        date = START_DATE + timedelta(days=dayIndex)
        for startTime in START_TIMES:
            jsonOutput.append({"id": timeslotIndex, "dentist": dentist, "startTime": startTime, "date": str(date), "status": "available"})
            timeslotIndex += 1

with open("timeslots.json", "w") as jsonFile:
    json.dump(jsonOutput, jsonFile)
