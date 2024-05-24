from main import BooksCollector

import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('book_name',
                             ['Пять Пять Пять Пять Пять Пять Пять Шесть!',  # проверка 41 символа
                              'Пять Пять Пять Пять Пять Пять Пять Семь!!!',  # проверка 42 символов
                              'Пять Пять Пять Пять Пять Пять Пять Пять Пять!']  # проверка 45 символов
                             )
    def test_add_new_book_name_longer_than40_false(self, book_name):  # проверка добавления книги с названием длинее 40

        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert len(collector.books_genre) == 0  # книги не добавляются в словарь

    def test_add_new_book_cannot_add_book_duplicate(self):  # проверка на добавление дубликата книги

        collector = BooksCollector()

        collector.add_new_book('Hello test')
        collector.add_new_book('Hello test')

        assert len(collector.books_genre) == 1  # вторая такая же книга не добавилась

    def test_set_book_genre_if_genre_not_in_list(self):  # жанр не добавляется, если его нет в списке

        collector = BooksCollector()

        collector.add_new_book('Hello test')
        collector.set_book_genre('Hello test', 'Жанр которого нет')

        assert collector.books_genre['Hello test'] == ''  # жанр не добавился

    def test_get_book_genre_shows_genre_true(self):  # проверка, что выводится установленный жанр

        collector = BooksCollector()

        collector.add_new_book('Hello test')
        collector.set_book_genre('Hello test', 'Ужасы')

        assert collector.get_book_genre('Hello test') == 'Ужасы'  # выводимый жанр совпадает с установленным

    @pytest.mark.parametrize('book, genre',
                             [
                                ['Book_1', 'Мультфильмы'],
                                ['Book_2', 'Ужасы']
                             ]
                             )
    def test_get_books_with_specific_genre_shows_correct_books(self, book, genre):  # проверяем, что выводятся книги определеннго жанра

        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_with_specific_genre(genre) == [book]

    def test_get_books_genre_if_empty_shows_empty(self):  # проверка вывода пустого словаря

        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    def test_get_books_genre_shows_all_books(self):  # проверка вывода словаря с книгами

        collector = BooksCollector()

        collector.add_new_book('Book_1')
        collector.add_new_book('Book_2')  # добавим 2 книги в словарь
        collector.set_book_genre('Book_1', 'Ужасы')  # первой книге укажем жанр

        assert collector.get_books_genre() == {'Book_1': 'Ужасы', 'Book_2': ''}

    @pytest.mark.parametrize('genre_for_children', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_shows_books_for_children(self, genre_for_children):

        collector = BooksCollector()

        collector.add_new_book('Book_1')
        collector.set_book_genre('Book_1', genre_for_children)  # поочереди проверяем доступные детям жанры

        assert collector.get_books_for_children() == ['Book_1']

    @pytest.mark.parametrize('age_restricted_genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_doesnt_show_restricted_books(self, age_restricted_genre):

        collector = BooksCollector()

        collector.add_new_book('Book_1')
        collector.set_book_genre('Book_1', 'Мультфильмы')  # одна книга для детей
        collector.add_new_book('Book_2')
        collector.set_book_genre('Book_2', age_restricted_genre)  # вторая книга не для детей

        assert collector.get_books_for_children() == ['Book_1']  # показывается только первая книга

    def test_add_book_in_favorites_add_duplicate_false(self):

        collector = BooksCollector()

        collector.add_new_book('Book_1')
        collector.add_book_in_favorites('Book_1')  # добавили книгу в избранное
        collector.add_book_in_favorites('Book_1')  # добавили книгу в избранное повторно

        assert len(collector.favorites) == 1  # проверяем, что книга добавилась только 1 раз

    def test_delete_book_from_favorites_book_deleted(self):

        collector = BooksCollector()

        collector.add_new_book('Book_1')
        collector.add_book_in_favorites('Book_1')
        collector.delete_book_from_favorites('Book_1')

        assert len(collector.favorites) == 0  # проверяем, что писок после удаления стал пустой

    def test_get_list_of_favorites_books(self):

        collector = BooksCollector()

        collector.add_new_book('Book_1')
        collector.add_book_in_favorites('Book_1')
        collector.add_new_book('Book_2')
        collector.add_book_in_favorites('Book_2')  # добавим 2 книги в избранное

        assert collector.get_list_of_favorites_books() == ['Book_1', 'Book_2']  # обе книги в избранном
