import csv
from db.connection import *

def load_csv():
    cnx = get_connection()
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