# openfile

def read_all():
    f = open("filedata/mydata.txt", "r", encoding="utf8")
    print(f.read())
    f.close()

# read line by line


def read_line():
    f = open("filedata/mydata.txt", "r", encoding="utf8")
    for i in range(1, 5):
        print(f.readline(), end="")
    for read_line in f:
        print(f.read_line, end="")
    f.close()

    read_line()
