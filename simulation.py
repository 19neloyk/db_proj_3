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

    student_sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    fake = Faker()
    id = max_id + 1
    hall_id = random.choice(residence_ids)[0]
    first_name  = fake.first_name()
    last_name   = fake.last_name()
    email       = last_name+first_name + "laf.edu"

    values =    ( id, hall_id, first_name, None, last_name,
                 2023, "BS", "Math", email,
                "32452453555", "5 Home St", "2001-10-19",
                "1232", "78452453555", 1, "Has a bad disciplinary record")
    
    cursor.execute(student_sql, values)

    print('student added')
    #commit the changes
    conn.commit()

    #closing connection
    conn.close()

def assign_class():
    print('class_assigned')


def faker_simulation():
    fake = Faker()
    print(fake.major())

