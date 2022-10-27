import psycopg2

conn = psycopg2.connect("dbname=x user=y password=z host=a port=b")
cur = conn.cursor()
cur.execute("SELECT * from users")
query = cur.fetchall()
print(query)
cur.close()
conn.close()
