import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Тесты для функции city_country()."""

    def test_city_country(self):
        """Проверяет корректное форматирование 'City, Country'."""
        formatted_string = city_country('Santiago', 'Chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

        # Дополнительные тестовые случаи
        self.assertEqual(city_country('Paris', 'France'), 'Paris, France')
        self.assertEqual(city_country('Tokyo', 'Japan'), 'Tokyo, Japan')

    def test_city_country_population(self):
        """Проверяет форматирование с указанием населения."""
        formatted_string = city_country('Santiago', 'Chile', 5000000)
        self.assertEqual(formatted_string, 'Santiago, Chile – population 5000000')

        # Дополнительные тестовые случаи
        self.assertEqual(
            city_country('Cairo', 'Egypt', 20000000),
            'Cairo, Egypt – population 20000000'
        )
        self.assertEqual(
            city_country('Sydney', 'Australia', 5300000),
            'Sydney, Australia – population 5300000'
        )


if __name__ == '__main__':
    unittest.main()
