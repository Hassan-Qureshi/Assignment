import pymysql
from Model import Document
host = 'localhost'
user = 'root'
password = 'root'
db = 'assignment'
table = 'document'

def getConnection():
    connection = pymysql.connect(host, user, password, db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return connection

def add(name, author, description):
    try:
        con = getConnection()
        with con.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO "+ table + " (`document_name`, `author`, `description`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, author, description))
            con.commit()    # Compulsory....
            flag = True
    except:
        con.rollback()
        flag = False
    return flag


def get_all():
    results = None
    try:
        with getConnection().cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM " + table
            cursor.execute(sql)
            results = cursor.fetchall()
    except:
        print("Error in retrieving data")
        return

    return results

def getByID(id):
    results = None
    try:
        with getConnection().cursor() as cursor:
            cursor.execute("SELECT * FROM "+table+" WHERE id = %s", id)
            results = cursor.fetchone()
            print(results)
    except:
        print("Error in retrieving data by id")
        return
    return results

def deleteByID(id):

    flag = False
    try:
        conn = getConnection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM "+table+" WHERE id = %s", id)
            conn.commit()
            flag = True
            print("Deleted")
    except:
        conn.rollback()
        flag = False
    return flag



# print(add('Abdullah-Novel', 'Naseem', "Amazing Story based novel"))
documents = []
# for
documents.append(Document())
getAll()
#getByID(5)
#deleteByID(1)