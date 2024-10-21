from collections import defaultdict 
from functools import reduce
from datetime import datetime
from collections import Counter



# Підготовка даних
mobile_app = [
    {"User": "Roman", "Time": "03:25:45", "Addition": "Instagram","function": "delete"},
    {"User": "Olexandr", "Time": "12:54:01", "Addition": "Twich", "function": "update"},
    {"User": "Yaroslav", "Time": "22:43:52", "Addition": "Telegram", "function": "download"},
    {"User": "Dmitriy", "Time": "00:42:59", "Addition": "camera", "function": "open"},
    {"User": "Anna", "Time": "00:00:58", "Addition": "App store", "function": "open"},
    {"User": "Volodymyr", "Time": "12:32:12", "Addition": "Telegram", "function": "open"},
    {"User": "Alex", "Time": "08:45:45", "Addition": "Chrome", "function": "open"},
    {"User": "John", "Time": "15:54:12", "Addition": "facebook", "function": "update"},
    {"User": "Valeria", "Time": "22:22:22", "Addition": "Steam", "function": "download"},
    {"User": "Artem", "Time": "19:21:45", "Addition": "Clash Royal", "function": "delete"},
    {"User": "Vitalyi", "Time": "04:08:04", "Addition": "", "function": "update"},
    {"User": "Valera", "Time": "12:42:53", "Addition": "Telegram", "function": "open"},
    {"User": "Sergiy", "Time": "12:43:45", "Addition": "Telegram", "function": "open"},
    {"User": "Robin", "Time": "22:37:31", "Addition": "facebook", "function": "delete"},
    {"User": "Tetiana", "Time": "10:34:42", "Addition": "facebook", "function": "open"},
    {"User": "Anastasia", "Time": "01:43:42", "Addition": "monobank", "function": "download"},
    {"User": "Vyacheslav", "Time": "20:23:32", "Addition": "Дія", "function": "update"},
    {"User": "Sophy", "Time": "01:03:40", "Addition": "Instagram", "function": "open"},
    {"User": "Andrey", "Time": "01:04:22", "Addition": "Instagram", "function": "open"}
]

# Виведення всіх користувачів
def show_all_users(users):
    for user in users:
        print(user)

# Додавання користувача
def add_User(User, new_user,time, addition, function):
    User.append({"User": new_user, "Time": time, "Addition": addition, "function": function})
    print("User успішно додано")

# Видалення функції користувача   
def remove_function(users, index):
    if 0 <= index < len(users):
        users[index]["function"] = None
        print("Функцію успішно видалено")
    else:
        print("Невірний індекс")

# Оновлення користувача
def update_user(user, index, key, value):
    if 0 <= index < len(user):
        user[index][key] = value
        print("Користувача успішно оновлено")
    else:
        print("Невірний індекс")
 
# Фільтрує користувачів за додатком       
def find_addition_by_User(addition, User):
    return list(filter(lambda x: x["Addition"] == addition, User))

# Підраховує користувачів які зробили будь яку функцію з одним додатком
def count_user_by_addition(user, target_addition):
    return reduce(lambda acc, user: acc + 1 if user.get("Addition") == target_addition else acc, user, 0)

# Підраховує найбільш популярний додаток використання користувачами  
def popular_addition_open(data):
    open_entries = [entry["Addition"] for entry in data if entry["function"] == "open"]
    # Підрахунок кількості використань кожного додатку
    addition_counts = Counter(open_entries)
    if addition_counts:
        most_common_addition = addition_counts.most_common(1)[0] # перший елемент у списку
        return most_common_addition # Повертає
    else:
        return None

#Сортування за часом відкриття додатків
def sort_time_by_addition(time):
    return sorted(time, key=lambda x: datetime.strptime(x["Time"], "%H:%M:%S"))

# Інтерактивний інтерфейс

def print_menu():
    print("\n==== Меню аналізу використання мобільних додатків ====")
    print("1. Додати користувача")
    print("2. Видалити функцію користувача")
    print("3. Оновити користувача")
    print("4. Фільтрувати користувачів за додатком")
    print("5. Підрахувати користувачів, що використовували один додаток")
    print("6. Показати найпопулярніший додаток за відкриттями")
    print("7. Сортувати за часом відкриття додатків")
    print("8. Показати всіх користувачів")
    print("9. Вийти")

def main():
    while True:
        print_menu()
        try:
            b = int(input("\nОберіть опцію: "))
            
            if b == 1:
                new_user = input("Введіть ім'я користувача: ")
                time = input("Введіть час (у форматі HH:MM:SS): ")
                addition = input("Введіть додаток: ")
                function = input("Введіть функцію: ")
                add_User(mobile_app, new_user, time, addition, function)
                
            elif b == 2:
                index = int(input("Введіть індекс користувача для видалення функції: "))
                remove_function(mobile_app, index)
                
            elif b == 3:
                index = int(input("Введіть індекс користувача для оновлення: "))
                key = input("Введіть ключ (User, Time, Addition, function): ")
                value = input(f"Введіть нове значення для {key}: ")
                update_user(mobile_app, index, key, value)
                
            elif b == 4:
                addition = input("Введіть додаток для фільтрації: ")
                filtered_users = find_addition_by_User(addition, mobile_app)
                for user in filtered_users:
                    print(user)
                    
            elif b == 5:
                addition = input("Введіть додаток для підрахунку користувачів: ")
                count = count_user_by_addition(mobile_app, addition)
                print(f"Кількість користувачів, що використовували {addition}: {count}")
                
            elif b == 6:
                most_popular = popular_addition_open(mobile_app)
                if most_popular:
                    print(f"Найпопулярніший додаток: {most_popular[0]}, використаний {most_popular[1]} разів")
                else:
                    print("Немає відкритих додатків")
                    
            elif b == 7:
                sorted_users = sort_time_by_addition(mobile_app)
                for user in sorted_users:
                    print(user)
                    
            elif b == 8:
                show_all_users(mobile_app)
                
            elif b == 9:
                print("Вихід...")
                break
                
        except ValueError as e:
            print(f"Помилка: {e}. Спробуйте ще раз.")
            
if __name__ == "__main__":
    main()