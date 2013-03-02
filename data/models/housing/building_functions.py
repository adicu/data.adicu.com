def name(value):
    """string"""
    return '%%%s%%' % value, "Building~~*%(name)s"

def apartment_style(value):
    """boolean"""
    return value, "ApartmentStyle=%(apartment_style)s"

def suite_style(value):
    """boolean"""
    return value, "SuiteStyle=%(suite_style)s"

def corridor_style(value):
    """boolean"""
    return value, "CorridorStyle=%(corridor_style)s"

def private_bathroom(value):
    """boolean"""
    return value, "PrivateBathroom=%(private_bathroom)s"

def semi_private_bathroom(value):
    """boolean"""
    return value, "SemiPrivateBathroom=%(semi_private_bathroom)s"

def shared_bathroom(value):
    """boolean"""
    return value, "SharedBathroom=%(shared_bathroom)s"

def private_kitchen(value):
    """boolean"""
    return value, "PrivateKitchen=%(private_kitchen)s"

def semi_private_kitchen(value):
    """boolean"""
    return value, "SemiPrivateKitchen=%(semi_private_kitchen)s"

def shared_kitchen(value):
    """boolean"""
    return value, "SharedKitchen=%(shared_kitchen)s"

def lounge(value):
    """boolean"""
    return value, "Lounge%s\'\'" % ('!=' if _to_bool(value) else '=')

def _to_bool(value):
    if str(value).lower() in ("yes", "y", "true",  "t", "1"): return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))
