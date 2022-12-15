from faker import Faker
import psycopg2


def add_student():
    
    conn = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="password" # Assuming this is your password
    )

    cursor = conn.cursor()
    id_sql = "SELECT max(lnumber) FROM student;"
    cursor.execute(id_sql)
    max_id = cursor.fetchone()[0]
    print("max_id ", max_id)
    conn.commit()

    student_sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    id = max_id + 1
    values =    ( id, 0, "Neloy", None, "Kundu",
                 2023, "BS", "Math", "neloy@laf.edu",
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

