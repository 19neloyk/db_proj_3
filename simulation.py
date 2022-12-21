from faker import Faker
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


