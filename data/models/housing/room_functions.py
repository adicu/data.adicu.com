def room_location_area(value):
    return value, "RoomLocationArea~~*%(room_location_area)s"

def residential_area(value):
    return value, "ResidentialArea~~*%(residential_area)s"

def room_location(value):
    return value, "RoomLocation~~*%(room_location)s"

def room_location_section(value):
    return value, "RoomLocationSection~~*%(room_location_section)s"

def room_location_floor_suite(value):
    return value, "RoomLocationFloorSuite~~*%(room_location_floor_suite)s"

def room(value):
    return value, "Room~~*%(room)s"

def room_area(value):
    return value, "RoomArea~~*%(room_area)s"

def room_space(value):
    return value, "RoomSpace~~*%(room_space)s"

def ay_12_13_rs_status(value):
    return value, "AY1213RSStatus~~*%(ay_12_13_rs_status)s"

def point_value(value):
    return value, "ROUND(CAST(PointValue as NUMERIC),1)=ROUND(CAST(%(point_value)s as NUMERIC),1)"

def lottery_number(value):
    return value, "LotteryNumber=%(lottery_number)s"

def is_suite(value):
    return value, "CallNumber=%(is_suite)s"
