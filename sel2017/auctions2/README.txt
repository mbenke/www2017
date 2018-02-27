Jan Wróblewski <xi@mimuw.edu.pl>

Przykładowy projekt wykorzystujący AJAX metodą POST przerobiony z wersji GET i zakodzony na labach 10. Dodany jest także bootstrap.
Zrobiony pod Django 1.7.7 i Pythonem 2.7 (na students). Inne konfiguracje mogą wymagać rekonstrukcji bazy danych i małych modyfikacji kodu.

Projekt zawiera aukcję jednego elementu, w której można anonimowo podbijać cenę.
Cena jest zapisywana w bazie danych, aktualizowana na stronie i sprawdzana czy jest obecnie najwyższa.
