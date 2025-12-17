# Задание 9-5: Login Attempts

class User:
    """Модель пользователя"""
    
    def __init__(self, first_name, last_name, age, location):
        """Инициализирует атрибуты пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0  # Новый атрибут для подсчета попыток входа
    
    def describe_user(self):
        """Выводит информацию о пользователе"""
        print(f"Пользователь: {self.first_name} {self.last_name}")
        print(f"Возраст: {self.age}")
        print(f"Местоположение: {self.location}")
        print(f"Попыток входа: {self.login_attempts}")
    
    def greet_user(self):
        """Приветствует пользователя"""
        print(f"Привет, {self.first_name}! Рады видеть вас снова.")
    
    def increment_login_attempts(self):
        """Увеличивает количество попыток входа на 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Сбрасывает количество попыток входа до 0"""
        self.login_attempts = 0


# Создаем экземпляр пользователя
user = User("Анна", "Иванова", 28, "Москва")

# Увеличиваем попытки входа несколько раз
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Проверяем текущее количество попыток
print(f"Попыток входа после 3 инкрементов: {user.login_attempts}")

# Сбрасываем попытки входа
user.reset_login_attempts()
print(f"Попыток входа после сброса: {user.login_attempts}")

# Дополнительная демонстрация
user.describe_user()
user.greet_user()