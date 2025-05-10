from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    
    def test_default_value_in_init(self,collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # добавляем новую книгу
    def test_add_new_book_add_two_books_success(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_add_two_same_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби') 
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name_of_book', ['', '01234567890123456789012345678901234567890123456789'])
    def test_add_new_book_add_book_with_uncorrecte_len(self, collector, name_of_book): 
        collector.add_new_book(name_of_book)
        assert len(collector.books_genre) == 0
    
    # устанавливаем книге жанр
    def test_set_book_genre_correct_genre_success(self,collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert collector.books_genre['Мастер и Маргарита'] == 'Фантастика'
    
    def test_set_book_genre_uncorrect_genre_fail(self,collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Мистика')
        assert collector.books_genre['Мастер и Маргарита'] == ''

    def test_set_book_genre_without_book_fail(self,collector):
        collector.set_book_genre('Мастер и Маргарита', 'Мистика')
        assert len(collector.books_genre) == 0

    # получаем жанр книги по её имени
    def test_get_book_genre_success(self,collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Ужасы')
        assert collector.get_book_genre('Мастер и Маргарита') == 'Ужасы'

    def test_get_book_genre_nothing_in_genre(self,collector): 
        collector.add_new_book('Мастер и Маргарита')
        assert collector.get_book_genre('Мастер и Маргарита') == ''

    def test_get_book_genre_no_book(self,collector): 
        assert collector.get_book_genre('Мастер и Маргарита') is None

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_success(self,collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        collector.add_new_book('Библия')
        collector.set_book_genre('Библия', 'Фантастика')        
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_with_specific_genre_no_books_with_genre(self,collector):
        collector.add_new_book('Мастер и Маргарита') 
        assert collector.get_books_with_specific_genre("Фантастика") == []

    def test_get_books_with_specific_genre_empty_books_genre(self,collector):
        assert collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_with_specific_genre_uncorrect_genre(self,collector):
        assert collector.get_books_with_specific_genre('Мистика') == []
           
    # получаем словарь books_genre
    def test_get_books_genre_one_position(self,collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Ужасы')
        assert collector.books_genre == {'Мастер и Маргарита': 'Ужасы'}

    def test_get_books_genre_one_position_without_genre(self,collector):
        collector.add_new_book('Мастер и Маргарита')
        assert collector.books_genre == {'Мастер и Маргарита': ''}

    def test_get_books_genre_nothing(self,collector): 
        assert collector.books_genre == {}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_suitable(self, collector):
        collector.add_new_book('Библия')
        collector.set_book_genre('Библия', 'Комедии')
        assert 'Библия' in collector.get_books_for_children()

    def test_get_books_for_children_unsuitable(self, collector):
        collector.add_new_book('Трудовой кодекс')
        collector.set_book_genre('Трудовой кодекс', 'Ужасы')
        assert 'Трудовой кодекс' not in collector.get_books_for_children()

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert len(collector.get_list_of_favorites_books()) == 1
    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.delete_book_from_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' not in collector.get_list_of_favorites_books()
    
    def test_delete_book_from_favorites_another_book(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.delete_book_from_favorites('Библия')
        assert len(collector.get_list_of_favorites_books())==1
        
    # получаем список Избранных книг
    def test_get_list_of_favorites_books_success(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Библия')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Библия')
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита', 'Библия']

    def test_get_list_of_favorites_books_empty_list(self, collector):
        assert collector.get_list_of_favorites_books() == []
