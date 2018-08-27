import threading
from DB.Singleton import *

table = 'document'


class DBController(threading.Thread):
    connection = DbConnection.get_connection()

    def __init__(self):
        pass

    @classmethod
    def add(self, name, author, description):
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO " + table + " (`document_name`, `author`, `description`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, author, description))
                self.connection.commit()  # Compulsory....
                return True
        except:
            self.connection.rollback()
            return False

    @classmethod
    def get_all(self):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM " + table
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
        except:
            print("Error in retrieving data")
            return None

    @classmethod
    def get_by_id(self, __id__):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM " + table + " WHERE id = %s", __id__)
                results = cursor.fetchone()
                return results
        except:
            print("Error in retrieving data by id")
            return None

    @classmethod
    def delete_by_id(self, id):

        conn = self.connection
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM " + table + " WHERE id = %s", id)
                conn.commit()
                print("Deleted")
                return True
        except:
            conn.rollback()
            return False
    @classmethod
    def update_by_id(self, id, name, author, description):
        conn = self.connection
        sql = """
            UPDATE document 
            SET document_name = %s, author = %s, description = %s
            WHERE id = %s"""
        values = (name, author, description, id)
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                conn.commit()
                print("Updated")
                return True
        except:
            conn.rollback()
            return False


