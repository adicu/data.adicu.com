import sys
import argparse
import os

import lib.pg

schema =  [
    "Term varchar(32)",
    "Course varchar(32)",
    "PrefixName varchar(32)",
    "DivisionCode varchar(32)",
    "DivisionName varchar(32)",
    "CampusCode varchar(32)",
    "CampusName varchar(32)",
    "SchoolCode varchar(32)",
    "SchoolName varchar(32)",
    "DepartmentCode varchar(32)",
    "DepartmentName varchar(32)",
    "SubtermCode varchar(32)",
    "SubtermName varchar(32)",
    "CallNumber varchar(32)",
    "NumEnrolled int",
    "MaxSize int",
    "EnrollmentStatus varchar(32)",
    "NumFixedUnits int",
    "MinUnits int",
    "MaxUnits int",
    "CourseTitle varchar(32)",
    "CourseSubtitle varchar(32)",
    "TypeCode varchar(32)",
    "TypeName varchar(32)",
    "Approval varchar(32)",
    "BulletinFlags varchar(32)",
    "ClassNotes varchar(32)",
    "MeetsOn1 varchar(32)",
    "StartTime1 time",
    "EndTime1 time",
    "Building1 varchar(32)",
    "Room1 varchar(32)",
    "MeetsOn2 varchar(32)",
    "StartTime2 time",
    "EndTime2 time",
    "Building2 varchar(32)",
    "Room2 varchar(32)",
    "MeetsOn3 varchar(32)",
    "StartTime3 time",
    "EndTime3 time",
    "Building3 varchar(32)",
    "Room3 varchar(32)",
    "MeetsOn4 varchar(32)",
    "StartTime4 time",
    "EndTime4 time",
    "Building4 varchar(32)",
    "Room4 varchar(32)",
    "MeetsOn5 varchar(32)",
    "StartTime5 time",
    "EndTime5 time",
    "Building5 varchar(32)",
    "Room5 varchar(32)",
    "MeetsOn6 varchar(32)",
    "StartTime6 time",
    "EndTime6 time",
    "Building6 varchar(32)",
    "Room6 varchar(32)",
    "Meets1 varchar(32)",
    "Meets2 varchar(32)",
    "Meets3 varchar(32)",
    "Meets4 varchar(32)",
    "Meets5 varchar(32)",
    "Meets6 varchar(32)",
    "Instructor1PID varchar(32)",
    "Instructor1Name varchar(32)",
    "Instructor2PID varchar(32)",
    "Instructor2Name varchar(32)",
    "Instructor3PID varchar(32)",
    "Instructor3Name varchar(32)",
    "Instructor4PID varchar(32)",
    "Instructor4Name varchar(32)",
    "PrefixLongname varchar(32)",
    "ExamMeet varchar(32)",
    "ExamDate varchar(32)",
    "ChargeMsg1 varchar(32)",
    "ChargeAmt1 varchar(32)",
    "ChargeMsg2 varchar(32)",
    "ChargeAmt2 varchar(32)",
]

def create_table():
    print 'Creating courses table with proper schema...'
    pg = lib.pg.pg_aync()
    cursor = pg.cursor()
    db_query = 'SELECT * FROM courses_t;'
    #db_query = 'CREATE TABLE IF NOT EXISTS courses_t (%s);' % ", ".join(schema)
    cursor.execute(db_query, _finish)
    #pg.commit()
    print 'Courses table created.'

def _finish(cursor):
    print '%s' % cursor.fetchall()
    print 'Courses table created.'


def main():
    parser = argparse.ArgumentParser(description="""Read a directory of courses
            JSON dump file and writes """)
    parser.add_argument('--create', action='store_true')
    args = parser.parse_args()
    if args.create: create_table()

if __name__ == "__main__":
    main()
