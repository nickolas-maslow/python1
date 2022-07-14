import psycopg2
from data import *

con = psycopg2.connect(user=user, host=host, password=password, database=db_name)
cur = con.cursor()
cur.execute('''
    CREATE IF NOT EXISTS database new_postgres_db
''')
cur.execute('''
    CREATE IF NOT EXISTS public.new_postgres_tb(
    name text,
    age int,
    is_having_money boolean NOT NULL DEFAULT false,
    id SERIAL,
    PRIMARY KEY (id)
    )   
''')
con.commit()
con.close()

#######################################################################################################################


con = psycopg2.connect(user=user, host=host, password=password, database=db_name)
cur = con.cursor()
new_arr = [
    ['x', 12, 'true'],
    ['y', 4, 'true'],
    ['z', 16, 'false'],
    ['q', 22, 'false'],
    ['t', 56, 'true'],
]
for i in new_arr:
    query_string = f"""
    INSERT INTO public.new_postgres_db (name, age, is_having_money)
    VALUES ('{i[0]}, {i[1]}, {[2]}')
    """
cur.execute(query_string)
con.commit()
con.close()


#######################################################################################################################


connection = psycopg2.connect(user=user, password=password, host=host, database=db_name)
cur = connection.cursor()
cur.execute("""
SELECT * FROM public.new_postgres_db
WHERE age > 20
ORDER BY age ABS
""")
records = cur.fetchall()
print(records)
connection.close()
