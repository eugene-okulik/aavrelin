class Book:
    page_material = 'бумага'
    availability_of_text = True

    def __init__(self, book_title, author, number_of_pages, flag_whether_the_book = False, isbn = None):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.flag_whether_the_book = flag_whether_the_book

    def every_book(self):
        flag_whether_the_book_true = 'зарезервирована'
        if self.flag_whether_the_book:
            return (
                f"Название: {self.book_title},"
                f" Автор: {self.author},"
                f" страниц: {self.number_of_pages},"
                f" материал: {self.page_material},"
                f" {flag_whether_the_book_true}"
            )
        else:
            return (
                f"Название: {self.book_title},"
                f" Автор: {self.author},"
                f" страниц: {self.number_of_pages},"
                f" материал: {self.page_material}"
            )


class SchoolBooks(Book):
    def __init__(self, book_title, author, number_of_pages, lesson, class_name, flag_whether_the_book = False):
        super().__init__(book_title, author, number_of_pages, flag_whether_the_book)
        self.lesson = lesson
        self.class_name = class_name

    def books_for_lesson(self):
        flag_whether_the_book_true = 'зарезервирована'
        if self.flag_whether_the_book:
            return (
                f"Название: {self.book_title},"
                f" Автор: {self.author},"
                f" страниц: {self.number_of_pages},"
                f" предмет: {self.lesson},"
                f" класс: {self.class_name}"
            )
        else:
            return (
                f"Название: {self.book_title},"
                f" Автор: {self.author},"
                f" страниц: {self.number_of_pages},"
                f" предмет: {self.lesson},"
                f" класс: {self.class_name}"
                f" {flag_whether_the_book_true}"
            )


book_1 = Book("Идиот", "Достоевский", 500, True)
book_2 = Book("Евгений Онегин", "Пушкин", 400)
book_3 = Book("Мастер и Маргарита", "Булгаков", 512)
book_4 = Book("Война и мир", "Толстой", 1225)
book_5 = Book("Преступление и наказание", "Достоевский", 672)

for book in [book_1, book_2, book_3, book_4, book_5]:
    print(book.every_book())

school_book_1 = SchoolBooks("Алгебра", "Иванов", 200, "Математика",
                            9, True)
school_book_2 = SchoolBooks("История России", "Петров", 300, "История",
                            10, False)
school_book_3 = SchoolBooks("География", "Иванов", 400, "География",
                            8, True)
school_book_4 = SchoolBooks("Физика", "Максимов", 500, "Физика",
                            11, True)
school_book_5 = SchoolBooks("Биология", "Викторов", 600, "Биология",
                            7, False)

for book_lesson in [school_book_1, school_book_2, school_book_3, school_book_4, school_book_5]:
    print(book_lesson.books_for_lesson())
