from functools import reduce

# список 
sportsmen = [
    {'name': 'John', 'age': 25, 'sport': 'Football', 'medals': 5, 'competitions': 10},
    {'name': 'Alice', 'age': 23, 'sport': 'Tennis', 'medals': 3, 'competitions': 8},
    {'name': 'Bob', 'age': 30, 'sport': 'Swimming', 'medals': 7, 'competitions': 15},
    {'name': 'Roman', 'age': 19, 'sport': 'Swimming', 'medals': 105, 'competitions': 89},
    {'name': 'Sasha', 'age': 20, 'sport': 'Chess', 'medals':5 , 'competitions': 10},
    {'name': 'Yaroslav', 'age': 20, 'sport': 'Chess', 'medals': 8, 'competitions': 15 },
    {'name': 'Andrey', 'age': 21, 'sport': 'football', 'medals': 2, 'competitions':21 },
    {'name': 'Valeria', 'age': 19, 'sport': 'Swimming', 'medals': 66 , 'competitions': 71},
    {'name': 'Vitaliy', 'age': 21 , 'sport': 'Basketball', 'medals': 1, 'competitions': 1},
    {'name': 'Vadim', 'age': 14, 'sport': 'Cybersport', 'medals': 1, 'competitions': 2},
    {'name': 'Oleksandr', 'age': 26, 'sport': 'Boxing', 'medals': 9, 'competitions': 12},
    {'name': 'Olena', 'age': 22, 'sport': 'Volleyball', 'medals': 4, 'competitions': 9},
    {'name': 'Ihor', 'age': 24, 'sport': 'Wrestling', 'medals': 11, 'competitions': 17},
    {'name': 'Anastasia', 'age': 18, 'sport': 'Gymnastics', 'medals': 15, 'competitions': 25},
    {'name': 'Dmytro', 'age': 9, 'sport': 'Tennis', 'medals': 6, 'competitions': 13},
    {'name': 'Mykola', 'age': 13, 'sport': 'Weightlifting', 'medals': 10, 'competitions': 20},
    {'name': 'Kateryna', 'age': 23, 'sport': 'Skiing', 'medals': 3, 'competitions': 6},
    {'name': 'Taras', 'age': 31, 'sport': 'Running', 'medals': 5, 'competitions': 14},
    {'name': 'Viktoria', 'age': 19, 'sport': 'Swimming', 'medals': 7, 'competitions': 16},
    {'name': 'Maksym', 'age': 17, 'sport': 'Judo', 'medals': 12, 'competitions': 18},
    {'name': 'Valeriy', 'age': 15, 'sport': 'Judo', 'medals': 0, 'competitions': 2}
]

# Обчислення середнього віку спортсменів
def average_age(athletes):
    total_age = sum([athlete['age'] for athlete in athletes])
    return total_age / len(athletes)


def total_medals(athletes):
    return sum([athlete['medals'] for athlete in athletes])

def filter_by_age(athletes, min_age=18):
    return list(filter(lambda athlete: athlete['age'] >= min_age, athletes))

# Підрахунок загальну кількість змагань
def total_competitions(*athletes):
    return sum([athlete['competitions'] for athlete in athletes])

sorted_athletes = sorted(sportsmen, key=lambda x: x['medals'], reverse=True)

# Підрахунок загальної кількості медалей
def recursive_medal_count(athletes, idx=0):
    if idx == len(athletes):
        return 0
    return athletes[idx]['medals'] + recursive_medal_count(athletes, idx + 1)

# Функції map, filter та reduce
# застосування map для отримання імен спортсменів
names = list(map(lambda athlete: athlete['name'], sportsmen))

def filter_medalists(athletes):
    return list(filter(lambda athlete: athlete['medals'] > 10, athletes))

def filter_medalists_1(athletes):
    return list(filter(lambda athlete: athlete['medals'] > 50, athletes))

def filter_medalists_lose(athletes):
    return list(filter(lambda athlete: athlete['medals'] <= 0, athletes))
  
def filter_medalist_one(athletes):
    return list(filter(lambda athlete: 1 <= athlete['medals'] <= 10, athletes))

# Використав reduce для обчислення загальної кількості змагань
total_comp = reduce(lambda total, athlete: total + athlete['competitions'], sportsmen, 0)


# Інтерактивний інтерфейс
def main():
    print("Список спортсменів:")
    for athlete in sportsmen:
        print(f"Ім'я: {athlete['name']}, Вік: {athlete['age']}, Спорт: {athlete['sport']}, Медалі: {athlete['medals']}")

    avg_age = average_age(sportsmen)
    print(f"\nСередній вік спортсменів: {avg_age}")

    total_med = total_medals(sportsmen)
    print(f"Загальна кількість медалей: {total_med}")

    print("\nСпортсмени, відсортовані за кількістю медалей:")
    for athlete in sorted_athletes:
        print(f"{athlete['name']}: {athlete['medals']} медалей")
       
    filtered_athletes = filter_by_age(sportsmen)
    print("\nСпортсмени віком 18 років і старше:")
    for athlete in filtered_athletes:
        print(f"{athlete['name']}, Вік: {athlete['age']}")
        
    while True:
        try:
            b = int(input('\n 1 = Спортсмени, які мають 0 медалей \n 2 = Спортсмени, які мають більше ніж 10 медалей \n 3 = Спортсмени, які мають більше ніж 50 медалей \n 4 = Спортсмени, які мають більше 1 медалі але не більше 10 медалей \n 5 = Вийти \n Введіть: '))
    
            if b == 1:
                medalists = filter_medalists_lose(sportsmen)
                print("\nСпортсмени, які мають 0 медалей:")
                for athlete in medalists:
                    print(f"{athlete['name']}, Медалі: {athlete['medals']}")

            elif b == 2:
                medalists = filter_medalists(sportsmen)
                print("\nСпортсмени, які мають більше ніж 10 медалей:")
                for athlete in medalists:
                    print(f"{athlete['name']}, Медалі: {athlete['medals']}")

            elif b == 3:
                medalists = filter_medalists_1(sportsmen)
                print("\nСпортсмени, які мають більше ніж 50 медалей:")
                for athlete in medalists:
                    print(f"{athlete['name']}, Медалі: {athlete['medals']}")

            elif b == 4:
                medalists = filter_medalist_one(sportsmen)
                print("\nСпортсмени, які мають більше 1 медалі:")
                for athlete in medalists:
                    print(f"{athlete['name']}, Медалі: {athlete['medals']}")

            elif b == 5:
                print("Вихід...")
                break
                
        except ValueError as e:
            print(f"Помилка: {e}. Спробуйте ще раз.")
        
if __name__ == "__main__":
    main()
