import pymysql

# Connect to the database
conn = pymysql.connect(
    host='127.0.0.1',
    user='rose',
    password='makeuptutorial',
    database='makeup_tutorial'
)
cursor = conn.cursor()

# Insert 2 tutorials for each category

# Glam Makeup - Tutorial 1
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('Glam Makeup Tutorial - Evening Glam', 'A glamorous makeup tutorial for special evening occasions', 'Glam Makeup', '["Moisturizer", "Primer", "Foundation", "Concealer", "Brows", "Eyeshadow", "Glitter Primer", "Contour", "Highlighter", "Lashes"]', '["https://example.com/glam1-step1.jpg", "https://example.com/glam1-step2.jpg", "https://example.com/glam1-step3.jpg", "https://example.com/glam1-step4.jpg", "https://example.com/glam1-step5.jpg", "https://example.com/glam1-step6.jpg", "https://example.com/glam1-step7.jpg", "https://example.com/glam1-step8.jpg", "https://example.com/glam1-step9.jpg", "https://example.com/glam1-step10.jpg"]', 1)
""")

# Glam Makeup - Tutorial 2
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('Glam Makeup Tutorial - Red Carpet Glam', 'A glamorous makeup tutorial for red carpet events', 'Glam Makeup', '["Moisturizer", "Primer", "Foundation", "Concealer", "Brows", "Eyeshadow", "Glitter", "Contour", "Highlighter", "Lashes", "Lipstick"]', '["https://example.com/glam2-step1.jpg", "https://example.com/glam2-step2.jpg", "https://example.com/glam2-step3.jpg", "https://example.com/glam2-step4.jpg", "https://example.com/glam2-step5.jpg", "https://example.com/glam2-step6.jpg", "https://example.com/glam2-step7.jpg", "https://example.com/glam2-step8.jpg", "https://example.com/glam2-step9.jpg", "https://example.com/glam2-step10.jpg", "https://example.com/glam2-step11.jpg"]', 1)
""")

# No Makeup Look - Tutorial 1
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('No Makeup Look - Natural Glow', 'A simple no makeup look for everyday natural beauty', 'No Makeup Look', '["Moisturizer", "Sunscreen or Tinted Sunscreen"]', '["https://example.com/nomakeup1-step1.jpg", "https://example.com/nomakeup1-step2.jpg"]', 1)
""")

# No Makeup Look - Tutorial 2
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('No Makeup Look - Fresh and Dewy', 'A fresh and dewy no makeup look for a youthful appearance', 'No Makeup Look', '["Moisturizer", "Sunscreen", "Blush"]', '["https://example.com/nomakeup2-step1.jpg", "https://example.com/nomakeup2-step2.jpg", "https://example.com/nomakeup2-step3.jpg"]', 1)
""")

# Latina Makeup - Tutorial 1
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('Latina Makeup Tutorial - Bold Eyes', 'A bold eye makeup tutorial inspired by Latina beauty', 'Latina Makeup', '["Matte Primer", "Foundation", "Eyeshadow", "Eyeliner", "Mascara"]', '["https://example.com/latina1-step1.jpg", "https://example.com/latina1-step2.jpg", "https://example.com/latina1-step3.jpg", "https://example.com/latina1-step4.jpg", "https://example.com/latina1-step5.jpg"]', 1)
""")

# Latina Makeup - Tutorial 2
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('Latina Makeup Tutorial - Sultry Lips', 'A sultry lip-focused makeup tutorial for Latina flair', 'Latina Makeup', '["Matte Primer", "Foundation", "Lip Liner", "Lipstick", "Gloss"]', '["https://example.com/latina2-step1.jpg", "https://example.com/latina2-step2.jpg", "https://example.com/latina2-step3.jpg", "https://example.com/latina2-step4.jpg", "https://example.com/latina2-step5.jpg"]', 1)
""")

# Douyin Makeup - Tutorial 1
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('Douyin Makeup Tutorial - Trendy Eyes', 'A trendy eye makeup tutorial popular on Douyin', 'Douyin Makeup', '["Sunscreen", "Contact Lens", "Eyeshadow", "Eyeliner"]', '["https://example.com/douyin1-step1.jpg", "https://example.com/douyin1-step2.jpg", "https://example.com/douyin1-step3.jpg", "https://example.com/douyin1-step4.jpg"]', 1)
""")

# Douyin Makeup - Tutorial 2
cursor.execute("""
INSERT INTO tutorial (title, description, category, steps, step_images, user_id)
VALUES ('Douyin Makeup Tutorial - Cute and Playful', 'A cute and playful makeup tutorial inspired by Douyin trends', 'Douyin Makeup', '["Sunscreen", "Contact Lens", "Blush", "Highlighter", "Lip Tint"]', '["https://example.com/douyin2-step1.jpg", "https://example.com/douyin2-step2.jpg", "https://example.com/douyin2-step3.jpg", "https://example.com/douyin2-step4.jpg", "https://example.com/douyin2-step5.jpg"]', 1)
""")

conn.commit()
print('Tutorials inserted successfully')

# Close the connection
conn.close()
