import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Show all tables
cursor.execute('SHOW TABLES')
tables = cursor.fetchall()

print('Tables in makeup_tutorial database:')
for table in tables:
    print(table[0])

# Close the connection
conn.close()
