import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Insert a test tutorial
cursor.execute("""
INSERT INTO tutorial (title, description, category, difficulty, duration, steps, user_id)
VALUES ('Test Tutorial', 'A test tutorial', 'Foundation', 'Beginner', 30, '["Step 1", "Step 2"]', 1)
""")

conn.commit()
print('Tutorial inserted successfully')

# Close the connection
conn.close()
