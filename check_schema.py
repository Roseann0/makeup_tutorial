import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Describe the tutorial table
cursor.execute('DESCRIBE tutorial')
result = cursor.fetchall()

print('Current tutorial table schema:')
for row in result:
    print(row)

# Close the connection
conn.close()
