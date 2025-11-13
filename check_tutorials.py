import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Select all tutorials
cursor.execute('SELECT * FROM tutorial')
result = cursor.fetchall()

print('Current tutorials:')
for row in result:
    print(row)

# Close the connection
conn.close()
