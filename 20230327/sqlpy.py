import pymysql

# pip install pymysql

defaults={
    "DB_HOST": "127.0.0.1",
    "DB_PORT" : 3306,
    "DB_NAME" : "11e",
    "DB_USER" : "11e_teszt",
    "DB_PASSWD" : "11e_teszt",
    "DB_TABLE" : "adatok"
}

def connDB(_host, _port, _user, _passwd, _dbname):
    return pymysql.connect(
                host=_host,
                port=_port,
                user=_user,
                password=_passwd,
                database=_dbname
                )

def selectDB(oszloplista="*"):
    con = connDB(
            defaults["DB_HOST"],
            defaults["DB_PORT"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"],
            defaults["DB_NAME"])
    cursor = con.cursor()

    sql= f"SELECT {oszloplista} FROM {defaults['DB_TABLE']};"
    cursor.execute(sql)
    rows = cursor.fetchall()
    con.close()
    return rows

def insertDB( nev, kor):
    con = connDB(
            defaults["DB_HOST"],
            defaults["DB_PORT"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"],
            defaults["DB_NAME"])
    cursor = con.cursor()

    sql= f"INSERT INTO {defaults['DB_TABLE']}"
    sql+= f"(név, kor) VALUES ('{nev}', '{kor}');"
    cursor.execute(sql)
    con.commit()
    con.close()

rows = selectDB("név")

insertDB("Laura", 9)
for row in rows:
    print(row)


