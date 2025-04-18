import mysql.connector
from config import config

def execute_query(sql):
    print("inside the execute_query function")
    conn = mysql.connector.connect(**config["MYSQL"])
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return columns, results

