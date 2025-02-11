# Создайте студента (student) - 4284
INSERT INTO students (name, second_name) VALUES ('Aleksey', 'Mansem')
SELECT * FROM students ORDER BY id DESC LIMIT 1

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их (6282-6283)
INSERT INTO books (title, taken_by_student_id) VALUES ('Lesson_SQL_10/02', 4284);
INSERT INTO books (title, taken_by_student_id) VALUES ('Lesson_SQL_09/02', 4284);
SELECT * FROM books ORDER BY id DESC LIMIT 2

# Создайте группу (group) и определите своего студента туда (2689)
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Moskow', '10.02.2025', '10.02.2026');
SELECT * FROM `groups` WHERE title = 'Moskow'
UPDATE students SET group_id = 2689  WHERE id = 4284
SELECT * FROM students  WHERE name = 'Aleksey'

# Создайте несколько учебных предметов (subjects) (4298-4299)
INSERT INTO subjets (title) VALUES ('математика');
INSERT INTO subjets (title) VALUES ('физика');


# Создайте по два занятия для каждого предмета (lessons) (8030-8033)
SELECT * FROM subjets ORDER BY id DESC LIMIT 2
INSERT INTO lessons (title, subject_id) VALUES ('Занятие-1', 4298);
INSERT INTO lessons (title, subject_id) VALUES ('Занятие-2', 4298);
INSERT INTO lessons (title, subject_id) VALUES ('Занятие-3', 4299);
INSERT INTO lessons (title, subject_id) VALUES ('Занятие-4', 4299);
#id (8030-8033)
SELECT * FROM lessons ORDER BY id DESC LIMIT 8

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUE (4, 8030, 4284);
INSERT INTO marks (value, lesson_id, student_id) VALUE (3, 8031, 4284);
INSERT INTO marks (value, lesson_id, student_id) VALUE (5, 8032, 4284);
INSERT INTO marks (value, lesson_id, student_id) VALUE (2, 8033, 4284);
# Проверка (id 6301-6304)
SELECT * FROM marks ORDER BY id DESC LIMIT 8


# Получите информацию из базы данных:
# Все оценки студента
SELECT * FROM marks WHERE student_id = 4284

# Все книги, которые находятся у студента
SELECT * FROM books WHERE taken_by_student_id = 4284

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
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
INNER JOIN books b ON st.id = b.taken_by_student_id
INNER JOIN `groups` g ON st.group_id = g.id
INNER JOIN marks m ON st.id = m.student_id
INNER JOIN lessons l ON l.id = m.lesson_id
INNER JOIN subjets sj ON sj.id = l.subject_id
WHERE st.id = 4284;
