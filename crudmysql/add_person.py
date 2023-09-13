import pymysql
from connectdb import connectmysql as con
# ฟังก์ชั่นเพิ่มข้อมูลเข้าตาราง person


def addperson():
    connention = con.connectdb()
    cursor = connention.cursor()

    # sql

    sql = """
        insert into person (fullname,email,age) 
        values ('StillGot','stillgot1@gmail.com','33')

        """
    try:
        cursor.execute(sql)
        connention.commit()
        print('เพิ่มข้อมูลเรียบร้อยแล้ว')
    except pymysql.error:
        print(pymysql.error)


# เรียกใช้
addperson()
