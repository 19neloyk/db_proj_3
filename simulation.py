from faker import Faker
import psycopg2
import random

#this will be one year(2 semester) simulation. 
def one_year_simulation():
    semester = 'Fall'
    #start of semester 


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
    professor_sql = "SELECT staffid FROM staff WHERE jobid=0"
    cursor.execute(professor_sql)
    professorids = cursor.fetchall()
    professorid = random.choice(professorids)[0]

    #section = 0
    #semester
    #year
    location = "Rockwell"
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