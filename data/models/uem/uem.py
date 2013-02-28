import logging

single_event_format = {

        }

SELECT = [key for key in single_course_format]

TABLE = "uem_t"

time_format = ["StartTime", "EndTime"]

def build_response_dict(row):
    response = single_course_format.copy()
    for i, key in enumerate(single_course_format):
        if key in time_format:
            response[key] = str(row[i])
        else:
            response[key] = row[i]
    return response
