import pymysql
from module import connectmysql as con
# ฟังก์ชั่น aaa


def createtable():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สร้างตาราง
    sql = """
        create table person(
        id int primary key auto_increment,
        fullname varchar(128) not null,
        email varchar(128) not null,
        age int not null
        )

        """
    try:
        cursor.execute(sql)
        connection.commit()
        print('สร้างตาราเรียบร้อยแล้ว')
    except pymysql.error:
        print(pymysql.error)


# เรียกใช้
createtable()
