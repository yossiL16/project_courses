import mysql.connector
from soldier_courses_explorer.config import *


def search_Records_by_Institution_Name():

    word = input("enter a name of institution: ")
    cursor.execute(f"""SELECT *
    FROM courses
    WHERE institution LIKE '%{word}%'
    LIMIT 50;""")

    x = cursor.fetchall()
    for i in x:
        print(i)


def search_Records_by_Course_Name():

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
    cursor.execute("""SELECT course, COUNT(*) AS num
        FROM courses
        GROUP BY course
        ORDER BY num DESC
        LIMIT 1;
""")
    print(cursor.fetchall())


def find_least_Common_Course():
    cursor.execute("""SELECT course, COUNT(*) AS num
FROM courses
GROUP BY course
ORDER BY num ASC
LIMIT 1;
""")
    print(cursor.fetchall())




