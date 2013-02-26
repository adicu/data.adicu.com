#def approval_required(value):
#    return ""

#import os,sys
#base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
#if base_dir not in sys.path:
#    sys.path.append(base_dir)

#@format_api_errors
#def raise_exception():    
#    raise Exception("Invalid query")

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
    
def term(value):
    if "spring" in value.lower():
	term_formatted = value[6:]+"1"
	return term_formatted, "Term=%(term)s"
    elif "fall" in value.lower():
	term_formatted = value[4:]+"2"
	return term_formatted, "Term=%(term)s"
    else:
    	#No matched queries...TODO
    	return value, "Term=asdfasdf"


    # def title():
        # pass
    
    # def units():
        # pass
