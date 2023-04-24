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
    
def updateKor(ujkor, felt=0):
    con = connDB(
            defaults["DB_HOST"],
            defaults["DB_PORT"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"],
            defaults["DB_NAME"])
    cursor = con.cursor()

    sql= f"UPDATE {defaults['DB_TABLE']} "
    sql+= f"SET Kor = {ujkor} WHERE {felt};"
    cursor.execute(sql)
    con.commit()
    con.close()

def deleteRows(felt="0"):
    con = connDB(
            defaults["DB_HOST"],
            defaults["DB_PORT"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"],
            defaults["DB_NAME"])
    cursor = con.cursor()

    sql= f"DELETE FROM {defaults['DB_TABLE']} "
    sql+= f"WHERE {felt};"
    cursor.execute(sql)
    con.commit()
    con.close()
    
def truncate(tablename):
    con = connDB(
            defaults["DB_HOST"],
            defaults["DB_PORT"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"],
            defaults["DB_NAME"])
    cursor = con.cursor()

    sql= f"TRUNCATE {tablename};"
    cursor.execute(sql)
    con.commit()
    con.close()

def droptable(tablename):
    con = connDB(
            defaults["DB_HOST"],
            defaults["DB_PORT"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"],
            defaults["DB_NAME"])
    cursor = con.cursor()

    sql= f"DROP TABLE {tablename};"
    cursor.execute(sql)
    con.commit()
    con.close()
    
def createTable(tablename):
    con = connDB(
            defaults["DB_HOST"],
            defaults["DB_PORT"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"],
            defaults["DB_NAME"])
    cursor = con.cursor()
    sql=f"CREATE TABLE {tablename}("
    sql+= "`id` INT NOT NULL AUTO_INCREMENT ,"
    sql+= "`név` VARCHAR(50) NOT NULL ,"
    sql+= "`kor` INT NOT NULL ,"
    sql+= "`magasság` INT NOT NULL ,"
    sql+= "PRIMARY KEY (`id`)"
    sql+= ") ENGINE = InnoDB;"
    cursor.execute(sql)
    con.commit()
    con.close()
createTable("adatok")    
#updateKor(6, "Kor=9")
#deleteRows("Kor=6")
#truncate(defaults["DB_TABLE"])
#rows = selectDB("*")

#insertDB("Laura", 9)
#for row in rows:
#    print(row)

#droptable(defaults["DB_TABLE"])
