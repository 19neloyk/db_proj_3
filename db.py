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

def build_db():
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
    print("Database tables and starting data added successfully");
    
    
    #Closing the connection
    conn.close()


