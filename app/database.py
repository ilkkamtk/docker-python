import mysql.connector
from dotenv import load_dotenv
import os


class Database:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        # MariaDB server details
        self.mariadb_host = os.getenv('LOCAL_HOST')
        self.mariadb_user = os.getenv('MARIADB_USER')
        self.mariadb_pass = os.getenv('MARIADB_PASS')
        self.mariadb_db = os.getenv('MARIADB_DB')
        self.mariadb_connection = None

    def connect(self):
        try:
            # Connect to MariaDB server through the tunnel
            self.mariadb_connection = mysql.connector.connect(
                host=self.mariadb_host,
                port=os.getenv('LOCAL_PORT'),
                user=self.mariadb_user,
                password=self.mariadb_pass,
                database=self.mariadb_db,
                autocommit=True
            )
            print("Connected to MariaDB through SSH tunnel.")

        except mysql.connector.Error as err:
            print(f"Failed to connect to MariaDB: {err}")

    def execute_query(self, query, params=None, fetch_all=True):
        cursor = self.mariadb_connection.cursor(dictionary=True)
        cursor.execute(query, params)

        if fetch_all:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()

        cursor.close()
        return result

    def close(self):
        # Close the database connection
        if self.mariadb_connection:
            self.mariadb_connection.close()
