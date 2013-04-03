def building(value):
    """string"""
    return '%%%s%%' % value, "Building1~~*%(building)s"
    
def call_number(value):
    """int"""
    return value, "CallNumber=%(call_number)s"
    
def campus(value):
    """string"""
    return '%%%s%%' % value, "(CampusName~~*%(campus)s OR CampusCode~~*%(campus)s)"
    
def class_type(value):
    """string"""
    return '%%%s%%' % value, "(TypeCode~~*%(class_type)s OR TypeName~~*%(class_type)s)"
    
def courseid(value):
    """string"""
    return '%%%s%%' % value, "Course~~*%(courseid)s"

def course(value):
    """ string """
    return '%%%s%%' % value, "Course~~*%(course)s"

def ends_after(value):
    """time: HH:MM"""
    ends = value.split(":")
    ends_formatted = ends[0] + ":" + ends[1] + ":00"
    return ends_formatted, "EndTime1>%(ends_after)s"
    
def ends_before(value):
    """time: HH:MM"""
    ends = value.split(":")
    ends_formatted = ends[0] + ":" + ends[1] + ":00"
    return ends_formatted, "EndTime1<%(ends_before)s"

def ends_at(value):
    """ time: HH:MM"""
    ends = value.split(":")
    ends_formatted = ends[0] + ":" + ends[1] + ":00"
    return ends_formatted, "EndTime1=%(ends_at)s"
    
def not_full(value):
    """boolean"""
    if __to_bool(value):
    	return value, "(NumEnrolled<MaxSize OR MaxSize=0)"
    else:
    	return value, "NumEnrolled>MaxSize"
    
def professor(value):
    """string"""
    return '%%%s%%' % value, "Instructor1Name~~*%(professor)s"
    
def starts_after(value):
    """time HH:MM"""
    starts = value.split(":")
    starts_formatted =  starts[0] + ":" + starts[1] + ":00"
    return starts_formatted, "StartTime1>%(starts_after)s"
    
def starts_before(value):
    """time HH:MM"""
    starts = value.split(":")
    starts_formatted = starts[0] + ":" + starts[1] + ":00"
    return starts_formatted, "StartTime1<%(starts_before)s"

def starts_at(value):
    """ time HH:MM"""
    starts = value.split(":")
    starts_formatted = starts[0] + ":" + starts[1] + ":00"
    return starts_formatted, "StartTime1=%(starts_at)s"
    
def students_less_than(value):
    """int"""
    return value, "NumEnrolled<%(students_less_than)s"
    
def term(value):
    """string"""
    if "spring" in value.lower():
        term_formatted = value[6:]+"1"
        return term_formatted, "Term=%(term)s"
    elif "fall" in value.lower():
        term_formatted = value[4:]+"2"
        return term_formatted, "Term=%(term)s"
    else:
    	#No matched queries...TODO
    	return value, "Term=%(term)s"

def meets_on(value):
    """string"""
    return '%%%s%%' % value, "MeetsOn1~~*%(meets_on)s"

def __to_bool(value):
    if str(value).lower() in ("yes", "y", "true",  "t", "1"): return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))
