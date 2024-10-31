**Тестовые случаи:**

| № | Сценарий | Входные данные (a, b, c) | Ожидаемый результат | Метод проверки |
|---|---|---|---|---|
| 1 | Два различных корня | (1, -3, 2) | 1.0, 2.0 | `assertAlmostEqual` |
| 2 | Один корень (дискриминант = 0) | (1, -2, 1) | 1.0, 1.0 | `assertAlmostEqual` |
| 3 | Нет действительных корней (дискриминант < 0) | (1, 1, 1) | None, None | `assertIsNone` |
| 4 | Коэффициент a = 0 (линейное уравнение/ошибка) | (0, 1, 1) | `ZeroDivisionError` /  `ValueError` (укажите ожидаемое поведение) | `assertRaises(ZeroDivisionError)` /  `assertRaises(ValueError)` |
| 5 | Коэффициент b = 0 | (1, 0, -4) | -2.0, 2.0 | `assertAlmostEqual` |
| 6 | Коэффициент c = 0 | (1, 2, 0) | -2.0, 0.0 | `assertAlmostEqual` |
| 7 | a близкое к нулю (положительное) | (1e-10, -3, 2) |  (Вычислить ожидаемые значения) | `assertAlmostEqual` |
| 8 | a близкое к нулю (отрицательное) | (-1e-10, -3, 2) | (Вычислить ожидаемые значения) | `assertAlmostEqual` |
| 9 | Большие значения коэффициентов | (1e10, 1e10, 1e10) | (Вычислить ожидаемые значения, проверить на переполнение/потерю точности)  | `assertAlmostEqual` (или другой подходящий метод) |
| 10 | Некорректный тип данных: a - строка | ("a", 1, 1) | `TypeError` | `assertRaises(TypeError)` |
| 11 | Некорректный тип данных: b - список | (1, [1], 1) | `TypeError` | `assertRaises(TypeError)` |
| 12 | Некорректный тип данных: c - None | (1, 1, None) | `TypeError` | `assertRaises(TypeError)` |
