# Задание 9-4: Number Served
# Основываясь на упражнении 9-1

class Restaurant:
    """Простая модель ресторана"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты названия ресторана и типа кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Добавляем новый атрибут с дефолтным значением 0
        self.number_served = 0  # Количество обслуженных посетителей
    
    def describe_restaurant(self):
        """Выводит информацию о ресторане"""
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт"""
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")
    
    def set_number_served(self, number):
        """Устанавливает количество обслуженных посетителей"""
        self.number_served = number
    
    def increment_number_served(self, additional_customers):
        """Увеличивает количество обслуженных посетителей"""
        self.number_served += additional_customers


# Создаем экземпляр ресторана
restaurant = Restaurant("La Bella Italia", "итальянская")

# 1. Выводим количество обслуженных посетителей (должно быть 0)
print(f"Количество обслуженных посетителей: {restaurant.number_served}")

# 2. Меняем значение напрямую и выводим снова
restaurant.number_served = 10
print(f"Количество обслуженных посетителей после изменения: {restaurant.number_served}")

# 3. Используем метод set_number_served() для установки нового значения
restaurant.set_number_served(25)
print(f"Количество обслуженных посетителей после set_number_served(): {restaurant.number_served}")

# 4. Используем метод increment_number_served() для увеличения значения
# Допустим, за день обслужено 15 посетителей
restaurant.increment_number_served(15)
print(f"Количество обслуженных посетителей после increment_number_served(): {restaurant.number_served}")

# Демонстрация других методов из упражнения 9-1
restaurant.describe_restaurant()
restaurant.open_restaurant()