import psycopg2
from get_api import data

try:
    connection = psycopg2.connect(host='localhost',
                                  user='postgres',
                                  password='1111',
                                  database='new_postgres_bd')
    cursor = connection.cursor()
    for i in data:
        query_string = f"""
            INSERT INTO public.new_postgres_bd (userId, id, title, body)
            VALUES ({i['userId']}, {i['id']}, {i['title']}, {i['body']})
        """
        cursor.execute()
        connection.commit()
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')
