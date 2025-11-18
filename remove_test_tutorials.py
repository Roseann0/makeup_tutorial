import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Remove all "Test Tutorial" entries
cursor.execute("DELETE FROM tutorial WHERE title = 'Test Tutorial'")

conn.commit()
print('Test tutorials removed successfully')

# Close the connection
conn.close()
