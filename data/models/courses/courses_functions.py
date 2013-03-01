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
    return '%%%s%%' % value, "Building1~~*%(building)s"
    
def call_number(value):
    return value, "CallNumber=%(call_number)s"
    
def campus(value):
    return '%%%s%%' % value, "(CampusName~~*%(campus)s OR CampusCode~~*%(campus)s)"
    
def class_type(value):
    return '%%%s%%' % value, "(TypeCode~~*%(class_type)s OR TypeName~~*%(class_type)s)"
    
def courseid(value):
    return '%%%s%%' % value, "Course~~*%(courseid)s"

def department(value):
    return '%%%s%%' % value, "(DepartmentName~~*%(department)s OR DepartmentCode~~*%(department)s)"
    
def ends_after(value):
    ends_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return ends_formatted, "EndTime1>%(ends_after)s"
    
def ends_before(value):
    ends_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return ends_formatted, "EndTime1<%(ends_before)s"
    
def not_full(value):
    if __to_bool(value):
    	return value, "(NumEnrolled<MaxSize OR MaxSize=0)"
    else:
    	return value, "NumEnrolled>MaxSize"
    
def professor(value):
    return '%%%s%%' % value, "Instructor1Name~~*%(professor)s"
    
def school(value):
    return '%%%s%%' % value, "SchoolName~~*%(school)s"
    
def starts_after(value):
    starts_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return starts_formatted, "StartTime1>%(starts_after)s"
    
def starts_before(value):
    starts_formatted = value[0:2] + ":" + value[2:4] + ":00"
    return starts_formatted, "StartTime1<%(starts_before)s"
    
def students_less_than(value):
    return value, "NumEnrolled<%(students_less_than)s"
    
def term(value):
    if "spring" in value.lower():
        term_formatted = value[6:]+"1"
        return term_formatted, "Term=%(term)s"
    elif "fall" in value.lower():
        term_formatted = value[4:]+"2"
        return term_formatted, "Term=%(term)s"
    else:
    	#No matched queries...TODO
    	return value, "Term=%(term)s"


def title(value):
    return '%%%s%%' % value, "CourseTitle~~*%(title)s"

def meets_on(value):
    return '%%%s%%' % value, "MeetsOn1~~*%(meets_on)s"

def __to_bool(value):
    """
       Converts 'something' to boolean. Raises exception for invalid formats
           Possible True  values: 1, True, "1", "True", "yes", "y", "t"
           Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
    """
    if str(value).lower() in ("yes", "y", "true",  "t", "1"): return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))
