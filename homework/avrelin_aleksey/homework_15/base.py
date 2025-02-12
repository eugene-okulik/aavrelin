import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',  # Исправлено: параметр user вместо username
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# Создаем студента
cursor = db.cursor(dictionary=True)
query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(query, ['Aleksey', 'Mansem'])
student_id = cursor.lastrowid
db.commit()

# Добавляем 2 книги
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.execute(query, ['Lesson_SQL_10/02', student_id])
books_1_id = cursor.lastrowid
cursor.execute(query, ['Lesson_SQL_09/02', student_id])
books_2_id = cursor.lastrowid
db.commit()

# Создаем группу
query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(query, ['Moskow', '2025-02-10', '2026-02-10'])
groups_id = cursor.lastrowid
db.commit()

# Добавляем студента к группе
query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query, [groups_id, student_id])
db.commit()

# Создание учебных предметов
query = "INSERT INTO subjets (title) VALUES (%s)"
cursor.execute(query, ['математика'])
subjets_1_id = cursor.lastrowid
cursor.execute(query, ['физика'])
subjets_2_id = cursor.lastrowid
db.commit()

# Создаем 4 занятия
query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.execute(query, ['Занятие-1', subjets_1_id])
lessons_1_id = cursor.lastrowid
cursor.execute(query, ['Занятие-2', subjets_1_id])
lessons_2_id = cursor.lastrowid
cursor.execute(query, ['Занятие-3', subjets_2_id])
lessons_3_id = cursor.lastrowid
cursor.execute(query, ['Занятие-4', subjets_2_id])
lessons_4_id = cursor.lastrowid
db.commit()

# Проставляем оценку студенту по 4 занятиям
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.execute(query, [4, lessons_1_id, student_id])
cursor.execute(query, [3, lessons_2_id, student_id])
cursor.execute(query, [5, lessons_3_id, student_id])
cursor.execute(query, [2, lessons_4_id, student_id])
db.commit()

# Получаем все оценки студента
query = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(query, [student_id])
marks = cursor.fetchall()
print(marks)

# Получаем все книги имеющиеся у студента
query = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(query, [student_id])
books = cursor.fetchall()
print(books)

# Получаем всю информацию о студенте
query = """
    SELECT
        st.id AS student_id,
        st.name AS student_name,
        st.second_name AS student_second_name,
        g.title AS group_title,
        b.title AS book_title,
        m.value AS mark_value,
        l.title AS lesson_title,
        sj.title AS subject_title
    FROM students st
    LEFT JOIN books b ON st.id = b.taken_by_student_id
    LEFT JOIN `groups` g ON st.group_id = g.id
    LEFT JOIN marks m ON st.id = m.student_id
    LEFT JOIN lessons l ON l.id = m.lesson_id
    LEFT JOIN subjets sj ON sj.id = l.subject_id
    WHERE st.id = %s
"""
cursor.execute(query, [student_id])
student_info = cursor.fetchall()
print(student_info)

# Закрытие соединения
cursor.close()
db.close()
