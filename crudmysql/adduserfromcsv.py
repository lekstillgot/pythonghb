import pymysql
from connectdb import connectmysql as con
import csv
# ฟังก์ชั่นสำหรับอ่านและเพิ่มข้อมูลเข้าตาราง csv


def readcsvandinsertusers():
    connection = con.connectdb()
    cursor = connection.cursor()
    with open('../filedata/user.csv', 'r', encoding="utf8")as csv_file:
        # สร้าง Reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        # ข้าม Header
        header = next(csv_reader)

        # วนลูปอ่าน
        for row in csv_reader:
            sql = "insert into users (name,email,mobile) values (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("เพิ่มข้อมูลเรียบร้อยแล้ว")
    connection.commit()
    connection.close()


# เรียกใช้
readcsvandinsertusers()
