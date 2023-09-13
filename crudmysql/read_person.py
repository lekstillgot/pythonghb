import pymysql
from connectdb import connectmysql as con
from tabulate import tabulate


def readperson():
    connention = con.connectdb()
    cursor = connention.cursor()

    sql = """
    select * from person
    """

    try:
        cursor.execute(sql)
        connention.commit()
        headers = {"id": "ID", "fullname": "FULLNAME",
                   "email": "EMAIL", "age": "AGE"}
        print(tabulate(cursor, headers=headers, tablefmt="pretty"))
    except pymysql.Error:
        print(pymysql.Error)


# เรียกใช้
readperson()
