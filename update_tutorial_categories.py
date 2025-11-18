import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Update tutorial categories
# IDs 1-2: Glam Makeup
cursor.execute("UPDATE tutorial SET category = 'Glam Makeup' WHERE id IN (1, 2)")

# IDs 3-4: No Makeup Look
cursor.execute("UPDATE tutorial SET category = 'No Makeup Look' WHERE id IN (3, 4)")

# IDs 5-6: Latina Makeup
cursor.execute("UPDATE tutorial SET category = 'Latina Makeup' WHERE id IN (5, 6)")

# IDs 7-8: Douyin Makeup
cursor.execute("UPDATE tutorial SET category = 'Douyin Makeup' WHERE id IN (7, 8)")

conn.commit()
print('Tutorial categories updated successfully')

# Close the connection
conn.close()
