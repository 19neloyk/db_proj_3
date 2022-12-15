import psycopg2


def create_db():
    conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='password',
        host='127.0.0.1',
        port= '5432'
    )

    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing query to create a database
    sql = '''CREATE database college''';

    # Creating a database
    cursor.execute(sql)
    print("Database created successfully........")
    
    #Closing the connection
    conn.close()

def build_db_tables():
    conn = psycopg2.connect(
        host="localhost",
        database="college",
        user="postgres",
        password="password" # Assuming this is your password
    )

    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    
    # Now populate the database with its tables, and starting table data
    cursor.execute(open("build_tables.sql", "r").read())
    print("Database tables added successfully");
    
    
    #Closing the connection
    conn.close()
    
def populate_db_tables():
    conn = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="password" # Assuming this is your password
    )
        
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    
    # Insertion sqls
    librarybooks_sql = "INSERT INTO librarybooks VALUES (%d, %s, %s)"
    values = [(0, "War and Peace", "Leo Tolstoy"),
                (1,"Clifford the Big Red Dog","Norman Bridwell"),
                (2, "Zoo", "James Patterson")]
    [cursor.execute(librarybooks_sql, val) for val in values]
    
    
    jobtype_sql = "INSERT INTO jobtype VALUES (%d, %s, %d)"
    values = [(0, "Professor", 40),
                (1, "Custodian", 40),
                (2, "IT Worker", 40)]
    [cursor.execute(jobtype_sql, val) for val in values]
    
    
    staff_sql = "INSERT INTO staff VALUES (%d, %d, %s, %s, %s, %d, %s, %s, %d)"
    values = [(0, 0, "Andrew", None, "Ng", True, "Rockwell", 180000),
                (1, 0, "John", "Howard", "Young", True, "Hugel", 134000),
                (2, 1, "Eddy", "Yin", "Taylor", False, "Marquis Dining Hall", 45000),
                (3, 2, "Martha", "Abigail", "Stewart", False, "Skillman Library", 90000)]
    [cursor.execute(staff_sql, val) for val in values]
    
    
    course_sql = "INSERT INTO course VALUES (%d, %d, %s, %s, %s)"
    values =[(0, 104, "CS", "Introduction to Game Programming", "This course provides hands-on experience developing computer games."),
                (1, 320, "CS", "Introduction to Database Systems", "This course examines the organization design and implementation of database management systems."),
                (2, 150, "CS", "Data Structures and Algorithms", None),
                (3, 202, "ENGL", "Writing Seminar", "Writing seminars are courses that make writing and language their explicit subject."),
                (4, 290, "MATH", "Transition to Theoretical Mathematics", "An introduction to the concepts and techniques that permeate advanced mathematics."),
                (5, 335, "MATH", "Introduction to Probability", None)]
    [cursor.execute(course_sql, val) for val in values]
    
    classinstance_sql = "INSERT INTO classinstance VALUES (%d, %d, %d, %d, %s, %d, %s, %d)"
    values =[(0,0,0,0,"Fall","Rockwell",20),
             (1,0,0,1,"Fall","Rockwell",20),
             (2,1,0,0,"Spring","Hugel",20),
             (3,2,0,0,"Spring","Hugel",20),
             (4,3,1,0,"Winter","Acopian",20),
             (5,4,0,0,"Spring","Rockwell",20),
             (6,4,1,1,"Spring","Acopian",20),
             (7,5,1,0,"Summer","Hugel",20)]
    [cursor.execute(classinstance_sql, val) for val in values]
    
    residenthall_sql = "INSERT INTO residencehall VALUES (%d, %s, %s, %d, %d, %d, %s)"
    values =[(0,"Gates Hall", "14 Quad Drive", 4, 1, 130, True),
             (1,"McKeen Hall", "16 Quad Drive", 4, 1, 130, True),
             (2,"Ruef Hall", "8 Side Drive", 5, 1, 200, True),
             (3,"South Hall", "10 Side Drive", 4, 2, 120, True),
             (4,"McKelvy Hall", "200 Happy Street", 2, 3, 25, False)]
    [cursor.execute(residenthall_sql, val) for val in values]
    
    student_sql = "INSERT INTO student VALUES (%d, %d, %s, %s, %s, %d, %s, %s, %s, %d, %d, %s, %d, %d, %d, %s)"
    values =[(0, "Neloy", None, "Kundu", 2023, "BS", "Math", "neloy@laf.edu", 32452453555, "5 Home St", DOBBBB, 1232, 78452453555, 1, "Has a bad disciplinary record"),
             (0, "Lekso", None, "Borashvili", 2023, "BS", "Computer Science", "lekso@laf.edu", 23408914325, "6 Georgia St", DOBBBB, 6235, 53408914325, 2, None),
             (0, "Jackson", "John", "Chambers", 2024, "BA", "Computer Science", "jackson@laf.edu", 19028734678, "1 Conn Ave", DOBBBB, 6463, 6408914325, 3, None),
             (0, "Griffin", "Jack", "Spahr", 2024, "BA", "Government and Law", "griffin@laf.edu", 34678190287, "4 Main Line Dr", DOBBBB, 1234, 83408914325, 2, None),
             (0, "Thomas", "Tate", "Vasu", 2022, "BA", "Economics", "tate@laf.edu", 40989072513, "83 Philly Dr", DOBBBB, 7688, 13408914325, 3, "On the brink of getting expelled"),
             (0, "Malolan", None, "Vasu", 2023, "BS", "Math", "malo@laf.edu", 12398021392, "100 India Ave", DOBBBB, 9756, 63409814325, 1, None)]
    [cursor.execute(student_sql, val) for val in values]
    
    studenttoclassinstance_sql = "INSERT INTO studenttoclassinstance VALUES (%d, %d, %s, %s)"
    values = [(0,0,"IN-PROGRESS", None),
              (0,3,"IN-PROGRESS", None),
              (0,5,"IN-PROGRESS", None),
              (1,1,"PASSED", "A"),
              (1,3,"WITHDRAWN", None),
              (1,4,"IN-PROGRESS", None),
              (2,2,"PASSED", "B"),
              (2,3,"IN-PROGRESS", None),
              (2,5,"WITHDRAWN", None),
              (3,0,"PASSED", "A"),
              (3,3,"PASSED", "B+"),
              (3,5,"IN-PROGRESS", None),
              (4,1,"FAILED", "F"),
              (4,3,"IN-PROGRESS", None),
              (4,4,"WITHDRAWN", None)]
    
    prerequisite_sql = "INSERT INTO prerequisite VALUES (%d, %d)"
    
    
    outcome_sql = "INSERT INTO prerequisite VALUES (%d, %s)"
    
    
    
    # Start inserting actual information into the databases
        
        
        
        


