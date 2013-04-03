#def approval_required(value):
#    return ""

#import os,sys
#base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
#if base_dir not in sys.path:
#    sys.path.append(base_dir)

#@format_api_errors
#def raise_exception():    
#    raise Exception("Invalid query")

def call_number(value):
    """int"""
    return value, "CallNumber=%(call_number)s"
    
def courseid(value):
    """string"""
    return '%%%s%%' % value, "Course~~*%(courseid)s"

def course(value):
    """string"""
    return '%%%s%%' % value, "Course~~*%(course)s"

def department(value):
    """string"""
    return '%%%s%%' % value, "(DepartmentName~~*%(department)s OR DepartmentCode~~*%(department)s)"
    
def school(value):
    """string"""
    return '%%%s%%' % value, "SchoolName~~*%(school)s"

def title(value):
    """string"""
    return '%%%s%%' % value, "CourseTitle~~*%(title)s"

def description(value):
    """string (be careful with this pretty please, it's an expensive query)"""
    return '%%%s%%' % value, "Description~~*%(description)s"

def __to_bool(value):
    if str(value).lower() in ("yes", "y", "true",  "t", "1"): return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))
