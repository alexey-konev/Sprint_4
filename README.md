# qa_python

1) test_add_new_book_name_longer_than40_false:
Проверяем, что книга с названием длинее 40 символов не добавляется в словарь books_genre
Параметризация: поочередно проверяем граничные значения (41, 42 символа) и значение в середине КЭ (45 символов)

2) test_add_new_book_cannot_add_book_duplicate:
Проверяем, что дубликат книги не добавился в словарь books_genre

3) test_set_book_genre_if_genre_not_in_list:
Проверяем, что книге не устанавливается жанр, если его нет в списке genre 

4) test_get_book_genre_shows_genre_true:
Проверка, что установленный жанр книги совпадает с выводимым

5) test_get_books_with_specific_genre_shows_correct_books:
Проверяем, что выводятся книги, соответсвующие выбранному жанру
Параметризация: проверяем две разные книги с двумя разными жанрами

6) test_get_books_genre_if_empty_shows_empty:
Проверка вывода пустого словаря

7) test_get_books_genre_shows_all_books:
Проверяем, что выводятся все книги добавленные в словарь books_genre, даже если у книги нет жанра

8) test_get_books_for_children_shows_books_for_children:
Проверяем, что если у книги жанр 'Фантастика', 'Мультфильмы' или 'Комедии', то она выводится
Параметризация: поочередно перебираем доступные детям жанры

9) test_get_books_for_children_doesnt_show_restricted_books:
Проверяем, что если у книги жанр 'Ужасы' или 'Детективы', то она не выводится
Параметризация: поочередно перебираем не доступные детям жанры

10) test_add_book_in_favorites_add_duplicate_false:
Проверяем, что добавить книгу в избранное можно только 1 раз

11) test_delete_book_from_favorites_book_deleted:
Проверяем, что книга удалилась из избранного

12) test_get_list_of_favorites_books:
Проверяем, что выводятся все книги в избранном