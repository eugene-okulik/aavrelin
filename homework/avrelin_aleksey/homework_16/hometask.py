import csv
import os
import mysql.connector as mysql
import dotenv


dotenv = dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

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
"""
cursor.execute(query)
student_info = cursor.fetchall()

file = 'data.csv'
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(base_path)))
new_file_path = os.path.join(
    homework_path, 'homework', 'eugene_okulik', 'Lesson_16', 'hw_data', file
)


with open(new_file_path, newline='') as csv_new:
    file = csv.reader(csv_new)
    csv_data = []
    for row in file:
        csv_data.append(row)

for csv_row in csv_data:
    (
        name, second_name, group_title,
        book_title, subject_title, lesson_title,
        mark_value
    ) = csv_row
    found_in_base = "Не найдено"
    for base_row in student_info:
        if (
                base_row['student_name'] == name and
                base_row['student_second_name'] == second_name and
                base_row['group_title'] == group_title and
                base_row['book_title'] == book_title and
                base_row['subject_title'] == subject_title and
                base_row['lesson_title'] == lesson_title and
                str(base_row['mark_value']) == mark_value
        ):
            found_in_base = "Найдено"
            break

    if found_in_base == "Не найдено":
        print(
            f'name: {name}, second_name: {second_name}, '
            f'group_title: {group_title}, book_title: {book_title}, '
            f'subject_title: {subject_title}, lesson_title: {lesson_title}, '
            f'mark_value: {mark_value}'
        )

cursor.close()
db.close()
