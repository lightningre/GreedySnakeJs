# -*- coding: utf-8 -*-
import psycopg2
import hashlib


def md5_encoding(str):
    md5_object = hashlib.md5()
    md5_object.update(str)
    return md5_object.hexdigest()

# Create a table


def create(conn, table):
    cur = conn.cursor()
    cur.execute(f'''CREATE TABLE {table}
        (ID INT PRIMARY KEY   NOT NULL,
        NAME      TEXT  NOT NULL,
        AGE      INT   NOT NULL,
        ADDRESS    CHAR(50),
        HOBBY       CHAR(50),
        SALARY     REAL);''')
    print("Table created successfully")
    conn.commit()


# Inserts data into the table
def insert(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (5, 'Wuxiang', 22, 'Shanghai', 20000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (6, 'Beiyipu', 25, 'Dalian', 15000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (7, 'Iricbing', 24, 'Jiaxin', 20000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (8, 'Xinyu', 21, 'Tianjin', 65000.00 )")

    conn.commit()
    print("Records created successfully")


# Query data
def query(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, name, address, salary from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")


# Update data
def update(conn):
    cur = conn.cursor()
    cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit
    print("Total number of rows updated :", cur.rowcount)

    cur.execute("SELECT id, name, address, salary from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print("Operation done successfully")


# Delete data
def delete(conn):
    cur = conn.cursor()
    cur.execute("DELETE from COMPANY where ID=2;")
    conn.commit
    print("Total number of rows deleted :", cur.rowcount)

    cur.execute("SELECT id, name, address, salary from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")


if __name__ == "__main__":
    conn = psycopg2.connect(database="gas", user="postgres",
                            password="p5tgb6tfc%^", host="127.0.0.1", port="5432")
    print("Opened database successfully\n")
    query(conn)
    conn.close()

    print("\n")
    str_ = '123qwe'
    md5_result = md5_encoding(str_.encode('utf-8'))  # 必须先进行转码，否则会报错
    print(f"'{str_}' is changed to '{md5_result}' by md5")
