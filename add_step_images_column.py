import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Add step_images column to tutorial table
cursor.execute("""
ALTER TABLE tutorial ADD COLUMN step_images TEXT
""")

conn.commit()
print('step_images column added successfully')

# Close the connection
conn.close()
