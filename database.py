import os
import cx_Oracle
from fastapi import HTTPException

class OracleDB:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.service_name = os.getenv("DB_DSN")
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.view_name = os.getenv("VIEW_NAME")

    def connect(self):
        try:
            dsn = cx_Oracle.makedsn(self.host, self.port, service_name=self.service_name)
            self.connection = cx_Oracle.connect(self.username, self.password, dsn)
            self.cursor = self.connection.cursor()
        except cx_Oracle.Error as error:
            raise HTTPException(status_code=500, detail=f"Database error: {error}")

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def read_data_from_view(self, view_name):
        try:
            query = f"SELECT * FROM {self.view_name}"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except cx_Oracle.Error as error:
            raise HTTPException(status_code=500, detail=f"Database error: {error}")
