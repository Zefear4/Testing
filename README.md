**Тестовые случаи:**

| № | Сценарий | Входные данные (a, b, c) | Ожидаемый результат |
|---|---|---|---|
| 1 | Два различных корня | (1, -3, 2) | 1.0, 2.0 |
| 2 | Один корень (дискриминант = 0) | (1, -2, 1) | 1.0, 1.0 |
| 3 | Нет действительных корней (дискриминант < 0) | (1, 1, 1) | None, None |
| 4 | Коэффициент a = 0 (линейное уравнение/ошибка) | (0, 1, 1) | `ZeroDivisionError`|
| 5 | Коэффициент b = 0 | (1, 0, -4) | -2.0, 2.0 
| 6 | Коэффициент c = 0 | (1, 2, 0) | -2.0, 0.0
| 7 | Некорректный тип данных: a - строка | ("a", 1, 1) | `TypeError` |