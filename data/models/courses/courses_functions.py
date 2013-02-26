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
    
    # def ends_before():
        # pass
    
    # def meets():
        # pass
    
    # def not_full():
        # pass
    
    # def professor():
        # pass
    
    # def school():
        # pass
    
    # def starts_after():
        # pass
    
    # def starts_before():
        # pass
    
    # def students_less_than():
        # pass
    
    # def subtitle():
        # pass
    
    # def term():
        # pass
    
    # def title():
        # pass
    
    # def units():
        # pass
