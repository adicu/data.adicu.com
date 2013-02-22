import app.basic
# import lib.dbs as dbs

class CoursesHandler(app.basic.BaseHandler):
    def get(self):
        get_arg = self.get_argument
        possible = [
                "building",
                "term",
                "school",
                "call_number",
                "not_full",
                "professor",
                "department",
                "students_less_than",
                "class_type",
                "meets",
                "starts_before",
                "starts_after",
                "ends_before",
                "ends_after",
                "approval_required",
                "units",
                "title",
                "subtitle",
                "campus",
                "courseid",
        ]
        querys = {q: get_arg(q, None) for q in possible if get_arg(q, None)}

        return self.api_response(querys)
