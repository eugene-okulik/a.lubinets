class Book:

    page_material = "бумага"
    text_availability = "имеется"

    def __init__(self, title, author, page_count, isbn, reserved):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def info(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                  f"материал: {self.page_material}, зарезервирована ")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                  f"материал: {self.page_material} ")


first_book = Book("Идиот", "Достоевский", 500, 123456789, False)
second_book = Book("Мастер и Маргарита", "Булгаков", 528, 23456789, True)
third_book = Book("Война и мир", "Достоевский", 5202, 5512377, False)
fourth_book = Book("Мертвые души", "Гоголь", 352, 44125678, False)
fifth_book = Book("Тургенев", "Отцы и дети", 288, 1233567899, False)

fifth_book.info()
second_book.info()
third_book.info()
fourth_book.info()
fifth_book.info()


class SchoolBook(Book):
    def __init__(self, title, author, page_count, subject, tier, isbn, reserved, task_availability):
        super().__init__(title, author, page_count, isbn, reserved)
        self.subject = subject
        self.tier = tier
        self.task_availability = task_availability

    def info(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                  f"предмет: {self.subject}, класс: {self.tier}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                  f"предмет: {self.subject}, класс: {self.tier}")


first_school_book = SchoolBook("Алгебра", "Иванов", 200, "Математика", 9,
                               33441232, False, True)
second_school_book = SchoolBook("История", "Лебедева", 245, "История", 11,
                                44123534, False, False)
third_school_book = SchoolBook("География", "Алексеев", 180, "География", 9,
                               12343466, False, False)
fourth_school_book = SchoolBook("Геометрия", "Зив", 248, "Математика", 9,
                                5543241, True, True)
fifth_school_book = SchoolBook("Химия", "Врублевский", 325, "Химия", 10,
                               43256457, False, False)

first_school_book.info()
second_school_book.info()
third_school_book.info()
fourth_school_book.info()
fifth_school_book.info()
