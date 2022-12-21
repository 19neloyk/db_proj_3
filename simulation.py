from faker import Faker
from db import make_db_query
import psycopg2
import random

"""
One semester simulation
Takes in semester and year
We have defined at the start what happens every semester(standard procedures of the school)
"""
def one_semester_simulation(semester, year):
    
    conn = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="password" # Assuming this is your password
    )

    cursor = conn.cursor()
    #start of semester 
    #let's say for this semester we add one instance of every course
    course_sql = "SELECT courseid FROM course"

    cursor.execute(course_sql)
    courses = cursor.fetchall()
    for courseid in courses:
        add_classinstance(courseid[0],1,semester,year)

    #Now here we need to assign students to classes this semester

    conn.commit()
    conn.close()
    #end of semester
    #generate student to get random grade in classes he is taking


def add_student():
    
    conn = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="password" # Assuming this is your password
    )

    #assign student new id
    cursor = conn.cursor()
    id_sql = "SELECT max(lnumber) FROM student;"
    cursor.execute(id_sql)
    max_id = cursor.fetchone()[0]
    conn.commit()
    
    #retrieve residence hall ids to assign random one.
    residence_ids_sql = "SELECT hallid FROM residencehall;"
    cursor.execute(residence_ids_sql)
    residence_ids = cursor.fetchall()
    conn.commit()

    student_sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    fake = Faker()
    id = max_id + 1
    hall_id = random.choice(residence_ids)[0]
    first_name  = fake.first_name()
    last_name   = fake.last_name()
    email       = last_name+first_name + "laf.edu"
    number      = fake.msisdn()
    address     = fake.address()
    emergency   = fake.msisdn()
    values      =(  id, hall_id, first_name, None, last_name,
                    2023, email,
                    number, address, "2001-10-19",
                    "1232", emergency, 1, 0, "Has a bad disciplinary record")
    
    cursor.execute(student_sql, values)

    #we also need to give this kid a major. 

    print('student added')
    #commit the changes
    conn.commit()

    #closing connection
    conn.close()

def assign_class():
    print('class_assigned')


"""
    This will Sester - FALL/SPRING/INTERIM
    YEAR             - YYYY
    It will pick random course. assign it a professor from the same department.
    random location, 
    random start time, 
    duration 50 minutes MWF, 75 TTH
"""

def add_classinstance(courseid, section, semester, year):

    conn = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="password" # Assuming this is your password
    )

    cursor = conn.cursor()

    

    #CRN
    crn_sql = "SELECT max(crn) FROM classinstance;"
    cursor.execute(crn_sql)
    crn = cursor.fetchone()[0] + 1
    
    #courseid
    professor_sql = "SELECT staffid,location FROM staff WHERE jobid=0 AND department IN (SELECT department from course WHERE courseid = %s)"
    cursor.execute(professor_sql, [courseid,])
    professors = cursor.fetchall()
    professor = random.choice(professors)
    print(professor)
    professorid = professor[0]
    location = professor[1]
    #section = 0
    #semester
    #year
    
    starttimes = ["0800", "0900", "1000", "1100", "1300", "1400", "1500"]
    starttime  = random.choice(starttimes)
    duration   = random.choice([75, 50])
    weekdays   = random.choice(["MWF", "TTH"])
    enrollment_limit = 20

    classinstance_sql = "INSERT INTO classinstance VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (crn, courseid, professorid, section, semester, year, location, starttime, duration, weekdays, enrollment_limit)
    cursor.execute(classinstance_sql, values)
    
    conn.commit()
    conn.close()

    print('Class Instance added')


"""
We need to assign Student to a class that will be called from a simulation
Set IN_PROGRESS
"""
def add_student_to_class(lnumber, crn):

    conn = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="password" # Assuming this is your password
    )

    cursor = conn.cursor()

    studentclasssql = "INSERT INTO studenttoclassinstance VALUES (%s, %s, %s, %s)"

    values = (lnumber, crn, 'IN_PROGRESS', None)

    cursor.execute(studentclasssql, values)

    conn.commit()
    conn.close()


# This will generate a valid id for a table
def generate_id(table_name, column_name):
    query = "SELECT max(%s) FROM %s;" % (column_name, table_name)
    result = make_db_query(query)
    if len(result) == 0:
        return 0
    return result[0][0]
    

def add_courses_and_majors():
    courses = [
        {
            "course_name" : "Calculus I",
            "course_department": "Mathematics",
            "course_number" : "MATH101",
            "course_description" : "Introduction to Calculus",
        },
        {
            "course_name" : "Calculus 2",
            "course_department": "Mathematics",
            "course_number" : "MATH102",
            "course_description" : "Introduction to Calculus 2",
        },
        {
            "course_name" : "Theoretical Mathematics",
            "course_department": "Mathematics",
            "course_number" : "MATH103",
            "course_description" : "Real Analysis and Calculus",
        },
        {
            "course_name" : "Intro to Computer Science",
            "course_department": "Computer Science",
            "course_number" : "CS101",
            "course_description" : "CS for beginners",
        },
        {
            "course_name" : "Software Engineering",
            "course_department": "Computer Science",
            "course_number" : "CS102",
            "course_description" : "Build stuff!",
        },
        {
            "course_name" : "Reading and Writing",
            "course_department": "English",
            "course_number" : "ENGL101",
            "course_description" : "Learn how to read and write!",
        },
        {
            "course_number" : "ENGL102",
            "course_department": "English",
            "course_name" : "English Literature",
            "course_description" : "Read Shakespeare",
        },
    ]
    
    all_majors_information = [
                    {   
                        "name": "Mathematics",
                        "degrees" : ["BA", "BS"],
                        "required_course_numbers" : ["MATH101", "MATH102", "MATH103"]
                    },
                    {
                        "name": "Computer Science",
                        "degrees" : ["BA", "BS"],
                        "required_course_numbers" : ["MATH101", "CS101", "CS102"]
                    },
                    {
                        "name": "English",
                        "degrees" : ["BA"],
                        "required_course_numbers" : ["ENGL101", "ENGL102"]
                    }
    ]
    
    # First add all the courses
    for course in courses:
        course_id = generate_id("course", "courseid")
        course_name = course["course_name"]
        course_department = course["course_department"]
        course_number = course["course_number"]
        course_description = course["course_description"]
        
        query_str = "INSERT INTO course VALUES (%s, %s, %s, %s, %s)" % course_id, course_name, course_department, course_number, course_description
        make_db_query(query_str)
    
    
    # Add all the majors and their requirements
    for major_info in all_majors_information:
        cur_major_id = generate_id("major", "majorid")
        cur_major_name = major_info["name"]
        cur_major_degrees = major_info["degrees"]
        cur_major_requirement_numbers = major_info["required_course_numbers"]
        
        # Add the major (with variations for the degree)
        for degree in cur_major_degrees:
            query_str = "INSERT INTO major VALUES (%s, %s, %s)" % (cur_major_id, cur_major_name, degree)
            make_db_query(query_str)
        
        # Now add the major requirements
        for requirement_number in cur_major_requirement_numbers:
            # First find the relevant courseid
            query_str = "SELECT courseid FROM course WHERE coursenumber = %s" % requirement_number
            result = make_db_query(query_str)
            
            # Now add that id, if it exists
            if len(result) == 0:
                print("Could not find course with name %s" % requirement_number)
            else:
                course_id = result[0][0]
                query_str = "INSERT INTO majorrequirement VALUES (%s, %s)" % (cur_major_id, course_id)
                make_db_query(query_str)


