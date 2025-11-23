import csv
import mysql.connector



cnx = mysql.connector.connect(
    user="root", password="", host="127.0.0.1", database="soldier_courses_db"
)
cursor = cnx.cursor()

path = "../data/courses.csv"
with open(path, encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        cursor.execute("""INSERT INTO courses(
institution, city, address, course,
district, telephone, email)
VALUES(%s, %s, %s, %s, %s, %s, %s);""", row)

cnx.commit()
cursor.close()
cnx.close()