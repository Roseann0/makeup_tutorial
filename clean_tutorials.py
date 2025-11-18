import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Delete all tutorials except the new 8 (IDs 41-48)
cursor.execute("DELETE FROM tutorial WHERE id NOT IN (41,42,43,44,45,46,47,48)")

conn.commit()
print('Old tutorials removed successfully')

# Close the connection
conn.close()
