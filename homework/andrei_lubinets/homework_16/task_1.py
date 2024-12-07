import os
import csv
import mysql.connector as mysql
import dotenv

bace_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(bace_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    data = csv.DictReader(csv_file)
    csv_data = []
    for line in data:
        csv_data.append(line)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
select_query = """
SELECT s.name, s.second_name, g.title as "group_title", b.title as "book_title",
s2.title as "subject_title", l.title as "lesson_title", m.value as "mark_value" 
FROM students s
LEFT JOIN `groups` g on g.id = s.group_id
LEFT JOIN books b on b.taken_by_student_id = s.id
LEFT JOIN marks m on m.student_id = s.id
LEFT JOIN lessons l on l.id = m.lesson_id
LEFT JOIN subjets s2 on s2.id = l.subject_id
"""

cursor.execute(select_query)
db_data = cursor.fetchall()

no_match = list(filter(lambda x: x not in db_data, csv_data))
print('Данные отсутствующие в БД: ')
for row in no_match:
    print(row)

db.close()
