#def approval_required(value):
#    return ""

def building(value):
    return value, "Building1=%(building)s"
    
def call_number(value):
    return value, "CallNumber=%(call_number)s"
    
def campus(value):
    return value, "(CampusName=%(campus)s OR CampusCode=%(campus)s)"
    
def class_type(value):
    return value, "(TypeCode=%(class_type)s OR TypeName=%(class_type)s)"
    
def courseid(value):
    return value, "Course=%(courseid)s"

def department(value):
    return value, "(DepartmentName=%(department)s OR DepartmentCode=%(department)s)"
    
def ends_after(value):
    ends_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return ends_formatted, "EndTime1>%(ends_after)s"
    
def ends_before(value):
    ends_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return ends_formatted, "EndTime1<%(ends_before)s"
    
    # def meets():
        # pass
    
def not_full(value):
    if value == "true":
    	return value, "(NumEnrolled<MaxSize OR MaxSize=0)"
    else:
    	return value, "NumEnrolled>MaxSize"
    
def professor(value):
    name_formatted = value.upper()
    return name_formatted, "Instructor1Name ~ %(professor)s"
    
    # def school():
        # pass
    
def starts_after(value):
    starts_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return starts_formatted, "StartTime1>%(starts_after)s"
    
def starts_before(value):
    starts_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return starts_formatted, "StartTime1<%(starts_before)s"
    
def students_less_than(value):
    return value, "NumEnrolled<%(students_less_than)s"
    
    # def subtitle():
        # pass
    
    # def term():
        # pass
    
    # def title():
        # pass
    
    # def units():
        # pass
