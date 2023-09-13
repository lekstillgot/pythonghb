import pymysql
from connectdb import connectmysql as con
# ฟังก์ชั่นแก้ไชข้อมูลเข้าตาราง person


def updateperson():
    connention = con.connectdb()
    cursor = connention.cursor()

    # sql

    sql = """
        delete from person 
        where id = '1'

        """
    try:
        cursor.execute(sql)
        connention.commit()
        print('แก้ไขข้อมูลเรียบร้อยแล้ว')
    except pymysql.error:
        print(pymysql.error)


# เรียกใช้
updateperson()
