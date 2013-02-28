def name(value):
    return value, "Building~~*%(name)s"

def apartment_style(value):
    return value, "ApartmentStyle=%(apartment_style)s"

def suite_style(value):
    return value, "SuiteStyle=%(suite_style)s"

def corridor_style(value):
    return value, "CorridorStyle=%(corridor_style)s"

def private_bathroom(value):
    return value, "PrivateBathroom=%(private_bathroom)s"

def semi_private_bathroom(value):
    return value, "SemiPrivateBathroom=%(semi_private_bathroom)s"

def shared_bathroom(value):
    return value, "SharedBathroom=%(shared_bathroom)s"

def private_kitchen(value):
    return value, "PrivateKitchen=%(private_kitchen)s"

def semi_private_kitchen(value):
    return value, "SemiPrivateKitchen=%(semi_private_kitchen)s"

def shared_kitchen(value):
    return value, "SharedKitchen=%(shared_kitchen)s"

def lounge(value):
    return value, "Lounge%s\'\'" % ('!=' if _to_bool(value) else '=')

def _to_bool(value):
    """
       Converts 'something' to boolean. Raises exception for invalid formats
           Possible True  values: 1, True, "1", "True", "yes", "y", "t"
           Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
    """
    if str(value).lower() in ("yes", "y", "true",  "t", "1"): return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))
