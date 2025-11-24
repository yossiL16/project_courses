import mysql.connector
from db.connection import get_connection


def search_Records_by_Institution_Name():
    cnx = get_connection()
    cursor = cnx.cursor()
    word = input("enter a name of institution: ")
    cursor.execute(f"""SELECT *
    FROM courses
    WHERE institution LIKE '%{word}%'
    LIMIT 50;""")

    x = cursor.fetchall()
    for i in x:
        print(i)


def search_Records_by_Course_Name():
    cnx = get_connection()
    cursor = cnx.cursor()
    word = input("enter a name of course: ")
    cursor.execute("""SELECT id, institution, city, course, district, telephone, email
FROM courses
WHERE course LIKE CONCAT('%', %s, '%') 
LIMIT 50;
""", (word,))

    x = cursor.fetchall()
    for i in x:
        print(i)


def find_Most_Common_Course():
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute("""SELECT course, COUNT(*) AS num
        FROM courses
        GROUP BY course
        ORDER BY num DESC
        LIMIT 1;
""")
    print(cursor.fetchall())


def find_least_Common_Course():
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute("""SELECT course, COUNT(*) AS num
FROM courses
GROUP BY course
ORDER BY num ASC
LIMIT 1;
""")
    print(cursor.fetchall())


def show_Course_Count_per_District():
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute("""
    SELECT district, COUNT(*) AS num_courses
        FROM courses
        GROUP BY district
        ORDER BY num_courses DESC;
        """)
    listi = cursor.fetchall()
    for i in listi:
        print(i)


def free_SQL_Query():
    cnx = get_connection()
    cursor = cnx.cursor()

    while True:
        query = input("please enter a query: ")
        if query.strip().upper().startswith("SELECT"):
            cursor.execute(query)
            print(cursor.fetchall())
            break
        else:
            print("Error! You can only start with SELECT")
            continue


