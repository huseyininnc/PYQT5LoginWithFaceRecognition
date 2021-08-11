import sqlite3 as sql3

with sql3.connect('databases/face_recognition.db') as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS faces(
role VARCHAR(20) NOT NULL,
name VARCHAR(20) NOT NULL,
facepath VARCHAR(20) NOT NULL);
''')

db.commit()
db.close()