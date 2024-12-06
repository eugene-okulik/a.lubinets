import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# добавляем студента
cursor.execute("INSERT INTO  students (name, second_name) values ('Bruce', 'Wayne')")
student_id = cursor.lastrowid
print(f"ID студента: {student_id}")

print("-" * 40)
# добавляем книги
cursor.execute("INSERT INTO books (title) values ('Грокаем алгоритмы часть 2')")
book1_id = cursor.lastrowid
print(f"ID книги: {book1_id}")
cursor.execute("INSERT INTO books (title) values ('Не простой Python')")
book2_id = cursor.lastrowid
print(f"ID книги: {book2_id}")

print("-" * 40)
# добавляем книги к ранее добавленному студенту
cursor.execute(f"Update books SET taken_by_student_id = {student_id} where id = {book1_id}")
cursor.execute(f"Update books SET taken_by_student_id = {student_id} where id = {book2_id}")
cursor.execute(f"SELECT title FROM books WHERE taken_by_student_id = {student_id}")
added_books = cursor.fetchall()
print(f"Добавили книги для студента с ID {student_id}:\n{added_books}")

print("-" * 40)
# добавляем группу
cursor.execute("INSERT INTO `groups` (title,start_date,end_date) "
               "values ('QA manual team', '2024-11-20', '2025-01-31')"
               )
group_id = cursor.lastrowid
print(f"ID группы: {group_id}")

print("-" * 40)
# связываем студента с группой
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")
cursor.execute(f"SELECT * FROM students WHERE group_id = {group_id}")
data_group = cursor.fetchone()
print(f"Студент с ID {student_id} находится в группе под ID {data_group['group_id']}")

print("-" * 40)
# добавляем предметы
cursor.execute("INSERT INTO subjets (title) Values ('Техническая механика часть 2')")
subjets1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) Values ('КОМПРОМАТ')")
subjets2_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM subjets WHERE id = {subjets1_id}")
added_subjets1 = cursor.fetchall()
print(f"Добавили прдемет: {added_subjets1}")
cursor.execute(f"SELECT * FROM subjets WHERE id = {subjets2_id}")
added_subjets2 = cursor.fetchall()
print(f"Добавили прдемет: {added_subjets2}")

print("-" * 40)
# добавляем уроки в предметы
cursor.execute(f"INSERT INTO lessons (title, subject_id) Values ('Статика твердого тела', {subjets1_id})")
lesson1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) Values ('Сдвиг и кручение', {subjets1_id})")
lesson2_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) Values ('Растяжение-сжатие', {subjets2_id})")
lesson3_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) Values ('Сложное сопротивление', {subjets2_id})")
lesson4_id = cursor.lastrowid
cursor.execute(f"SELECT title FROM lessons WHERE subject_id = {subjets1_id}")
data1_lesson = cursor.fetchall()
print(f"Данные по урокам добавленные по предмету c ID {subjets1_id}:\n{data1_lesson}")
cursor.execute(f"SELECT title FROM lessons WHERE subject_id = {subjets2_id}")
data2_lesson = cursor.fetchall()
print(f"Данные по урокам добавленные по предмету c ID {subjets2_id}:\n{data2_lesson}")

print("-" * 40)
# добавляем оценки по предметам для ранее добавленного студента
insert_many = "INSERT INTO marks (value, lesson_id, student_id) Values (%s, %s, %s)"
cursor.executemany(insert_many, [
    (4, lesson1_id, student_id),
    (3, lesson2_id, student_id),
    (5, lesson3_id, student_id),
    (3, lesson4_id, student_id)
])
cursor.execute(f"SELECT value FROM marks WHERE student_id = {student_id}")
student_marks = cursor.fetchall()
print(f"Данные по оценкам студента с ID {student_id}:\n{student_marks}")

print("-" * 40)
# Выводим всю информацию по студенту
select_query = """
SELECT * FROM students
JOIN books
ON students.id = books.taken_by_student_id
JOIN `groups`
ON students.group_id = groups.id
JOIN marks
ON students.id = marks.student_id
JOIN lessons
ON marks.lesson_id = lessons.id
JOIN subjets
ON lessons.subject_id = subjets.id
WHERE
students.id = %s
"""
cursor.execute(select_query, (student_id,))
data = cursor.fetchall()
print(f"Все данные по студенты с ID {student_id}:\n{data}")
db.commit()

db.close()
